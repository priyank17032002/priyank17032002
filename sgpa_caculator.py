'''
Created on 12-May-2022

@author: Lucifer
'''
print("enter your grades in space separated manner ")
print("ex.  a+ a a b+ b ")
arr=[i for i in input().split()]
print("enter the credits of subject respectively ")
credit=[float(i) for i in input().split()]
sgpa=0
for i in range(len(arr)):
    if arr[i]=='A+' or arr[i]=='a+':
        point=10
        sgpa+=point*credit[i]
        
    elif arr[i]=='A' or arr[i]=='a' :
        point=9
        sgpa+=point*credit[i]
    
    elif arr[i]=='B+' or arr[i]=='b+':
        point=8
        sgpa+=point*credit[i]
        
    elif arr[i]=='B' or arr[i]=='b':
        point=7
        sgpa+=point*credit[i]
        
    elif arr[i]=='C+' or arr[i]=='c+':
        point=6
        sgpa+=point*credit[i]
        
    elif arr[i]=='C' or arr[i]=='c':
        point=5
        sgpa+=point*credit[i]
        
    elif arr[i]=='D' or arr[i]=='d':
        point=4
        sgpa+=point*credit[i]

    else:
        print("you not able to clear a one of your subject ")
        print("or else you enter wrong entries please check your entries once again ")
        break  
sgpa=sgpa/sum(credit)
print("your sgpa is ",sgpa)    