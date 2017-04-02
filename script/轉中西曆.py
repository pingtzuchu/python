import xml.etree.ElementTree as ET
import re
tree = ET.parse('C:/Users/Ping-tzu 2 Chu A1/Google 雲端硬碟/Cloud Drive/程式資料/Oxygen/ChinaXML/XML/From Excel/更始.xml')
root = tree.getroot()
newRoot = ET.fromstring("<date n='dynasty'>更始朝</date>")
lastEmperor=""
lastNianhao=""
otherCal=0
Month = "01"
ganzhi = 0
ganzhiList=["甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉", "甲戌", "乙亥", "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未", "甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑", "庚寅", "辛卯", "壬辰", "癸巳", "甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑", "壬寅", "癸卯", "甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑", "甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥"]
for worksheet in root.findall("Worksheet"):
        worksheet.tag="date"
        for row in worksheet.findall("Row"):
                if len(row.getchildren())==1:
                        celltext=row.find("Cell").text
                        if celltext.find("歲次") > -1:
                                print(celltext)
                                firstrowList=celltext.split("　")
                                firstrowList[0]=firstrowList[0][len(newRoot.text):]
                                emperor=firstrowList[0][0:len(re.split(r"王莽|[帝后祖宗王兒主嬰莽玄公侯]", firstrowList[0])[0])+1]
                                nianhao=firstrowList[0][len(emperor):]
                                nianhao=re.split(r"\d?\d?元?年", nianhao)[0]
                                cyear=firstrowList[0][len(emperor)+len(nianhao):]
                                cyear=cyear[:len(cyear)-1]
                                Year = firstrowList[3][2:len(re.split("年", firstrowList[3])[0])]
                                Year = "0"*(4-len(Year)) + Year
                                cyearGanzhi=firstrowList[1][3:]
                                if not emperor == lastEmperor:
                                        lastEmperor = emperor
                                        newRoot.append(ET.fromstring("<date n='emperor'>"+emperor+"</date>"))
                                        emperorChanged=1
                                if (not nianhao == lastNianhao) or (emperorChanged==1):
                                        emperorChanged=0
                                        lastNianhao=nianhao
                                        newRoot.find("date[last()]").append(ET.fromstring("<date n='nianhao'>"+nianhao+"</date>"))
                                newRoot.find("date[last()]/date[last()]").append(ET.fromstring("<date n='cyear'>" + cyear + "<note n='ganzhi'>" + cyearGanzhi + "</note>"+"</date>"))                         
                                otherCal=2
                        elif otherCal==1:
                                otherCal=0
                                newRoot.find("date[last()]/date[last()]/date[last()]").append(ET.fromstring("<note n='otherCal'>" + celltext + "</note>"))
                elif len(row.getchildren())==34:
                        j = 1	#每列格子數
                        if not row.find("Cell").text == "份":
                                cDay = 1    
                                for cell in row.findall("Cell"):
                                        celltext=cell.text
                                        if j==1:
                                                newRoot.find("date[last()]/date[last()]/date[last()]").append(ET.fromstring("<date n='cmonth'>" + celltext + "</date>"))
                                        if j==2:	#設定日干支
                                                for i in range(60):
                                                        if ganzhiList[i]==celltext:
                                                                ganzhi=i
                                        if 13>j>2 or 24>j>13 or j>24:
                                                newRoot.find("date[last()]/date[last()]/date[last()]/date[last()]").append(ET.fromstring("<date n='cday'>" + str(cDay) +"</date>"))
                                                if len(celltext) >=10:
                                                        Month = celltext[5:7]
                                                        celltext = celltext[8:10]
                                                celltext = "0"*(2-len(cell.text)) + celltext
                                                newRoot.find("date[last()]/date[last()]/date[last()]/date[last()]/date[last()]").append(ET.fromstring("<note n='ganzhi'>"+ganzhiList[ganzhi] + "</note>"))
                                                newRoot.find("date[last()]/date[last()]/date[last()]/date[last()]/date[last()]").append(ET.fromstring("<note n='day'>"+Year + "-" + Month + "-" +celltext+"</note>"))
                                                ganzhi += 1
                                                if ganzhi == 60:
                                                        ganzhi=0
                                                cDay += 1
                                        j += 1
                otherCal -= 1
tree._setroot(newRoot)
tree.write("C:/Users/Ping-tzu 2 Chu A1/Google 雲端硬碟/Cloud Drive/程式資料/Python/更始.xml", encoding="utf-8")
