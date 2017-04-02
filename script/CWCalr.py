import xml.etree.ElementTree as ET
tree = ET.parse('C:/Users/SONY/Google 雲端硬碟/Cloud Drive/程式資料/Oxygen/ChinaXML/Calendar/北宋.xml')
root = tree.getroot()
tree1= ET.parse('C:/Users/SONY/Google 雲端硬碟/Cloud Drive/程式資料/Oxygen/ChinaXML/Calendar/南宋.xml')
root1 = tree1.getroot()
for date in root1.findall("date"):
     root.append(date)
SongCal=[""]
for emperor in root.findall("date"):
     nianhaolist=[""]
     for nianhao in emperor.findall("date"):
          yearlist=[""]
          for cyear in nianhao.findall("date"):
               monthlist=[""]
               for cmonth in cyear.findall("date"):
                    daylist=[""]
                    for cday in cmonth.findall("date"):
                         ganzhi = cday.find("note[@n='ganzhi']").text
                         day = cday.find("note[@n='day']").text
                         daylist.append([cday.text, ganzhi, day])
                    monthlist.append([cmonth.text, daylist])
               ganzhi = cyear.find("note[@n='ganzhi']").text
               otherCal = cyear.find("note[@n='otherCal']").text
               yearlist.append([cyear.text, ganzhi, otherCal, monthlist])
          nianhaolist.append([nianhao.text, yearlist])
     SongCal.append([emperor.text, nianhaolist])
