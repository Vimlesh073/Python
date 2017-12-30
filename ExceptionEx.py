
try:
    
    n = input('enter data ')
    d = input('enter data ')
except ValueError:
    print('error : ',ValueError)    
except NameError:
    print('error : ',NameError)
except TypeError:
    print('error : ',TypeError)
except :
    print('error : ')

    
try:

    a = [11,2,3]

    #nested try
    try:
        
        for i in range(0,10):
            print(a[i])
            
    except:
        print('error in range ')
        
    o  = n/d
    print(o)
   
except:
    print('invalid input')
    
print("thank you!!!")

      
