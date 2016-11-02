#-*- coding:utf-8 -*-
#实现一个简单的购物车程序，给出一定的预算，在预算内购买商品
goods = [ 
    ['苹果手机',6300],
    ['苹果电脑',15800],
    ['平板',3200],
    ['小米mix',3499],
    ['小米note2',2799],
    ['大衣',1599],
    ['vr',3999],
    ['奥迪',488999]
]
salary = 30000
shop_list = []
while True:
    for index,g in enumerate(goods):
        #choice = input("你要购买的商品:").strip() 这里使用strip（）会有问题，修改如下
        choice = raw_input("你要购买的商品:")
        if choice.isdigit():
            choice = int(choice)
            print(goods[choice][0])
            goods_price = goods[choice][1]
            if goods_price <= salary:
                shop_list.append(goods[choice])
                salary -= goods_price
                print("你购买的商品是 %s,你的余额还剩 %s" %(goods[choice][0],salary))
            else:
                print("你的余额不足")
                

