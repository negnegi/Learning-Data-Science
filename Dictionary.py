dict_name = {"Name":"john","age":30,"city":"newyork"}
print (dict_name)
value= dict_name["Name"]
print(value)

dict_name["age"]=27
print(dict_name)
dict_name["major"]="math"
print(dict_name)
del dict_name["major"]
print(dict_name)
list_keys = list(dict_name.keys())
print(list_keys)
values_list = list(dict_name.values())
print(values_list)
list_items = list(dict_name.items())
print(list_items)
#SET
set_name=set()
set_name.add("mango")
print(set_name)