# print("hello world") #字符串 str
# print(2333)      #整数 int
# print(2.333)     #小数 float
# print(True)      #布尔值  (True/Flase)  bool
# print(())        #元组   tuple
# print([])        #数组   list
# print({})        #字典  dict
# # None Type        #None
# """
# 锄禾热当午       #多行注释  可选中"Ctrl+/"多行注释"
# 汗滴禾下午

# """

# print("哈哈",233,2.33)
# print("哈哈"+"嘻嘻")     #字符串的拼接
# print("哈哈"*10)         #字符串的重复叠加
# print(((1+2)*100-99)/2)  #数值的运算，整数和小数可在一起进行运算
# print(2<3)               #布尔值的判断

# 变量  给某个值取的名字
# 赋值  把一个具体的值交给这个变量
# a = "张三"   #把张三这个值给了名字叫做a的这个变量，变量的名字用小写字母。


# a = input("请输入：")     #input输入的是默认字符串
# b = input("请输入：")   
# print("input获取的内容 :", a+b)  #输出的是字符串的叠加

# type()显示出数据类型
# print(type("哈哈"))
# print(type(2333))
# print(type(2.33))
# print(type(()))
# print(type([]))
# print(type({}))

# 数据类型的转换
# a = float(input("请输入：")) 
# b = float(input("请输入："))  
# print("input获取的内容 :", a+b)


a = input("请输入 ：")
b = input("请输入 : ")
print("输出两段代码长度和 ：",len(a)+len(b))


# 元组  ,下标从零开始编号，不会重复
# a = (1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False)
# a = (1,2,3,4,5,6,7,8,9,10)
# print(a[5])
# print(a.index("哈哈"))  #只用于一维元组，查询元素的索引下标
# print(a.count("哈哈"))  #只用于一维元组，统计计数

# 切片
# print(a[:4])         #左闭右开，一定是取到开头begin的值，结尾end的值若有则取不到，若没有指定则可以取到end的值。
# print(a[4:9])
# print(a[9:])
# print(a[-5:-3])      #按负索引取值
# print(a[: :2])       #取元组所有项，步长为2
# print(a[: : -1])     #取元组的逆序
# print(a[4:])
# print(a[-1:0:-1])    #从负索引-1取到开头第一个的元素
# print(a[-3: -5:-1])   #逆序取元组中负索引-1到-3的元素


# 二维元组
# b = (a,"哈哈","嘻嘻")
# print(b[0][2])        #从b元组中的a元组取索引为2的值

# a = [1,2,3,4,"哈哈","嘻嘻",True,False]
# print(a[4])
# a.append("append1")  
# a.append("append2") 
# print(a)              #往数组追加数据，新增的在最后
# a.insert(3,"insert")  #往数组指定的下标加数据
# print(a)   
# #元组一旦写好后不可以修改，而数组是可以修改的。

# b =  a.pop(0)   #剪切，把数据拿出来放到别的地方去用
# c =  a.pop(0) 
# print(b+c)
# a.clear()      #清除数据
# xx=["你好","不好"]   #合并数组
# #a.extend(xx)
# print(a+xx)

# print(a)
# b = a.remove("哈哈")  #移除数据
# print(a)

# True = 1 ,False = 0
# 下标不要超出范围 = 越界

# 所有的方法都是用小括号结尾，比如，print(),int(),len();
# 元组、数组、字典的取值都是用中括号结尾，比如a[0];



# 字典的特点；
# 1.字典的值没有顺序
# 2.字典的结构必须是键值对格式。(键) Key: Value(值)。
# 3.字典{}，元组(),数组[]。
# 4.字典的键是不能改变的。只能改变键对应的值。

# a = {"name" : "张三","age":25,"地址":666}
# print(a["name"])                      #取值（从key里直接取值）


# a["high"] = "183cm"                   #新增
# print(a)


# a["name"] = "李四"                    #修改
# print(a)

# print("-----------------------")
# print(a.get("name"))                  #取值，取出后字典里仍然有这个值
# print(a)
# print(a.pop("name"))                  #剪切,从字典里取出值，取出之后字典里不存在这个值了
# print(a)

# print(a)
# a.update(laotie= 666)                 #更新数值
# print(a)

#  从Key直接取值如果取不存在的Key则会报错，Get取不存在的Key则会显示“None”。
# a = {"name" : "张三","age":25,"地址":666}
# print(a)

# print(a.get("py"))

# 数组和字典的的删除
# a = {"name" : "张三","age":25,"地址":666}
# del a["name"]
# print(a)

# a = [1,2,3,4,"哈哈","嘻嘻",True,False]
# del a[0]
# print(a)

# 练习：获取用户输入的个人信息，并且存储到字典中。个人信息包括name、age、sex。
# a = input("请输入姓名 ：")
# b = input("请输入年龄 ：")
# c = input("请输入性别 ：")
# d = {"姓名" :a,"年龄" :b,"性别":c}
# print(d)




