# write a factorial function, given n, you return n!


def factorial():
    total = 1
    n = int(input('give me a number '))
    
   
    while n > 1:
        total = total*n
        n = n-1
    print("The factorial is "+str(total))


    

factorial()