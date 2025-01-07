#DATE-22.10.2024
#Q.17 sort a dictionary by keys in ascending and descending order
d={"mango":20,"apple":30,"kiwi":10,"grapes":5}
print("original dictionary",d)
aresult=dict(sorted(d.items()))
print("dictionary in ascending order",aresult)
bresult=dict(sorted(d.items(),reverse=True))
print("dictionary in descending order",bresult)
