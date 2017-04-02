import xml.etree.ElementTree as ET
tree = ET.parse('C:/Users/SONY/Google 雲端硬碟/Cloud Drive/程式資料/Oxygen/ChinaXML/XML/南宋.xml')
root = tree.getroot()
daynode=root.findall("./date/date/date/date/date/note[1]")
def addZero(year, digit):
	if len(year) < digit:
		year = "0"*(digit-len(year)) + year
		return year
	else:
		return year
Year = "1127"
Month = "01"
j=1
for day in daynode:
	if len(day.text) >=10:
		if day.text[5:10]=="01-01":
			if j > 50:
				Year = addZero(str(int(Year)+1), 4)
				j = 1
			else:
				pass
			day.text = Year + "-01-01"
		else:
			day.text = Year + day.text[4:10]
			Month = day.text[5:7]
	else:
		day.text = Year + "-" + Month + "-" + addZero(day.text, 2)
	j=j+1
tree.write("C:/Users/SONY/Google 雲端硬碟/Cloud Drive/程式資料/Python/output2.xhtml")
