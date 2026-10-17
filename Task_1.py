def factorial(n):
    fact=1 #Taking an initial  fact=1 to update its value  
    if n==0:#Considering the fact that the input can be 0
        return 1;
    elif n==1:#Considering the fact that the input can be 1
        return 1;
    while n>1:#Using the condition that the input number is always greater than 0
        fact=fact*n#Using the  recursions here to update the value of fact
        n=n-1#Updating the value of n 
    return fact#returning the final value of fact 



