i=0
tempDic={}
for emperor in root.findall("date"):
      for nianhao in emperor.findall("date"):
            tempDic[nianhao.text]={}
            for cyear in nianhao.findall("date"):
                  ganzhi=cyear.find("note[@n='ganzhi']").text
                  tempDic[nianhao.text][ganzhi]=i
                  print (ganzhi)
                  i=i+1
            i=0

              
            
