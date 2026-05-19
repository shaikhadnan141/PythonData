#Access a list
lst = [1,2,3,4,5]
print (lst [0]) 

#Update list
lst = [1,2,3,4,5]
print (f'Before list {lst}')
lst [0]= 'hello'
print (f'After list {lst}')

#Using Slicing
lst = [1,2,3,4,5,6]
lst [0:3] = 10,20,30
print (lst)
