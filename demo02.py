# #判断
# # a = 1 
# # b =2 

# # if a ==1:
# #     print("哈哈哈")

# # if a > b :
# #     print("a比b大")   #两种条件语句的选择判断，代码要对齐，其属于同一个代码块。（按住TAB健可以自动缩进，其缩进四个空格代表代码块）
# # else :
# #      print("a比b小")

# # age = int(input("请输入你的年龄 ："))    #从上到下运行（从大到小），满足一个条件后就输出相应的结果。
# # if age >60 :
# #     print("你应该退休了")
# # elif  age > 30 :
# #     print("家庭的责任重要")
# # elif  age >20  :
# #     print("一定要好好规划自己的职业规划")
# # else :
# #     print("好好读书")



# # if age > 20 and age <=30:   #if elif多种条件语句选择判断，这种形式就是当第一种情况不满足的时候会进行第二种情况的判断，如果仍然不满足会进行第三种情况的判断，以此类推，如果还不满足就直接else处理。
# #     print("22222222")
# # elif age > 30:
# #     print("333333333")
# # elif age > 60:
# #     print("66666666")
# # else:
# #     print("xxxxxxxxxx") 

# #if 语句的嵌套：关于if语句的嵌套，就是指满足一个if语句之后，在它的条件语句里再进行一个if语句的判断，这种形式的嵌套形式在筛选数据或者条件过滤的时候常用到。

#  year = int(input("输入一个年份: "))
#  if (year % 4) == 0:               #满足能被四整除
#      if (year % 100) == 0:         #满足能被四整除且能被一百整除  
#          if (year % 400) == 0:     #满足既能被四整除，也能被一百整除，还能被四百整除
#              print(year,"是闰年")  # 是整百年但能被400整除的
#          else:
#              print(year,"不是闰年") #是整百年但不能被400整除
#      else:
#          print(year, "是闰年")  # 不是整百年但能被4整除的
#  else:
#      print(year,"不是闰年")     #不能被四整除

# """

# 公历闰年判定遵循的规律为: 四年一闰,百年不闰,四百年再闰.
# 公历闰年的简单计算方法（符合以下条件之一的年份即为闰年）
# 1.能被4整除而不能被100整除.
# 2.能被400整除

# """

# """
# if的判断条件:== , != , > , < , in , is ,not in ,not is 。

# """
# == ； 判断是否相等
# =  ：赋值

# in : 判断字典，数值等数据类型里是否有输入的内容
# is ：判断类型

# a = "你好"
# if a in ["你好","不好"] :
#     print("ok")
# else :
#     print("不ok")


# a = input("请输入：")
# if a == "":
#     print("不能为空！")
#     exit()
# if a in "0123456789":
#     a = int(a)
# else:
#     print("请输入正确的年龄！")
#     exit()
# if a > 5:
#     print("大")
# else:
#     print("小")



# a = 233
# if type(a) is int :
#     print("是数字")
# elif type(a) is str :
#     print("是字符串")
# else :
#     print("其他")




# a = 1
# while a < 10 :                 #while判断循环条件,通过条件控制循环的次数，a是在变化的
#      print("爱你"，a)
#      a = a +1

# 练习：现在有11个人的成绩，需要录入到系统中。
# 这是个人分别是，张三、李四、王麻子、浪晋、流云、希希、小梁、二狗、陈平安、朱珠、亚索
# 并且名字和成绩需要对应上。
# 而且大于60的和小于60的需要分开存放。

# highchengji = {}  # 定义了一个空字典，用来存储大于60的信息
# lowchengji = {}  # 定义了一个空字典，用来存储小于60的信息
# studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# a = 0  # 定义了一个变量，用来控制数组的下标的变化
# while a < len(studentlist):  # 因为所有的人的信息的录入，都是要用input，所有写了循环，len判断了数组的长度，总长度-1就是最大的下标
#     chengji = int(input("请输入"+studentlist[a]+"的成绩："))  # 录入信息，为了方便判断，所以转换了格式
#     if chengji >= 60:  # 判断分数
#         highchengji[studentlist[a]] = chengji  # 存到字典中
#     else:
#         lowchengji[studentlist[a]] = chengji
#     a = a + 1  # 控制下标变化，每一次循环，都+1
# print("大于60的：",highchengji)
# print("小于60的：",lowchengji)

# # 遍历
# # i 为遍历对象的值 ,自动变化。范围左闭右开。
# a =  ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# for i in a :
#     print(i)

# b = list(range(0,10,2))   #数列生成器，这条自动生成了一个步长为二的数列，若不加后面的参数则步长为默认为1。
# print(b)                  #数列的范围也遵循左闭右开的规则，不包含计数的最后一位。

# for i in range(100):
#     print(i)

#用for语句写的练习：

# highchengji = {}  # 定义了一个空字典，用来存储大于60的信息
# lowchengji = {}  # 定义了一个空字典，用来存储小于60的信息
# studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# for i in studentlist:  
#     chengji = int(input("请输入"+i+"的成绩："))  # 录入信息，为了方便判断，所以转换了格式
#     if chengji >= 60:  # 判断分数
#         highchengji[i] = chengji  # 存到字典中
#     else:
#         lowchengji[i] = chengji
# print("大于60的：",highchengji)
# print("小于60的：",lowchengji)

"""
练习：
打印九九乘法表
"""
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"X",j,"=",i*j,end="  ")
#     print()


# end = " "  #控制在循环中不换行,可以将结果输出到同一行或者在输出末尾添加不同的字符。
# print()    #起到了上一次的循环结束后换行的作用，
 
# python的print(" ")换行问题

# 1.print(" ")执行后,默认换行,光标停留在下一行.

# 2.要让print(" ")执行输出后不换行,方法:print("XXXXX ",end=" ")

# 3.原因:print(" ")之所以换行是因为print里的字符串""的最后一个end为"/n",即换行,要使其不换行,只需改变end即可

# 4.python中“end=”用法：例如print（“#”，end=" \n")，默认换行，print（“#”，end=" ")则在循环中不换行


# """
# 练习1：
# 通过print打印，模拟一个红绿灯的功能，注意：红灯30次，绿灯35次，黄灯3次。
# 练习2：
# 使用代码，实现一个注册的功能。
# 用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头。
# 储到到字典中，{username:password}
# """
"""
自己写的
"""

# print("红灯开始")
# # while True :
# for i in range(30) :
#         print("红灯倒计时还有",30-i,"秒结束")
# print("红灯结束，绿灯开始")
# for j in range(35) :
#         print("绿灯倒计时还有",35-j ,"秒结束")
# print("绿灯结束,黄灯开始")
# for k in range(3) :
#         print("黄灯倒计时还有",3-k ,"秒结束")
# print("黄灯结束")


# dict ={}
# a = input("请输入账号:")
# if len(a) >=5 and len(a) <=8 :
#     if  a[0] in "abcdefghijklmnopqrstuvwxyz" :
#         pass                                       #pass:空语句代表什么也不做，保证格式和语句完整。
#     else :
#         print("账号必须是小写字母开头！")
#         exit()
# else :
#     print("要求账号长度是5-8位！")
#     exit()
# b = input("请输入密码 ：")
# if len(b) >=6 and len(b) <=12 :
#     dict[a]= b
# else :
#     print("请输入正确的密码格式，密码长度6-12位！")
#     exit()
# print("注册成功！")
# print(dict)

"""
老师写的

"""

# light = {"红灯":35,"绿灯":30,"黄灯":3}        #字典的遍历是key的遍历
# for i in light :
#     for j in range(light[i]):
#         print(i,"倒计时还有",light[i]-j,"秒")

# username = input("请输入账号 ：")
# password = input("请输入密码 ：")
# if len(username) >=5 and len(username) <=8 :
#     if username[0] in "qwertyuiopasdfghjklzxcvbnm" :
#         if len(password) >=8 and len(password) <= 12 :
#             print("注册成功",{username :password})
#         else :
#             print("密码必须8—12位！")
#     else :
#         print("账号的首字母必须小写字母开头！")
# else :
#     print("账号的长度不符合规范，请输入5-8位的账号！")

#跳出循环和终止循环

#  continue:在循环中越过、跳过某一次循环，不会执行后面的代码，然后重新开始下一次的循环。
#  break : 终止循环或者是跳出整个一层循环队列,它放到那一层循环就对那一层循环生效。

# for i in range(10):
#     if i == 4 :
#         continue
#     print(i)
# print("-----------------")
# for i in range(10):
#     if i == 4 :
#         break
#     print(i)

#方法(函数)的定义

#方法的参数不一定是必须的（方法有的是本身自带的，有的是自定义创建的）
#自定义的方法自己可以加注释解释。方法的名称是唯一的。

# def checkname(username):
#     """  
#     自动判断账号长度是5-8位，并且账号必须小写开头。

#     """
#     if len(username) >=5 and len(username) <=8 :
#         if username[0] in "qwertyuiopasdfghjklzxcvbnm" :
#                 print("ok")
#         else :
#             print("账号的首字母必须小写字母开头！")
#     else :
#         print("账号的长度不符合规范，请输入5-8位的账号！")

# a ="7uiooi"                 #使用自定义的方法判断输入的账号是否满足要求
# checkname(a)

#def :方法的声明
#checkname:方法的名字
#username:方法的参数(可以没有)
# """" 方法的说明 """"
#方法的逻辑代码

# def jiafa(a,b):
#     """
#     这个方法的作用是实现两个数字相加
#     """
#     if type(a) is int and type(b) is int:
#         print(a+b)
#     else :
#         print("输入的数据类型不正确!")

# jiafa(2,6)
# jiafa("2",6)

# #retur  返回值：返回后我们可以对这个值做其他的操作，也就是得到一个结果后返回一个值给变量来进行后续的操作。
# #print  而print并不能，它只是把结果显示打印出来，并不会拿来使用。

# def checkname(username):
#     """  
#     自动判断账号长度是5-8位，并且账号必须小写开头。

#     """
#     if len(username) >=5 and len(username) <=8 :
#         if username[0] in "qwertyuiopasdfghjklzxcvbnm" :
#                 return True
#         else :
#             return "账号的首字母必须小写字母开头！"
#     else :
#         return "账号的长度不符合规范，请输入5-8位的账号！"

# username = input("请输入账号 ：")
# password = input("请输入密码 ：")
# if  checkname(username) == True :
#     if len(password) >=8 and len(password) <= 12 :
#         print("注册成功",{username :password})
#     else :
#         print("密码必须8—12位！")
# else :
#     print(checkname(username))



# def jiafa(a,b):
#     """
#     这个方法的作用是实现两个数字相加
#     """
#     if type(a) is int and type(b) is int:
#         return a+b
#     else :
#         return "输入的数据类型不正确!"

# a = jiafa(1,2)    #return可以得到这个数据
# print(a+2)


#异常捕获,针对某段代码进行判断是否正确，这样就可以避免报错。
#"type ："和  "except :"必须成对出现。
#若try后面的代码正确，则正常运行，若出现错误则执行except后面的代码。

# try :
#     print("a"+1)                   #except 后面写 typeerror （ 其为错误类型），如果省略就不指定类型，即捕获全部异常，deal为具体的处理语句。
# except :
#     print("上面的代码写错了")

# 异常类

#代码的单位：
#包》模块》 类 》方法 》变量
#之间的关系是即是包含又是并列的关系。

# try :
#     print(2+jiuo)        #异常类自动告诉代码哪里写错了，并告诉其错的原因。
# except Exception as e:
#     print("上面的代码写错了",e)


# a = input("请输入你的名字：")
# b = input("请输入你的年龄：")
# try :
#     if int(b)>18:
#         print("成年了")
#     else :
#         print("未成年")
# except :
#     print("请输入正确的年龄！")

#用来处理用户的输入的数据，尝试不同的数据类型的输入。


#包：1.系统自带的 2.第三方pip（1.安装 ：pip install "包名" 2.卸载 ：pip uninstall "包名" 3.查看 ； pip list)
#模块：各种py文件

#导入系统自带的包来使用,一定是先导入包，首先写在代码的最上面。
# import time
# import random    #生成随机数

# # for i in range(10):   #控制运行的停顿时间
# #     time.sleep(1)
# #     print(i)

# # a = random.randint(100,1000)  #自动生成随机数
# # print(a)

#练习：定义一个方法用来判断用户输入的账号密码是否符合规范

def check(username,password):
    """
    自动判断用户输入的账号密码是否符合规范

    """
    if len(username) >=5 and len(username) <=8 :
        if username[0] in "qwertyuiopasdfghjklzxcvbnm" :
            if len(password) >=8 and len(password) <= 12 :
                return"注册成功",{username :password}
            else :
                return "密码必须8—12位！"
        else :
            return "账号的首字母必须小写字母开头！"
    else :
       return "账号的长度不符合规范，请输入5-8位的账号！"

username=input("请输入账号：")
password=input("请输入密码：")
print(check(username,password))
