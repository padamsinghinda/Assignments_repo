f = open("file_handlind_demo.txt",'r')

##print("Function1 : %s " % f.read())
##f.seek(0)
##
##print("Function2 : %s " % f.readlines())
##f.seek(0)
##
##print("Funciton3 - line1 : %s" % f.readline())
##print("Funciton3 - line2 : %s" % f.readline())

print(" Finding distict user ID's ")
print(" ------------------------- ")
f.seek(0)
my_set = set()
my_dict_product = dict()
my_dict_user = dict()
for item in f.readlines()[1:]:
    ##print("Items are : %s" % item)
    item_tmp = item.split(',')
    my_set.add(item_tmp[0])

print("Distict user ID's are : %s " % my_set)
    
print(my_dict)    
