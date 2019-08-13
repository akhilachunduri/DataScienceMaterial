
# coding: utf-8

# In[ ]:


#Program to input a number from the user and check if it is positive, negative or zero

try:
    a=int(input("Enter the number : "))
    if a==0:
        print("The number is zero.")
    elif a>0:
        print("The number is a positive number.")
    else:
        print("The number is a negative number.")
except ValueError:
    print("Enter a valid number!")
    

    


# In[ ]:


#Program to Check if a Number is Odd or Even by taking user input
try:
    a=int(input("Enter the number : "))
    if (a%2)==0:
        print("The number is an even number.")    
    else:
        print("The number is an odd number.")
except ValueError:
    print("Enter a valid number!")


# In[ ]:


#Program to input a year with century and check if it is Leap Year 
#or print invalid if it is not in the form of year with century
try:
    a=int(input("Enter the Year : "))
    if (a%100)==0:
        if(a%400)==0:            
            print("The Year is a leap year.")  
        else:
            print("The year is not a leap year.")
    else:
        print("The year is not a century.")
except ValueError:
    print("Enter a valid year!")


# In[10]:


#Program to Find the Largest Among Three Numbers, using the least number of lines of code
try:
    a=float(input("Enter the first number : "))
    b=float(input("Enter the second number : "))
    c=float(input("Enter the third number : "))
    if (a>=b) and (a>=c):
        print("The largest number is :{0}".format(a))
    elif (b>=a) and (b>=c):
        print("The largest number is :",b)
    else:
        print("The largest number is :",c)
except ValueError:
    print("Enter a valid number!")


# In[24]:


#Program to input a month name and print number of days in it
import calendar
try:
    year=int(input("Enter the year : "))
    month=int(input("Enter the month: "))    
    print("The number of days in the {0} month of the year {1} is: {2}".format(calendar.month_name[month],year,monthrange(year,month)[1]))  
except ValueError:
    print("Enter a valid number!")


# In[2]:


#Program to Check if a number is Prime Number or not
try:
    a=int(input("Enter the first number : "))
   # b=int(input("Enter the second number : "))
    if a>1:
        for i in range(2,a):
            if (a%i==0):
                print("{0} is not a prime number".format(a))
                break
        else:
            print("{0} is a prime number".format(a)) 
    else:
        print("{0} is not a prime number".format(a))
except ValueError:
    print("Enter a valid number!")


# In[5]:


#Program to Check if a number is Prime Number or not with a range as user input
try:
    a=int(input("Enter the first number : "))
    b=int(input("Enter the second number : "))
    print("Prime numbers between {0} and {1} are : ".format(a,b))
    for j in range(a,b + 1):
        if j>1:
            for i in range(2,j):
                if (j%i==0):               
                    break
            else:
                print("{0}".format(j)) 
    
except ValueError:
    print("Enter a valid number!")


# In[11]:


#Program to Find the Factorial of a Number
try:
    a=int(input("Enter the number : "))
    fact=1
    if a==0:
        print("The factorial of {0} is 1".format(a))
    elif a<0:
        print("The factorial of {0} cannot be calculated".format(a))
    else:
        for i in range(1,a+1):
            fact=fact*i
        print("The factorial of {0} is {1}".format(a,fact))
except ValueError:
    print("Enter a valid number!")


# In[13]:


#Program to Display the multiplication Table by taking the number as input
try:
    a=int(input("Enter the number : "))
    for i in range(1,11):
        print("{0} x {1} = {2} ".format(a,i,a*i))
except ValueError:
    print("Enter a valid number!")


# In[7]:


#Program to Print the Fibonacci sequence
x,y=0,1
try:
    a=int(input("Enter the nth term : "))
    if a<0:
        print("Please enter a positive integer.")
    else:        
        print(0)
        while y < a:        
            print(y)
            x,y=y,x+y
except ValueError:
    print("Enter a valid number!")


# In[10]:


#Program to Find the Sum of Natural Numbers
try:
    a=int(input("Enter the number : "))
    if a<0:
        print("Please enter a positive integer.")
    else:
        sum=0
        while(a>0):
            sum=sum+a
            a=a-1
        print("The sum is ",sum)
except ValueError:
    print("Enter a valid number!")

