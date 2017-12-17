def calSal(bsal):
    hra = bsal*.50
    other = bsal
    ta = 2000

    pm = bsal+hra+other+ta
    pa  = pm*12

    tax = 0
    #tax
    if pa<=300000:
        tax = 0
    elif pa<=500000:
        tax = (pa-300000)*.05
    elif pa<=1000000:
        tax = 10000+(pa-500000)*.20
    else:
        tax = 110000+(pa-1000000)*.30

    print('Total Salary per month :',pm)
    print('Total Salary per year:',pa)
    print('Tax amount :',tax)



    

        
    

    
