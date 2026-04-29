# Sample List

L = ["Michael Jackson", 10.1,1982,"MJ",1]
print(L)
# Print the elements on each index

print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-5]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-4]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[3],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[4],
'\n Negative:' , L[-1]  )

print(L[3:5])
# Use extend to add elements to list

L1 = [ "Michael Jackson", 10.2]
L1.extend(['pop', 10])
print(L1)

# Use append to add elements to list

L2 = [ "Michael Jackson", 10.2]
L2.append(['pop', 10])
print(L2)