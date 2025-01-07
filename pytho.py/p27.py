#print all colors from color list 1 not contained in color list 2 create color list given as user input . use list comprehension
list1=[i for i in input("ENTER THE COLORS IN LIST 1:").split()]
list2=[i for i in input("ENTER THE COLORS IN LIST 2:").split()]
result=[i for i in list1 if i not in list2]
print("colors in list 1 but not in list 2", result)
