#list/array   : collection of data or values
# - multiple values can be stored on single variable
#################################################
#there are following type of array/list : i. single list/array  or linear array
a = [11,2225555,333,4444,1,2]  # index will start from 0 index 
 
print(a)

#print by index
print(a[2]) # 3rd element 

#print all numbers/element one by one / by index
for i in range(3,-1,-1):
    print(a[i])

for d in a:     # python does traverse element automatically one by one / for each (forward only)
    print(d)
    
#Example 1: get sum of all elements
su = 0

for d in a:     # python does traverse element automatically one by one / for each (forward only)
    su = su+d

print('sum of all elements : ',su)


#Example 2: show max/highest value
h = 0
for d in a:     # python does traverse element automatically one by one / for each (forward only)
    if h<d:
        h =d

print('highest value :',h)

# take input from and fill to array
mark = []
s = input('enter size for array : ')
for i in range(0,s):
    m = input(' enter score :')
    mark.append(m)


print(mark)

##########################################################
# - ii. multiple dimenssion or tabular or 2 D 
###########################################################
print('---------------------------------------------------------------')

s=[[22,33,44] ,[55,66,77], [77,88,99] ] # 3 * 3

print(s)
#print 2 row
print(s[1])

#print 3rd row and 2nd element
print(s[2][1])

#read row by row 
for row in s:
    print(row)

#read every element 
for row in s:  # table to row 
    for col in row: # row to col 
        print(col)



#read every element 
for row in s:  # table to row
    s= ''
    for col in row: # row to col 
        s = s+ str(col) +'\t'
        

    print(s)

#dynmaic fill data to the 2D array
rs = input('enter row size :')
cs = input('enter col size :')
data = []

for ri in range(0,rs):  # table to row
    row = []    
    for ci in range(0,cs):
        d = input('enter data :')
        row.append(d)
    data.append(row)
        

print(data)

#################################################
#touple
#################################################
day =('mon','tue','wed')
print(day)
print(day[1])

y1 =(111,222,3333)
y2 =(11,22,32)

print(y1+y2)

for i in range(1,1):
    d =input('ente day ')
    if d in day:
        print('can be applied')
    else :
        print('not in given list')

#dictionary
# key = value

emp = {'105':'aman',  '202':'divya','303':'ayush'}
print(emp['202'])

n = input('enter id which u want to search :')
print(emp[n])









      





       












