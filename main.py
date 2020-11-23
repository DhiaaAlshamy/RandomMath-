"""
ass5.py
CIS605
"""

from math import sqrt,atan,degrees,factorial

def ex0():
    """
   Just an  example code
   
    """
    i = int(input("Enter a non-negative integer: "))
    if i<0:
        print("Negative numbers do not have real square roots")
    else:
        root = sqrt(i)
        print("The square root is", round(root, 2))
def isPositive(number) :
    return number>0
    

def ex1() :
    
    
    """
    exercise 1
    """
    print("Input the height and the width of the triangle :")
    height = float(input("height: "))
    width = float(input("width: "))
    if not isPositive(height) or not isPositive(width) :
        print("Please enter a positive integers")
        return
    length = sqrt(height**2 + width**2)
    print("The length of the hypotenuse is", length )
    ang1Rad=atan(height/width)
    ang1Deg=degrees(ang1Rad)
    ang2Deg=90-ang1Deg
    print("The First Interior Angle is :", ang1Deg ,"degrees" )
    print("The Second Interior Angle is :", ang2Deg ,"degrees" )



def ex2() :
    """
    exercise 2
    """
    n = int(input("Enter n "))

    # first two terms
    n1, n2 = 0, 1
    count = 0
    if not isPositive(n):
       print("Please enter a positive integer")
    else:
       print(" Fibonacci series for ",n,":")
       series=[]
       while count < n:
           series.append(n1)
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1
           n2 = nth
       print(*series, sep=",")
   
def getBionomial(x,y):
  product=x
  rang=range(x-y+1,x)
  for num in rang:
    product=product*num
  return (product/factorial(y))
def ex3() :

  """
  exercise 3
  """
  print("Plesse enter the value of x and y")
  x=int(input("X = "))
  y=int(input("y = "))
  binomial=0
  if(not isPositive(x) or not isPositive(y)):
    print("please provide a positive numbers for both x and y")
    return
  if(y<x):
    binomial=getBionomial(x,y)
  elif(y==1):
    binomial=x
  elif(y==x):
    binomial=1
  #y>x
  else:
    binomial=0
  print('binomial coefficient of ', x ,' and ' , y , 'is : ',binomial )



def find_longest_And_Shorest_word(word_list):
    longest_word = ' '
    shortest_word = ''
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
        if len(word)<len(shortest_word) or shortest_word=='':
            shortest_word = word
    return [longest_word,shortest_word]
def ex4() :
    """
    exercise 4
    """
    str = input("Please Enter a line of text")
    splitStr=str.split()
    for word in splitStr:
        print(word)
    longest=find_longest_And_Shorest_word(splitStr)[0]
    shortest=find_longest_And_Shorest_word(splitStr)[1]
    print('Longest Word =',longest," length = ",len(longest))
    print('Shortest Word =',shortest," length = ",len(shortest))


def ex5() :
    """
    exercise 5
    """
    Text=input("Type a line of text: ")
    vowels="AEIOU"
    occ={}
    for i in range(len(Text)):
        ch=Text[i].upper()
        if(ch in vowels):
            if(ch in occ):
                occ[ch]=occ[ch]+1
            else:
                occ[ch]=1
    if(len(occ)==0):
        print('no vowels occurance found')
    else:
        print('least-frequently-occurring vowel(s) in the line :')
        for le in occ:
            if(min(occ.values())==occ[le]):
                print("vowel ",  le , "number of occurance =" , occ[le])

 
# modify the following line so that your name is displayed instead of KHALID
print("CIS 605 assignment - Samar Mohammed Aljehni")

# do not modify anything beneath this line
exlist = [None, ex1, ex2, ex3, ex4, ex5,ex0]
running = True
while running :
    line = input("\nSelect exercise (1-5) (0 to quit): ")
    if line == "0" : running = False
    elif len(line)==1 and "1"<=line<="5": exlist[int(line)]()
    else : print("Invalid input - try again")
    


