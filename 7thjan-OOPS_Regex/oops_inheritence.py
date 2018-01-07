'''
class compute:

    def getInput(self):
        print(self)
        self.id = input('enter sid :')
        self.name = input('enter name:')
        self.hs = input('enter hs:')
        self.es = input('enter es:')
        self.ms = input('enter ms:')
        self.cs = input('enter cs:')
        
    def calc(s):
        print(s)        
        s.total = s.hs+s.es+s.cs+s.ms
        s.avg = s.total/4
        s.grade = ''
        if s.avg>70:
            s.grade='A'
        elif s.avg>60:
            s.grade='B'
        elif s.avg>50:
            s.grade ='C'
        else:
            s.grade ='D'

    def printGrade(this):
        print(this)
        print('Id:',this.id)
        print('Name:',this.name)
        print('Total score :',this.total)
        print('Pect.:',this.avg)
        print('Grade :',this.grade)


        
o = compute()  ##xoddd001
o.getInput()  ##xoddd001
o.calc()  ##xoddd001
o.printGrade() ##xoddd001
'''

#parent class/base class
class calca:
    def add(s,a,b):
        c = a+b
        return c

    def sub(s,a,b):
        c = a-b
        print(c)

        
#child class or derived class 
class calcb(calca):
    
    def sub(s,a,b,c):
        d =a+b+c
        print(d)
        
    def mul(s,a,b):
        c = a*b
        print ('mul = ',c)
    def div(s,a,b):
        o = a/b
        print(o)


class calcc(calca):  #(calca,calcb): -- multiple inheritence 
    def concat(s,fn,ln):
        c = fn+' '+ln
        print ('your name is  = ',c)
    


'''
o = calca()
d = o.add(22,33)
print(d)
o.sub(22,33)
'''

o = calca()
o.sub(22,3)

ob = calcb()
ob.add(11,2)
ob.sub(33,3,1)
ob.mul(22,3)
ob.div(22,3)






        





        



    


        
        
        
