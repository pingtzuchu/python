import xml.etree.ElementTree as ET
tree = ET.parse('C:/Users/Ping-tzu 2 Chu A1/Google 雲端硬碟/Cloud Drive/程式資料/Oxygen/ChinaXML/XML/From Excel/明朝.xml')
root = tree.getroot()
newRoot=ET.fromstring("<date n='dynasty'>明</date>")
lastEmperor=""
lastNianhao=""
otherCal=0
Year = "1368"
Month = "01"
ganzhi=0
lDays=0
ganzhiList=["甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉", "甲戌", "乙亥", "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未", "甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑", "庚寅", "辛卯", "壬辰", "癸巳", "甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑", "壬寅", "癸卯", "甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑", "甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥"]
for worksheet in root.findall("Worksheet"):
    """nianhao=worksheet.get("name")
    nianhaos.add(nianhao)"""
    for row in worksheet.findall("Row"):
         if len(row.getchildren())==1:
             celltext=row.find("Cell").text
            if celltext.find("歲次") > -1:
                firstrowList=celltext.split("　")
                emperor=firstrowList[0][1:3]
                nianhao=firstrowList[0][3:5]
                cyear=firstrowList[0][5:]
                cyear=cyear[:len(cyear)-2]
                cyearGanzhi=firstrowList[1][3:]
                if not emperor == lastEmperor:
                     print (emperor)
                    lastEmperor = emperor
                    newRoot.append(ET.fromstring("<date n='emperor'>"+emperor+"</date>"))
                if not nianhao == lastNianhao:
                    lastNianhao = nianhao
                    newRoot.find("date[last()]").append(ET.fromstring("<date n='nianhao'>" + nianhao + "</date>"))
                newRoot.find("date[last()]/date[last()]").append(ET.fromstring("<date n='cyear'>" + cyear + "</date>"))
                newRoot.find("date[last()]/date[last()]/date[last()]").append(ET.fromstring("<note n='ganzhi'>" + cyearGanzhi + "</note>"))
                otherCal=1
            elif otherCal==1:
                otherCal=0
                newRoot.find("date[last()]/date[last()]/date[last()]").append(ET.fromstring("<note n='otherCal'>" + celltext + "</note>"))
        elif len(row.getchildren())==34:
             j = 1
             cDay=1
             for cell in row.findall("Cell"):
                celltext=cell.text
                if j==1:
                    newRoot.find("date[last()]/date[last()]/date[last()]").append(ET.fromstring("<date n='cmonth'>" + celltext + "</date>"))
                if j==2:
                    cganzhi=celltext
                    for i in range(60):
                        if ganzhiList[i]==cganzhi:
                            ganzhi=i
                if 13>j>2 or 24>j>13 or j>24:
                    newRoot.find("date[last()]/date[last()]/date[last()]/date[last()]").append(ET.fromstring("<date n='cday'>" + str(cDay) +"</date>"))
                    if len(celltext) >=10:
                        if celltext[5:10]=="01-01":
                            if lDay > 50:
                                Year = str(int(Year)+1)
                                Month="01"
                                lDay = 1
                                celltext="01"
                                newRoot.find("date[last()]/date[last()]/date[last()]/date[last()]/date[last()]").append(ET.fromstring("<note n='day'>"+Year + "-01-01"+"</note>"))
                            else:
                                Month = daytext[5:7]
                                celltext="01"
                    celltext = "0"*(2-len(cell.text)) + celltext
                    newRoot.find("date[last()]/date[last()]/date[last()]/date[last()]/date[last()]").append(ET.fromstring("<note n='ganzhi'>"+ganzhiList[ganzhi] + "</note>"))
                    newRoot.find("date[last()]/date[last()]/date[last()]/date[last()]/date[last()]").append(ET.fromstring("<note n='day'>"+Year + Month+celltext+"</note>"))
                    ganzhi += 1
                    cDay += 1			
newRoot.write("C:/Users/Ping-tzu 2 Chu A1/Google 雲端硬碟/Cloud Drive/程式資料/Python/ming.xml")
