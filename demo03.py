# """
# class  声明类的名字
# 类的名字的首字母必须大写
# 默认属性方法  __init__
# 使用__init__来接受参数
# 每个类里面的方法，第一个参数必须是self
# 类里面所有的方法，都必须要传一个参数，叫做self，指的是定义的类本身
# """
# # class GirlFriend():
# #     """
# #     女朋友

# #     """
# #     def __init__(self) :       #类的属性。（定义类的属性的时候一定是两个下划线)
# #         self.sex = "女"
# #         self.high = "170cm"
# #         self.weight = "55kg"
# #         self.hair = "大波浪"
# #         self.age = "18岁"

# #     def caiyi(self,num) :  
# #         """
# #         才艺表演
# #         """
# #         print("你性别为"+self.sex+"身高为"+self.high+"体重为"+self.weight+"发型为"+self.hair+"年龄为"+self.age+"的女朋友开始了才艺表演之：")
# #         if num == 1 :
# #             print("胸口碎大石")
# #         elif num == 2 :
# #             print("唱跳RAP篮球")
# #         else :
# #             print("单手开瓶盖")
    
# #     def chuyi(self) :    
# #         """ 厨艺持家 """
# #         print("你性别为"+self.sex+"身高为"+self.high+"体重为"+self.weight+"发型为"+self.hair+"年龄为"+self.age+"的女朋友开始了厨艺表演之：")
# #         print("精通八大菜系")

# #     def work(self) :    
# #         """ 工作挣钱 """
# #         print("你性别为"+self.sex+"身高为"+self.high+"体重为"+self.weight+"发型为"+self.hair+"年龄为"+self.age+"的女朋友开始了工作之：")
# #         print("开挖掘机！")


# #先类的实例,再调用方法
# # zhangsan =  GirlFriend()
# # zhangsan.caiyi(2) 
# # zhangsan.chuyi()
# # print(zhangsan.high)

# #改类的参数
# class GirlFriend():
#     """
#     女朋友

#     """
#     def __init__(self,sex,high,weigh,hair,age) :       #类的属性。（定义类的属性的时候一定是两个下划线)
#         self.sex = sex
#         self.high = high
#         self.weight = weigh
#         self.hair = hair
#         self.age = age

#     def caiyi(self,num) :  
#         """
#         才艺表演
#         """
#         print("你性别为"+self.sex+"身高为"+self.high+"体重为"+self.weight+"发型为"+self.hair+"年龄为"+self.age+"的女朋友开始了才艺表演之：")
#         if num == 1 :
#             print("胸口碎大石")
#         elif num == 2 :
#             print("唱跳RAP篮球")
#         else :
#             print("单手开瓶盖")
    
#     def chuyi(self) :    
#         """ 厨艺持家 """
#         print("你性别为"+self.sex+"身高为"+self.high+"体重为"+self.weight+"发型为"+self.hair+"年龄为"+self.age+"的女朋友开始了厨艺表演之：")
#         print("精通八大菜系")

#     def work(self) :    
#         """ 工作挣钱 """
#         print("你性别为"+self.sex+"身高为"+self.high+"体重为"+self.weight+"发型为"+self.hair+"年龄为"+self.age+"的女朋友开始了工作之：")
#         print("开挖掘机！")

# # zhangsan =  GirlFriend("女","165cm","45kg","红头发","25岁")
# # zhangsan.caiyi(2) 
# # zhangsan.chuyi()
# # print(zhangsan.high)

# # class Car():
# #     def __init__(self,pinpai,yanse,neishi,jilun):
# #         self.pinpai = pinpai
# #         self.yanse = yanse
# #         self.neishi = neishi
# #         self.jilun = jilun

# #     def bianxing(self):
# #         print("车子变身为擎天柱！")

# #     def fly(self):
# #         print("芜湖！起飞！")

# # laotie = Car("奔驰","蓝色","豪华","八轮")
# # laotie.bianxing()
# # print(laotie.yanse)


# #类的继承和重写
# #GirlFriend ：父类
# #Nvpengy  ： 子类，继承了父类的所有的属性

# class Nvpengy(GirlFriend) :           #类的重写，重新定义重写
#     def work(self) :
#         print("修电脑")
# zhangsan = Nvpengy("女","172cm","60kg","卷发","25岁")
# zhangsan.work()
# zhangsan .chuyi()

# a = {"name":"张三","age":18}
# print("年龄%d名字叫%s的开始了新的一天"%(a["age"],a["name"]))


