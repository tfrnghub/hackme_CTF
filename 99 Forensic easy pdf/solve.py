import PyPDF2



pdfFile = open('easy.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
for i in range(pdfReader.numPages):
    page = pdfReader.getPage(i)
    print(page.extractText())
pdfFile.close()
