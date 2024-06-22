'''
dict = {}
subject1 = input("enter subject1")
marks1 = input("enter first subject marks")
subject2 = input("enter subject2 ")
marks2 = input("enter second subject marks")
subject3 = input("enter subject3 ")
marks3 = input("enter third subject marks")
dict[subject1] = marks1
dict[subject2] = marks2
dict[subject3] = marks3
print ("the subject and marks are",dict) '''
'''
set={int(9.0),float(9)}
print(set)
set={9.0 , "9"}
print(set)
set={("int",9) , ("float", 9.0)}
print(set)
'''

#lec5
'''
i=100
while i>=1 :
    print(i)
    i-=1

n=int(input("enter the table to be written"))
i=1
while i<=10 :
    print (n ,"*",i , "=" , n*i )    
    i+=1
   

list=[1,4,9,16,25,36,49,64,81,100]
i=0
length=len(list)  
while i<= length-1 :
    print (list[i])
    i+=1
    
tuple=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter the no. to be searched"))
i=0
while i < len(tuple) :
        r=tuple[i]
        if r==x :
            print("element found")
        else :
            print("element not found")    
        i+=1 

        
tuple=(1,4,9,16,25,36,49,64,81,100)
for ch in tuple:
    print(ch)
        
x=int(input("enter the no "))        
tuple=(1,4,9,16,25,36,49,64,81,100)
for ch in tuple :
    if ch == x:
        print (x, "found")
        break
    else :
        print("finding")
        '''

n=4
mul=1
for i in range(1,n+1):
    mul*=i
print(mul)            
