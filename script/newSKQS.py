import re
import docx
source="C:/temp/test.docx"
document=docx.Document(source)
newDoc="""<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml"
	schematypens="http://purl.oclc.org/dsdl/schematron"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>
      <fileDesc>
         <titleStmt>
            <title>Title</title>
         </titleStmt>
         <publicationStmt>
            <p>Publication Information</p>
         </publicationStmt>
         <sourceDesc>
            <p>Information about the source</p>
         </sourceDesc>
      </fileDesc>
  </teiHeader>
  <text>
      <body>
                """ #newXMLfile with several quan <div>s
quanTitle=[] #Title for Quan first level of div
xmlLevel=0 #div level
pageNumber=1 #page number
for para in document.paragraphs:
      if len(para.text)>10:
            firstPara=para.text[:para.text.find("\n")]
            length=len(firstPara)
            runLength=0
            titleList=firstPara.split("/")
            quan=titleList[len(titleList)-1]
            if not (quan in quanTitle): #test whether it is a new quan title
                  quanTitle.append(quan) #add the title into the quan title list
                  if not xmlLevel==0:
                        newDoc += ("</div>" * xmlLevel)+"\n"
                  newDoc += "<div><head>" + quan + "</head>\n" #add in new quan title
                  xmlLevel = 1
                  pageNumber=1
            pageNumber += 1
            newDoc += "<p>"      
            for run in para.runs:
                  runLength += len(run.text)
                  if runLength > length:
                        text=run.text
                        if run.style.name=="內文小註":
                              text="<hi>" + text + "</hi>"
                        if re.match("\\n\\u3000\\u3000\\u3000([^\\u3000])", text): #heading level 3
                              if xmlLevel==3:
                                    text = re.sub("\\n\\u3000\\u3000\\u3000([^\\u3000])", r"</p></div>\n<div><head>\1", text)
                              else:
                                    text = re.sub("\\n\\u3000\\u3000\\u3000([^\\u3000])", r"</p>\n<div><head>\1", text)
                                    xmlLevel=3
                              text += "</head>\n<p>"
                        if re.match("\\n\\u3000\\u3000([^\\u3000])", text): #heading level 2
                              if xmlLevel==2:
                                    text = re.sub("\\n\\u3000\\u3000([^\\u3000])", r"</p></div>\n<div><head>\1", text)
                              elif xmlLevel==1:
                                    xmlLevel=2
                                    text = re.sub("\\n\\u3000\\u3000([^\\u3000])", r"</p>\n<div><head>\1", text)
                              elif xmlLevel==3:
                                    xmlLevel=2
                                    text = re.sub("\\n\\u3000\\u3000([^\\u3000])", r"</p></div></div>\n<div><head>\1", text)
                              text += "</head>\n<p>"
                        newDoc += text
            newDoc += "<pb n='"+str(pageNumber)+"b'/></p>\n"
newDoc += "</div>" * xmlLevel + "</body></text></TEI>"
newName="C:/temp/temp.xml"
fw = open(newName, "w", encoding="utf-8")
fw.write(newDoc)
fw.close
