#1
# A simple Python function to check
# whether x is even or odd
 
 
#def evenOdd(x):
    #if (x % 2 == 0):
      #  print("even")
   # else:
      #  print("odd")
 
 
# Driver code to call the function
#evenOdd(18)
#evenOdd(13)


#2
#def square_value(num):
   # """This function returns the square
   # value of the entered number"""
   # return num**2
 
 
#print(square_value(2))
#print(square_value(-4))

#3
# Python program to
# demonstrate accessing of
# variables of nested functions
 
def f1():
    s = 'I love GeeksforGeeks'
     
    def f2():
       print(s)
         
    f2()
 
# Driver's code
f1()