import time 
now = time.strftime("%y-%m-%d %H:%M:%S")
text = input("请输入今天的心情 ：")     #w:写入，每次写入的时候会把之前的内容给清除掉 : a:追加内容
with open("D:\日记.txt","a",encoding="utf8") as f:             #可以指定存放日记.txt文件的位置，定义打开日记.txt文件的代码类型
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("-----------------\n")





#\t (制表符)    \n（换行）

