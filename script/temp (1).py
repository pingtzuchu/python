e=0
n=0
y=0
m=0
d=0
tempDDic={}
tempMDic={}
tempYDic={}
tempNDic={}
FromGanzhiToDay={}
for emperor in root.findall("date"):
      FromGanzhiToDay={}
      FromGanzhiToDay[emperor.text] = e
      for nianhao in emperor.findall("date")
            for cyear in nianhao.findall("date"):
                  for cmonth in cyear("date"):
                        for cday in cmonth("date"):
                              ganzhi = cday.find("note[@n='ganzhi']")
                              day = cday.find("note[@n='day']")
                              tempDDic[ganzhi] = d
                              d =  d + 1
                        d = 0
                  ganzhi
                  m = 0
                        
                        
                              
