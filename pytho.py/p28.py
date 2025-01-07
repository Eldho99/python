#create 2 lists of colors list 1 with colors [red blue green yellow purple] and list 2 with colors [blue yellow pink] use a set to find colors in list 1 that are not in list 2
list1=["red","blue","green","yellow","purple"]
list2=["blue","yellow","pink"]
result=set(list1)-set(list2)
print("color in list 1 not in list 2 as set",result)
print("as list",list(result))
