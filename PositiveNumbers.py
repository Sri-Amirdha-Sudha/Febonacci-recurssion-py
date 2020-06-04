def positive_elements(a):#gets a list of integers
    s=len(a)#find the length of the list
    for i in range(s):
        if a[i]>=0:
            print(a[i],end=",")

array=[]
flag=True
while flag:
    element=input("Enter a number or hyphen to terminate list: ")#get list values in run-time
    if element =="-":
        flag=False
        break
    else:
        array.append(int(element))#gets values in array
print("The positive numbers in the list is/are:\n")
positive_elements(array)#Function call
    
