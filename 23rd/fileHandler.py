data = open(r'C:\Users\vkumar15\Desktop\Python IO.txt','r')

#print(data.read()) : read alll lines

#print(data.readline()) # read first line

#print(data.readlines()) # read and stoer to list

#l = data.readlines()
# show count of line
i = 0

#for r in l:
for r in data.readlines():
         col  = r.split(':')
         
         print(col[0])
         i=i+1

print(i)

         






