from collections import defaultdict

f = open("D:\\ACADGILD\\git_clone\\Class_assignments\\file_handlind_demo.txt",'r')

temp_dict = defaultdict(list)

#create a dictionary having tuple (id,name) as key and list (product : count) as value
for item in f.readlines()[1:]:
    item_tmp = item.strip().split(',')
    if ((item_tmp[0],item_tmp[1])) not in temp_dict.keys():        
        temp_dict[(item_tmp[0],item_tmp[1])].append(list())
    
    temp_dict[(item_tmp[0],item_tmp[1])].append(item_tmp[2])
    #print(temp_dict)


for key in temp_dict.keys():
    my_list = []
    for value in temp_dict[key]:
        if value != [] :
            my_list.append(value)
    ##print(my_list)
        
    d = dict()
    for item in my_list :
        if item not in d.keys():
            d[item] = 1
        else :
            d[item] += 1
    temp_dict[key] = d     
    ##print(d)

#print unique id,name
print("Uniqur ID")
for item in temp_dict.keys():
    print(item[0])

#Distinct product for each user and total purchase
for item in temp_dict.keys():
    sum = 0
    print("Distict products for user %s is : %s" % (item , temp_dict[item].keys()))
    for product in temp_dict[item].keys():
        sum += temp_dict[item][product]
    print("Total products purchased by user %s is : %s" %(item, sum))


# Quantity of each product purchased
dict_prod_summary = dict()
for item in temp_dict.values():
    ##print(item)
    for prod in item.keys() :
        ##print(prod)
        if prod not in dict_prod_summary.keys():
            dict_prod_summary[prod] = item[prod]
        else :
            dict_prod_summary[prod] += item[prod]

print(dict_prod_summary)
