#x=int(input('enter first number:'))
#y=int(input('enter secpond number:'))
#z=int(input('enter third number:'))
#avg=(x+y+z)//3
#print('Average:',avg)
#x1=int(input('enter first number:'))
#y1=int(input('enter ssecond number;'))
#sum=x1+y1
#diff=int(x1-y1)
#pro=int(x1*y1)
#print('sum:',sum)
#print('difference',diff)
#print('product',pro)
#x=int(input('enter hours:'))
#min=(x*60)
#print('number of minutes:',min)

"""x=int(input('enter seconds:'))
hours=x//3600
hours_rem=x%3600
min=hours_rem//60
sec=hours_rem%60
print('Number of hours:',hours)
print('Number of minutes',min)
print('Number of seconds',sec)
x1=(input('Enter any string:'))
x2=(input('Enter another string:'))
print(f'legnth of string1=:',len(x1))
print(f'legnth of string2=:',len(x2))
print('sum of both strings:',len(x1)+len(x2))"""

#practice5----------------------------------------------------practice 5------------------------------
"""
x1=int(input('enter x1 = '))
x2=int(input('enter x2 = '))
y1=int(input('enter y1 = '))
y2=int(input('enter y2 = '))
x=(x2-x1)**2
y=(y2-y1)**2
d=(x+y)**0.5
print('distance= ',d)"""

#task2
"""
r=float(input('Enter the value of radius '))
v=4/3*(3.14)*(r)**3
print(v)"""
#task3
"""
vi=int(input('enter initial velocity '))
a=int(input('enter accelaration '))
t=int(input('enter time taken'))
vf=vi+a*t
print('vf = ',vf)
d=vi*t+(.5*a*t**2)
vf2=vi**2+(2*a*d)
print( 'vf2 = ',vf2)
print('d = ',d)
"""
#task4
"""
x=int(input('Enter x = '))
y=int( input('enter y = '))
a=3*((x**2)*y)
b=3*(x*(y**2))
z=(x**3)-(y**3)-a+b
print('(x-y)^3 = ',z)
"""
#practice 3---------------------------------------------practice 3---------------
"""
eng=int(input( 'enter english marks' ))
ur=int(input('enter urdu marks'))
ma=int(input('enter maths marks'))
isl=int(input('enter islamiyat marks'))
pak=int(input('enter pak std marks'))
phy=int(input('enter english marks'))
ch=int(input('enter chemistry marks'))
bio=int(input('enter biology marks'))
z=eng+ur+ma+isl+pak+phy+ch+bio
print('1.English\t\t75\t',eng)
print('2.Urdu\t\t\t75\t',ur)
print('3.maths\t\t\t75\t',ma)
print('4.islamiyat\t\t50\t',isl)
print('5.pak.std\t\t50\t',pak)
print('6.physics\t\t75\t',phy)
print('7.chemistry\t\t75\t',ch)
print('8.biology\t\t75\t',bio)
print(f'\tTOTAL\t\t525\t  {z}')
merit=int(input('enter last years merit'))
print('marks required in tenth :',merit-z)"""

#task 3
"""
n=int(input('Numerator:' ))
d=int(input('denominator:'))
v=n/d
print('Numerator:',n)
print('Denominator:',d)
print('value:',v)
"""
#task4
"""
mi=int(input('milk budget:'))
su=int(input('sugar budget:'))
t=int(input('tea budget:'))
bi=int(input('biscuit budget:'))
a=mi+0.2*mi
b=su+0.2*su
c=t+0.2*t
d=bi+0.2*bi
print('next month budget')
print('milk:\t',a)
print('sugar:\t',b)
print('tea:\t',c)
rint('biscuit: ',d)
print('Total\t',a+b+c+d)"""
#practice task 6---------------------------------------------practice 6------------------------------
#question 1
"""
import random
x= random.randint(1,5)
y=random.randint(1,5)
diff=x-y
print('first num',x)
print('second num',y)
if diff<=1:
    print('numbers are almost equal')
else:
    print('numbers are not equal')
"""
#question2
"""
import random
x= random.randint(1,5)
y=random.randint(1,5)
diff=x-y
print('first num',x)
print('second num',y)
if diff<=1:
    print('numbers are almost equal')
elif diff==0:
    print('numbers are exactly equal')
else:
    print('numbers are not equal')
    """
#question 3
"""
import random
marks=random.randint(0,100)
print('marks:\t',marks)
if marks>=85:
    print(f'grade:\tA')
elif marks>=80:
    print('grade:\tA-')
elif marks>=75:
    print('grade:\tB+')
elif marks>=70:
    print('grade:\tB')
elif marks>=65:
    print('grade:\tB-')
elif marks>=61:
    print('grade:\tC+')    
elif marks>=58:
    print('grade:\tC')
elif marks>=55:
    print('grade:\tC-')
elif marks>=50:
    print('grade:\tD')
elif marks<50:
    print('grade:\tF')
    """
#question4
"""
import math
x=int(input('enter required number of eggs : '))
req=math.ceil(x/6)
print('pack :\t',req)
x=int(input( "enter"))

req=x//6
if x%6!=0:
    req+=1
print(req)
"""
#question5
"""
len1=int(input('length of first rectangle :\t'))
wid1=int(input('width of first rectangle :\t'))
len2=int(input('length of second rectangle :\t'))
wid2=int(input('width of second rectangle :\t'))
area1=len1*wid1
area2=len2*wid2
if area1<area2:
    print('first rectangleis smaller')
elif area1==area2:
    print('both are equal')
else:
    print('second rectangle is smaller')
"""
"""
l=int(input('length: '))
w=int(input('width: '))
print(f'{l')
print(w)"""
"""
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

for i in range(length):
    for j in range(width):
        if i == 0 or i == length-1 or j == 0 or j == width-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    """

#practice task 7-----------------------------------practice 7--------------------------------
#question1
"""
import random
x1=random.randint(1,1000)
x2=random.randint(1,1000)
x3=random.randint(1,1000)
print('numbers before condition :', x1,x2,x3)

max=x1
min=x2
if max<x2:
    max=x2
elif max<x3:
    max=x3

if min>x1:
    min=x1
elif min>x3:
    min=x3

z=(x1+x2+x3)-min-max    
print('numbers after condition : ',min,z, max)
"""
"""
import random
x1=random.randint(1,1000)
x2=random.randint(1,1000)
x3=random.randint(1,1000)
print('numbers before condition :', x1,x2,x3)

if x1>x2:
    if x2>x3:
       larg=x1 
elif x3>x1 and x3>x2:
    larg=x3
elif x2>x1:
    if x1>x3:
        larg=x2
elif x3>x2 and x3>x1:
    larg=x3
elif x1>x3:
    if x3>x2:
        larg=x1
elif x2>x1 and x2>x3:
    larg=x2
elif x3>x1:
    if x1>x2:
        larg=x3
elif x2>x3 and x2>x1:
    larg=x2
    """
"""
if x1>x2 and x1>x3:
    larg=x1
    p=1
elif x2>x3 and x2>x1:
    larg=x2
    p=2
elif x3>x2 and x3>x1:
    larg=x3
    p=3
elif x1>x2 and x3>x1:
    larg=x3
    p=4
if x1<x2 and x1<x3:
    min=x1
    a=1
elif x2<x3 and x2<x1:
    min=x2
    a=2
elif x3<x2 and x3<x1:
    min=x3
    a=3
elif x1<x2 and x3<x1:
    min=x3
    a=4
    print(min,larg)
print(a,p)
    """
"""
if x1 <= x2 and x1 <= x3:
    if x2 <= x3:
        print(x1, x2, x3)
    else:
        print(x1, x3, x2)
elif x2 <= x3:
    print(x2, x3, x1)
else:
    print(x3, x2, x1)
    """
#question2******
"""
import random
x1=random.randint(1,1000)
x2=random.randint(1,1000)
x3=random.randint(1,1000)
print('numbers before condition :', x1,x2,x3)

max=x1
a=1
min=x2
b=2
if max<x2:
    max=x2
    a=2
elif max<x3:
    max=x3
    a=3
elif max<x4:
    max=x4
    a=4
if min>x1:
    min=x1
    b=1
elif min>x3:
    min=x3
    b=3
elif min>x4:
    min=x4
    b=4

z=(x1+x2+x3)-min-max    
print('numbers after condition : ',min,z, max)"""

#question 3*******
"""
import random
x1=random.randint(1,1000)
x2=random.randint(1,1000)
x3=random.randint(1,1000)
list=[x1,x2,x3]
print(list)
if sorted(list)==list:
    print('list is sorted')
elif sorted(list)!=list:
    print('list is not sorted')
"""
#question 4*****
"""

marks1=int(input('Marks 1 :'))
marks2=int(input('Marks 2 :'))

 
if marks1>=85:
   grade1=A
elif marks1>=80:
    grade1='A-'
elif marks1>=75:
    grade1='B+'
elif marks1>=70:
    grade1='B'
elif marks1>=65:
    grade1='B-'
elif marks1>=61:
    grade1='C+'    
elif marks1>=58:
    grade1='C'
elif marks1>=55:
    grade1='C-'
elif marks1>=50:
    grade1='D'
elif marks1<50:
    grade1='F'
    
if marks2>=85:
   grade2='A'
elif marks2>=80:
    grade2='A-'
elif marks2>=75:
    grade2='B+'
elif marks2>=70:
    grade2='B'
elif marks2>=65:
    grade2='B-'
elif marks2>=61:
    grade2='C+'    
elif marks2>=58:
    grade2='C'
elif marks2>=55:
    grade2='C-'
elif marks2>=50:
    grade2='D'
elif marks2<50:
    grade2='F'
if marks1==marks2:
    print('SAME')
elif grade1==grade2:
    print('ALMOST SAME')
elif grade1 !=grade2:
    print('DIFFERENT')
    """

#question 5******
#correct
"""
num = int(input("Enter a number: "))
divisible_by = []

if num % 2 == 0:
    divisible_by.append(2)
if num % 3 == 0:
    divisible_by.append(3)
if num % 5 == 0:
    divisible_by.append(5)
if num % 7 == 0:
    divisible_by.append(7)

if len(divisible_by) == 0:
    print(num, "is not divisible by 2, 3, 5, or 7")
elif len(divisible_by)==1:
    print(num, "is divisible by ", divisible_by," only")
elif len(divisible_by)==2:
    print(f'number is divisible by both {divisible_by[0]} and {divisible_by[1]}')    
elif len(divisible_by)==3:
    print(f'number is divisible by both {divisible_by[0]}, {divisible_by[1]} and {divisible_by[2]}')
    """
#method 2
"""
x=int(input('enter any number :'))
if x%2==0 and x%3==0 and x%5==0 and x%7==0:
    print('number is divisible by 2 ,3 and 5')
elif x%2==0 and x%3==0 and x%5==0:
    print('number is divisible by 2 and 3 and 5')
elif x%2==0 and x%3==0:    
    print('number is divisible by 2 and 3')
elif x%2==0 and x%7==0:
    print('number is divisible by 2 and 7 ')
elif x%2==0 and x%5==0:
    print('number is divisible by 2 and 5')
elif x%3==0 and x%5==0:
    print('number is divisible by 3 and 5')
elif x%3==0 and x%7==0:
    print('number is divisible by 3 and 7')
elif x%7==0 and x%5==0:
    print('number is divisible by 5 and 7')
elif x%2==0:
    print('number is divisible by 2 only')
elif x%3==0:
    print('number is divisible by 3 only')
elif x%5==0:
    print('number is divisible by 5 only')
elif x%7==0:
    print('number is divisible by 7 only')    
"""
#practice 8-----------------------------------------------------------------
#question1:
"""
x=input('enter character ')
x_asci=ord(x)
mask=1
for i in range (7,-1,-1):#start with 7 ends T -1 and have increment of -1
    if x_asci & (mask):
        print(f'Bit {8-i} is on')
    mask=mask<<1
    """
"""
x=input ('enter character')
asci_x=ord(x)
if asci_x & 1==1:
    print('bit 1 is on')
if  asci_x & 2==2:
    print('bit 2 is on')
if  asci_x & 4==4:
    print('bit 3 is on')
if  asci_x & 8==8:
    print('bit 4 is on')
if  asci_x & 16==16:
    print('bit 5 is on')
if  asci_x & 32==64:
    print('bit 6 is on')
if  asci_x & 64==64:
    print('bit 7 is on')"""
    
#QUESTION2:
"""
x=input('enter first charcater')
y=input('enter first charcater')
count=0
asci_x=ord(x)
asci_y=ord(y)
if asci_x & 1==asci_y &1:
    count+=1
if asci_x & 2 ==asci_y & 2:
    count=count+1
if asci_x& 4==asci_y & 4:
    count=count+1
if asci_x & 8==asci_y & 8:
     count=count+1
if asci_x & 16==asci_y & 16:
    count=count+1
if asci_x & 32==asci_y & 32:
   count=count+1
if asci_x & 64==asci_y & 64:
    count=count+1
print(count)
"""
#question 3 :
'''
char1=input('enter character ')
char2=input('enter character ')
def are_character_equal(char1,char2):
    
    mask1=ord(char1)
    mask2=ord(char1)
    diff=0
    for i in range(8):
        if (mask1 &(1<<i))!=(mask2 & (1<<i)):
            diff+=1
        if diff==0:
          return True
        else:
          return False
             
if are_character_equal (char1,char2):
    print('characters are equal')
else:
    print('charactrs are not equal')'''
#correct easy
"""
x=input('enter char ')
y=input('enter char ')
if ord(x)==ord(y):
    print('charecters  \'{x} \' and \'{y}\' are equal')
elif ord(x)!=ord(y):
    print('charcters  \'{x}\' and \'{y}\' are not equal')"""
#method 2
"""
x=input('enter char ')
y=input('enter char ')
if ord(x)-ord(y)==0:
      print(f'charecters \'{x} \' and \'{y}\' are equal')
else :
    print(f'characters \'{x}\' and \'{y}\' are not equal')
"""

#question4+++++++++
"""
x=input('enter charcter')
y= int(input('enter bit number'))
z=ord(x)
if z &( 1<<(y-1))==0:
    print(f'bit  at {y}is off')
else:
    print(f'bit at {y} is on')"""

#task 3
"""
char=input('ENTER CHARACTER')
def flip_first_six_bits(char):
    mask=ord(char)
    flipped_mask=mask^0b11111100
    return chr( flipped_mask)"""

#PRACTICE TASK 9-------------------------------------------PRACTICE 9---------
#task1++++++++++
"""
x=input('Enter a single character')
if len(x)!=1:
    print('character is not single')
if x=='D' or x=='H' or x=='h' or x=='d':
    print(" red " )
elif x=='s'or x=='S' or x=='c' or x=='C':
    print(" black")
"""
#task2+++++++++++++++++++
"""
import random
ranks=['ace','Two','three','four','five','six','seven','eight','nine','ten','jack','queen','king']
typs=['diamond','heart','spade','club']
rank=ranks[random.randint(0,12)]
typ=typs[random.randint(0,3)]
print(f'{rank} of {typ}')
"""
#METHOD 2+++
"""
import random
rank=random.randint(1,13)
suit=random.randint(1,4)
if rank==1:
    rank='Ace'
if rank==2:
    rank='Two'
if rank==3:
    rank='Three'
if rank==4:
    rank='Four'
if rank==5:
    rank='Five'
if rank==6:
    rank='Six'
if rank==7:
    rank='Seven'
if rank==8:
    rank='Eight'
if rank==9:
    rank='Nine'
if rank==10:
    rank='Ten'
    
elif rank==11:
    rank='Jack'
elif rank==12:
    rank='Queen'
elif rank==13:
    rank='King'
else :
    rank=str(rank)
    
if suit==1:
    suit='Diamond'
elif suit==2:
    suit='Heart'
elif suit==3:
    suit='Spade'
elif suit==4:
    suit='Club'
print(f'{rank} of {suit}')    
    
  """
#question 3+++++++++++++++++++++++++++++
"""
x=int(input('Enter three-digit-number'))
first=x//100
second=(x%100)//10
third=x%10
print(f'First Digit {first}\nSecond Digit {second}\nThird Digit {third}')
"""
#question 4++++++++++++++++++++++
"""
x=int(input('Enter three-digit-number'))
first=x//100
second=(x%100)//10
third=x%10
add=first+second+third
print(f'Sum of Digit : {add}')"""
#question 5+++++++++++++++++++++++
"""
x=int(input('Enter three-digit-number'))
first=x//100
second=(x%100)//10
third=x%10
print(f'Reverse number {third}{second}{first}')"""

#LAB 5--------------------LAB 5------------------LAB 5------------------LAB 5--
"""
import random
x=random.randint(20,99)
first=x//10
second=x%10
right=' '
left=' '
if first==2:
    left='twenty'
elif first==3:
    left='thirty'
elif first==4:
    left='fourty'
elif first==5:
    left='fifty'
elif first==6:
    left='sixty'
elif first==7:
    left='seventy'
elif first==8:
    left='eighty'
elif first==9:
    left='ninety'
if second==1:
    right='one'
elif second==2:
    right='two'
elif second==3:
    right='three'
elif second==4:
    right='four'
elif second==5:
    right='five'
elif second==6:
    right='six'
elif second==7:
    right='seven'
elif second==8:
    right='eight'
elif second==9:
    right='nine'
print(f' {x} :{left} {right}')"""
#question 2++++++++++++++++++++++
"""
for z in range(3):
    import random
    x=random.randint(1,13)
    y=random.randint(1,4)
    if x==1:
        symbol='Ace'
    elif x==2:
        symbol='two'
    elif x==3:
        symbol='three'
    elif x==4:
        symbol='four'
    elif x==5:
        symbol='five'
    elif x==6:
        symbol='six'
    elif x==7:
        symbol='seven'
    elif x==8:
        symbol='eight'
    elif x==9:
        symbol='nine'
    elif x==10:
        symbol='ten'
    elif x==11:
        symbol='jack'
    elif x==12:
        symbol='queen'
    elif x==13:
        symbol='king'
    if y==1:
        typ='diamond'
        color='red'
    elif y==2:
        typ='heart'
        color='red'
    elif y==3:
        typ='spade'
        color='black'
    elif y==4:
        typ='club'
        color='black'
    print(f'{symbol} of {typ} in color {color}')        
"""
""""
import random
num1=random.randint(1,13)
num2=random.randint(1,13)
num3=random.randint(1,13)
typ1=random.randint(1,4)
typ2=random.randint(1,4)
typ3=random.randint(1,4)
print(f' numbers\n{num1}  {num2}  {num3}')
print(f'type\n{typ1}  {typ2}   {typ3}')
if num1<num2 and num2<num3:
    if typ1==typ2 and typ2==typ3:
        print('all cards are in sequence and of samr type')
    else:
         print ('all cards are in sequence')
elif num1==num2 and num2==num3:
    if typ1==typ2 and typ2==typ3:
        print('all cardshave same number and of samr type')
    else:
         print ('all cards have same numbers')
elif typ1==typ2 or typ1==typ3 or typ2==typ3:
    print('two cards have same type')
elif num1<num2 or num2<num3:
    print('two cards are in sequence')
if typ1==1 or typ1==2:
    if typ2==1 or typ2==2:
        if typ3==1 or typ3==2:
            print('all cards have same color')
else:
    if num1>num2 and num2>num3 :
        print ('1 is highest {num1}' )
    elif num2>num1 and num2>num3:
        print ('2nd is heighest {num2}')
    elif num3>num2 and num3>num1:
        print('3rd is heighest {num3}')"""
#question3++++++++++++++
"""
x=input('Enter any character : ')
char=ord(x)
flip=char^0b111111
print(f'character after flip :{chr(flip)}')"""

#practice 10 ------------------------------------PRACTICE 10-------------------
 #question1 (print even  number in single line)
"""
x=0
while(x<=100):
    print (x ,end=' ')
    x+=2
print('even numbers in single line') """
#question 2(input starting and ending numbers)
"""
x=int(input('enter the starting number :'))
y=int (input ('enter the ending number :'))
while (x<=y):
    print(x ,end=' ')
    x+=1
"""
#question 3(input 5 numbers and print thier sum)
"""
count=1
sum=0
while count<=5:
     num=int(input('enter number : '))
     sum+=num
     count+=1
print(sum)   """ 
#question 4 (input 5 numbers and print maximum number)
"""
max=0
count=1
while count<=5:
    count+=1
    num=int(input ('enter number : '))
    if max<num:
        max=num
print(max)"""
 #question 5(odd numbers from 49 t0 1)
"""
odd=49
while odd>=1:
    print (odd ,end=' ')
    odd-=2

print('\n odd number')  """  
    
#PRACTICE 11-------------------------PRACTICE 11-------------------------------
#task01++++++++(loop runs 10 times tell which one is larger )
"""
import random
i=1
while i<=10:
    i+=1
    x=random.randint(1,20)
    y=random.randint(1,20)
    if x>y:
        print(f'{x} is larger than {y}')
    elif y>x:
        print(f'{y} is larger than {x}')
    else:
        print(f'{x} and {y}  are equal')"""
#task2+++++(print three random numbrers in ascending order)
"""
import random
i=1
while i<=10:
    i+=1
    x=random.randint(1,10)
    y=random.randint(10,20)
    z=random.randint(20,30)
    print(f'{x} {y} {z}')
    if x>y:
        x,y=y,x
    if y>z:
        y,z=z,y
    if x>y:
        x,z=z,x"""
#method 2============
"""
import random
i=1
while i<=10:
    x=random.randint(1,20)
    y=random.randint(1,20)
    z=random.randint(1,20)
    print(f'{x} {y} {z}')
    if x<y:
        if y<z:
            a,b,c=x,y,z
        else:
             a,b,c=x,z,y
    elif y<z:
        if z<x:
            a,b,c=y,z,x
        else:
            a,b,c=y,x,z
    elif z<x:
        if x<y:
            a,b,c=z,x,y
        else:
            a,b,c=z,y,x
        
    print (a,b,c)
    i+=1"""
#task 3++++++++(one to hundred print in words)
"""
import random
def wording(n):
    
    if n==1:
        return"one"
    elif n==2:
        return"two"
    elif n==3:
        return"three"
    elif n==4:
        return"four"
    elif n==5:
        return"five"
    elif n==6:
        return"six"
    elif n==7:
        return"seven"
    elif n==8:
        return"eight"
    elif n==9:
        return"nine"
    elif n==10:
        return"ten"
    elif n==11:
        return"eleven"
    elif n==12:
        return"twelve"
    elif n==13:
        return"thirteen"
    elif n==14:
        return"fourteen"
    elif n==15:
        return"fifteen"
    elif n==16:
        return"sixteen"
    elif n==17:
        return"seventeen"
    elif n==18:
        return"eighteen"
    elif n==19:
        return"nineteen"
    elif n==20:
        return"twenty"
    elif n==30:
        return"thirty"
    elif n==40:
        return"fourty"
    elif n==50:
        return"fifty"
    elif n==60:
        return"sixty"
    elif n==70:
        return"seventy"
    elif n==80:
        return"eighty"
    elif n==90:
        return"ninety"
    elif n==100:
        return"hundred"
    elif n>=21 and n<=29:
        return "twenty-"+wording(n%10)
    elif n>=31 and n<=39:
        return "thirty-"+wording(n%10)
    elif n>=41 and n<=49:
        return "fourty-"+wording (n%10)
    elif n>=51 and n<=59:
        return "fifty-"+wording (n%10)
    elif n>=61 and n<=69:
        return "sixty-"+wording(n%10)
    elif n>=71 and n<=79:
        return "seventy-"+wording(n%10)
    elif n>=81 and n<=89:
        return "eighty-"+wording(n%10)
    elif n>=91 and n<=99:
        return "ninety-"+wording(n%10)
    else :
        return "invalid number"

i=1
while i<=10:
    i+=1
    x=random.randint(1,100)
    print (f'{x} {wording(x)}')"""
#task 4+++++++++(random capital letter tell which one is vowel or consonent)

"""
import random
i=1
while i<=10:
    i+=1
    x=chr(random.randint(65,90))

    if x=='A' or x=='E' or x=='I' or x=='O' or x=='U' :
        print(f'Alphabete {x} is vowel')
    else :
        print(f'ALbhabet {x} is not vowel')"""
#task 5+++++++
"""
import random
i=1
sum_e=0
sum_o=0
while i<=10:
    x=random.randint(1,10)
    print(x,end=' ')
    i+=1
    if x%2==0:
        sum_e+=x
    else:
        sum_o=x+sum_o
print ('\nsum of even number',sum_e)
print ('sum of odd number ',sum_o )"""

#hackerrank question 1
"""

x=int(input('enter any positive integer'))
if x<=0:
    x=int(input('enter positive number'))
i=1
capital=65
small=97
while i<=x:
    
    print(chr(capital),end=" ")
    capital +=1
    i+=1
n=1
print()
while n<=x :   
      
    print(chr(small),end=' ')
    small +=1
    n+=1"""
    #hacker rank qiuestion 2
"""    
x=int(input())
i=1
capital=65
small=122
while i<=x:
    print(f'{chr(capital)}{chr(small)}',end='')
    small-=1
    capital+=1
    i+=1  """  
#hacker rank
"""
x=int(input())
if x%2==0:
    i=1
    while i<=x:
        print(i,end=' ')
        i+=1
        
else:
    while x>=1:
        print(x,end=' ')
        x-=1"""

#practice task 13--------------practice task 13-------------------------
#question 1+++++++++







#practice task 14--------------practice task 14------------------------

#question 1:

"""


i=65
while i<=90:
    if chr(i)=='A'or chr(i)=='E'or chr(i)=='I'or chr(i)=='O' or chr(i)=='U':
        print(f'\n {chr(i)}')
    else :
        print(chr(i),end=' ')
    i+=1         

"""

"""i=1
while i<=100:
    if i%3==0 and i%5!=0 or i%3!=0 and i%5==0:
        print(i,end=' ')
    i+=1
 """








#practice task 15---------------practice 15------------
#question 1++++++++++++=
"""
import random
count=0
i=1
while i<=10:
   x=random.randint(0,255)
   y=random.randint(0,255)
   print(f'first num {x} second num : {y}')
   if x&1==y&1:
       count+=1
   if x&2==y&2:
       count+=1
   if x&4==y&4:
       count+=1
   if x&8==y&8:
       count+=1
   if x&16==y&16:
       count+=1
   if x&32==y&32:
       count+=1
   if x&64==y&64:
       count+=1
   if x&128==y&128:
       count+=1
   print(f'similar bits in {x} and {y} are{count}')
   i+=1"""

#question 2+++++++
"""
x=int(input ('enter num'))
while x>0:
    print(x%8,end='')
    x=x//8"""


    
#question no.3+++++++++
"""
import random
h_set=0
h_avg=0
i=1
while i<=10:
    x=random.randint(1,10)
    y=random.randint(1,10)
    z=random.randint(1,10)
    avg=x+y+z//3
    print(x,y,z,'\t',avg)
    if avg > h_avg:
        h_avg=avg
        h_set=i
    i+=1    
print('heighest set is ',h_set)
"""

#question4++++++++++++++
"""
import random
h_set=0
m_set=0
m_avg=float('inf')  #100
h_avg=0
i=1
while i<=10:
    x=random.randint(1,10)
    y=random.randint(1,10)
    z=random.randint(1,10)
    avg=x+y+z//3
    print(x,y,z,'\t',avg)
    if avg > h_avg:
        h_avg=avg
        h_set=i
        a,b,c=x,y,z
    if avg < m_avg:
        m_avg=avg
        m_set=i
        p,q,r=x,y,z
    i+=1    
print('heighest set is ',h_set,'with element :', a,b,c)
print('minimum  set is ',m_set,'with element :', p,q,r)"""
#lab task 2
"""
import random
i=1
grade=''
fail=0
s_mid=0
s_fin=0
s_ses=0
s_total=0
ma_total=0
ma_mid=0
ma_ses=0
ma_fin=0
mi_total=float('inf')
mi_mid=float('inf')
mi_ses=float('inf')
mi_fin=float('inf')

print('Roll no\tMid\tFinal\tsessional\ttotal\tgrade')
while i<=30:
    
    mid=random.randint(0,35)
    fin=random.randint(0,40)
    ses=random.randint(0,25)
    total=mid+fin+ses
    print(f'{i}\t{mid}\t{fin}\t{ses}\t\t{total}\t{grade}')
    if total>=85:
        grade='A'
    elif total>=80:
        grade='A-'
    elif total>=75:
        grade='B+'
    elif total>=70:
        grade='B'
    elif total>=65:
        grade='B-'
    elif total>=61:
        grade='C+'    
    elif total>=58:
        grade='C'
    elif total>=55:
        grade='C-'
    elif total>=50:
        grade='D'
    elif total<50:
        grade='F'
        fail+=1
    i+=1
    s_mid=s_mid+mid
    s_fin=s_fin+fin
    s_ses=s_ses+ses
    s_total=s_total+total
    if ma_mid<mid:
        ma_mid=mid
    if ma_fin<fin:
        ma_fin=fin
    if ma_ses<ses:
        ma_ses=ses
    if ma_total<total:
        ma_total=total
    if mi_mid>mid:
        mi_mid=mid
    if mi_fin>fin:
        mi_fin=fin
    if mi_total>total:
        mi_total=total
    if mi_ses>ses:
        mi_ses=ses    
print(f'Total :30')
print(f'Pass:{30-fail}')
print(f'Fail :{fail}')
print(f'Overall Average Marks:  {s_total//30}')
print(f'Average Midterm Marks:  {s_mid//30}')
print(f'Average Sessional Marks:{s_ses//30}')
print(f'Average Final  Marks:   {s_total//30}')
print(f'Maximum Marks:          {ma_total}' )     
print(f'Maximum Final marks:    {ma_fin}')
print(f'Maximum  Sessional marks:{ma_ses}')
print(f'Maximum  Midterm marks: {ma_mid}')

print(f'Minimum  Marks:         {mi_total}')
print(f'Minimum  Midterm marks: {mi_mid}')
print(f'Minimum  Sessional marks:{mi_ses}')
print(f'Minimum  Final marks:    {mi_fin}')"""
    
