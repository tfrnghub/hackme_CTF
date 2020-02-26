import struct


from pdfminer.layout import LAParams
from pdfminer.layout import LTTextBox, LTTextLine, LTFigure, LTImage, LTTextBoxHorizontal
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdftypes import LITERALS_DCT_DECODE
from pdfminer.pdfcolor import LITERAL_DEVICE_GRAY
from pdfminer.pdfcolor import LITERAL_DEVICE_RGB
from pdfminer.pdfcolor import LITERAL_DEVICE_CMYK
from pdfminer.psparser import literal_name
from pdfminer.pdftypes import stream_value,PDFObjRef

def get_colorspace(spec):
    if isinstance(spec, list):
        name = literal_name(spec[0])
    else:
        name = literal_name(spec)
    if name == 'ICCBased' and isinstance(spec, list) and 2 <= len(spec):
        return stream_value(spec[1])['Alternate']
    elif name == 'DeviceN' and isinstance(spec, list) and 2 <= len(spec):
        return PDFColorSpace(name, len(list_value(spec[1])))
    else:
        return PREDEFINED_COLORSPACE.get(name)

def align32(x):
    return ((x+3)//4)*4
##  BMPWriter
##
class BMPWriter:

    def __init__(self, fp, bits, width, height):
        self.fp = fp
        self.bits = bits
        self.width = width
        self.height = height
        if bits == 1:
            ncols = 2
        elif bits == 8:
            ncols = 256
        elif bits == 24:
            ncols = 0
        else:
            raise ValueError(bits)
        self.linesize = align32((self.width*self.bits+7)//8)
        self.datasize = self.linesize * self.height
        headersize = 14+40+ncols*4
        info = struct.pack('<IiiHHIIIIII', 40, self.width, self.height, 1, self.bits, 0, self.datasize, 0, 0, ncols, 0)
        assert len(info) == 40, len(info)
        header = struct.pack('<ccIHHI', b'B', b'M', headersize+self.datasize, 0, 0, headersize)
        assert len(header) == 14, len(header)
        self.fp.write(header)
        self.fp.write(info)
        if ncols == 2:
            # B&W color table
            for i in (0, 255):
                self.fp.write(struct.pack('BBBx', i, i, i))
        elif ncols == 256:
            # grayscale color table
            for i in range(256):
                self.fp.write(struct.pack('BBBx', i, i, i))
        self.pos0 = self.fp.tell()
        self.pos1 = self.pos0 + self.datasize
        return

    def write_line(self, y, data):
        self.fp.seek(self.pos1 - (y+1)*self.linesize)
        self.fp.write(data)
        return



def save_image (image, page_number):
    if image.stream:
        stream = image.stream
        filters = list(stream.get_filters())
        (width, height) = image.srcsize
        
        colorspace=image.colorspace[0]
        #default isinstance(colorspace,PSLiteral) 
        if isinstance(colorspace,PDFObjRef):
            colorspace=get_colorspace(colorspace.resolve())


        if len(filters) == 1 and filters[0][0] in LITERALS_DCT_DECODE:
            ext = '.jpg'
        elif (image.bits == 1 or
              image.bits == 8 and colorspace in (LITERAL_DEVICE_RGB, LITERAL_DEVICE_GRAY)):
            ext = '.%dx%d.bmp' % (width, height)
        else:
            ext = '.%d.%dx%d.img' % (image.bits, width, height)
            
        name = str(page_number)+"_"+image.name+ext
        with open(name, 'wb') as fp:
            if ext == '.jpg':
                raw_data = stream.get_rawdata()
                if LITERAL_DEVICE_CMYK in image.colorspace:
                    from PIL import Image
                    from PIL import ImageChops
                    ifp = BytesIO(raw_data)
                    i = Image.open(ifp)
                    i = ImageChops.invert(i)
                    i = i.convert('RGB')
                    i.save(fp, 'JPEG')
                else:
                    fp.write(raw_data)
            elif image.bits == 1:
                bmp = BMPWriter(fp, 1, width, height)
                data = stream.get_data()
                i = 0
                width = (width+7)//8
                for y in range(height):
                    bmp.write_line(y, data[i:i+width])
                    i += width
            elif image.bits == 8 and colorspace is LITERAL_DEVICE_RGB:
                bmp = BMPWriter(fp, 24, width, height)
                data = stream.get_data()
                i = 0
                width = width*3
                for y in range(height):
                    bmp.write_line(y, data[i:i+width])
                    i += width
            elif image.bits == 8 and colorspace is LITERAL_DEVICE_GRAY:
                bmp = BMPWriter(fp, 8, width, height)
                data = stream.get_data()
                i = 0
                for y in range(height):
                    bmp.write_line(y, data[i:i+width])
                    i += width
            else:
                fp.write(stream.get_data())
        return name
        



#document = open('this-is-a-pen.pdf', 'rb')
document = open('test.pdf', 'rb')
#Create resource manager
rsrcmgr = PDFResourceManager()
# Set parameters for analysis.
laparams = LAParams()
# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
for i,page in enumerate(PDFPage.get_pages(document)):
    interpreter.process_page(page)
    # receive the LTPage object for the page.
    layout = device.get_result()
    for element in layout:
        if isinstance(element, LTTextBoxHorizontal):
            print(element.get_text())
        if isinstance(element, LTImage):
            print(save_image(element, i))
        if isinstance(element, LTFigure):
            for obj in element._objs:
                if isinstance(obj, LTImage):
                    print(save_image(obj, i))

