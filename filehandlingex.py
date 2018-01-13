data = open('C:\Users\hp\Desktop\Java Session-1.txt','r') #r -read

#print(data.read())

#print(data.readline())

a = data.readlines()

#print(a)
c = 0
for line in a:
    print(line)

    c  =c+1

print('row count =',c)
           





