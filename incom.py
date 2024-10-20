incom = float(input("pless enter the incom:"))
if (incom >0) and (incom<12000000):
    the_salary =incom -(incom*0.03)
    
if (incom >=12000000) and (incom <18000000):
    the_left_over =incom - (incom*0.05)  
    the_salary =the_left_over -(the_left_over*0.07)


if (incom >=18000000) and (incom <25000000):
    the_left_over =incom - (incom*0.1)  
    the_salary =the_left_over -(the_left_over*0.1) 
    

if (incom >=25000000) and (incom <50000000):
    the_left_over =incom - (incom*0.18)  
    the_salary =the_left_over -(the_left_over*0.11)   
    
 
if (incom >=50000000) and (incom <75000000):
    the_left_over =incom - (incom*0.28)  
    the_salary =the_left_over -(the_left_over*0.15)       


if incom >75000000:
    the_left_over =incom - (incom*0.50)  
    the_salary =the_left_over -(the_left_over*0.20)    
print(the_salary)    
    
    