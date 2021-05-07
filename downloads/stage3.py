def stu2b(account):
    if account == "40823231":   #學號40823231變成40823231-2
        return account + "-2"
    elif account[0:3] == "407":  #學號407xxxxx變成s407xxxxx
        return "s" + account
    else:
        return account                #其他學號按照原本學號
 
teamb = []
 
# open file, default is read mode, since txt content no chinese char
# no encoding = "UTF-8" is needed
with open("stage3_2b.txt") as fh:       #開啟檔案
    # readlines will read into the whole line and put into list format
    # has \n at the end of each line
    data = fh.readlines()
#print(len(data))
for i in range(len(data)):
    group = data[i].rstrip("\n").split("\t")
    teamb.append(group)
     
output = ""    
seperator = "-"*10 + "<br />"       #分隔線
 
for i in teamb[0:]:
    team = i[0]                              #小組 組長 其他六個組員
    leader = stu2b(i[1])
    m1 = stu2b(i[3])
    m2 = stu2b(i[5])
    m3 = stu2b(i[7])
    m4 = stu2b(i[9])
    m5 = stu2b(i[11])
    m6 = stu2b(i[13])
     
    try:
        m7 = stu2b(i[15])               #第七個組員
    except:
        m7 = ""
    try:
        m8 = stu2b(i[17])               #第八個組員
    except:
        m8 = ""
         
    leaderrepo = "<a href='http://github.com/" + leader + "/cd2021'>" + leader + " repo</a>"        #組長以及組員的倉儲和網站
    leadersite = "<a href='http://" + leader + ".github.io/cd2021'>" + leader +  " site</a>"
    m1repo = "<a href='http://github.com/" + m1 + "/cd2021'>" + m1 + " repo</a>"
    m1site = "<a href='http://" + m1 + ".github.io/cd2021'>" + m1 +  " site</a>"
    m2repo = "<a href='http://github.com/" + m2 + "/cd2021'>" + m2 + " repo</a>"
    m2site = "<a href='http://" + m2 + ".github.io/cd2021'>" + m2 +  " site</a>"
    m3repo = "<a href='http://github.com/" + m3 + "/cd2021'>" + m3 + " repo</a>"
    m3site = "<a href='http://" + m3 + ".github.io/cd2021'>" + m3 +  " site</a>"
    m4repo = "<a href='http://github.com/" + m4 + "/cd2021'>" + m4 + " repo</a>"
    m4site = "<a href='http://" + m4 + ".github.io/cd2021'>" + m4 +  " site</a>"
    m5repo = "<a href='http://github.com/" + m5 + "/cd2021'>" + m5 + " repo</a>"
    m5site = "<a href='http://" + m5 + ".github.io/cd2021'>" + m5 +  " site</a>"
    m6repo = "<a href='http://github.com/" + m6 + "/cd2021'>" + m6 + " repo</a>"
    m6site = "<a href='http://" + m6 + ".github.io/cd2021'>" + m6 +  " site</a>"
  
 
    teamrepo = "<a href='http://github.com/" + leader + "/" + team + "'>" + team + " repo</a>"      #小組的倉儲含網站
    teamsite =  "<a href='http://" + m1 + ".github.io/" + team + "'>" + team +  " site</a>"
 
    output += teamrepo + " | " + teamsite + " | " +leaderrepo + " | " + leadersite + " | " +m1repo + " | " + m1site + " | " +m2repo + " | " + m2site + " | " +m3repo + " | " + m3site + " | " +m4repo + " | " + m4site + " | " +m5repo + " | " + m5site + " | " +m6repo + " | " + m6site 
     
    if m7 != "":
       m7repo = "<a href='http://github.com/" + m7 + "/cd2021'>" + m7 + " repo</a>"                     #如果有第七個組員會再加倉儲和網站沒有的話就空白
       m7site = "<a href='http://" + m7 + ".github.io/cd2021'>" + m7 +  " site</a>"   
       output += " |  " + m7repo + "| " + m7site
    else:
        output += "" 
     
    if m8 != "":
       m8repo = "<a href='http://github.com/" + m8 + "/cd2021'>" + m8 + " repo</a>"                     #如果有第八個組員會再加倉儲和網站最後再加分隔線
       m8site = "<a href='http://" + m8 + ".github.io/cd2021'>" + m8 +  " site</a>"   
       output += " |  " + m8repo + "| " + m8site + "<br />" + seperator
    else:
        output += "<br />" + seperator
 
 
print(output)
# the following will use group data to generate needed html