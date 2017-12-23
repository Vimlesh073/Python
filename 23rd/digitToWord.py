d={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thriteen',14:'forteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninty'}

def convertTODigit(n):
         if n<21:
                  print(oneD(n))
         elif n<100:         
                  print(twoD(n))
         elif n<1000:
                  print(threeD(n))
         
         
def oneD(num):         
         return d[num]

def twoD(n):
         n1 = int(n/10) # 9
         n2 = n %10     # 0
                  
         if n2>0:
                  return d[n1*10]+ ' '+d[n2]
         else:
                  return d[n1*10]                  
def threeD(n):
         n1 = int(n/100)
         n2 = n%100
         
         
         s = d[n1]+' hundred'
         
         if n2>0 and n2< 21:
                      s = s+' '+oneD(n2)
         elif n2>20 and n2 < 100:
                     s = s+' '+twoD(n2)                
                  
         return s

def fourD(n):
         n1 = int(n/1000)
         
         n2 = n%1000
         s = d[n1]+' thousand'
         
         if n2>0 and n2< 21:
                      s = s+' '+oneD(n2)
         elif n2>20 and n2 < 100:
                     s = s+' '+twoD(n2)
         elif n2>99 and n2<1000:
                  s = s+' ' +threeD(n)
                  
                  
         return s

       


         
         
         
         

         
         
         











