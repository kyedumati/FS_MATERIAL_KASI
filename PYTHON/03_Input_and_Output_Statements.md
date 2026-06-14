# Input And Output Statements

## Reading dynamic input from the keyboard:

In Python 2 the following 2 functions are available to read dynamic input from the keyboard.

 1. raw_input()
 2. input()

### 1. raw_input():

 This function always reads the data from the keyboard in the form of String Format.  We have to convert that string type to our required type by using the corresponding type casting methods.

**Eg:**
```python
 x=raw_input("Enter First Number:")
 print(type(x))    It will always print  str type only for any input type
```

### 2. input():

 input() function can be used to read data directly in our required format.We are not required to perform type casting.

```python
 x=input("Enter Value)
 type(x)

 10 ===> int
 "virat"===>str
 10.5===>float
 True==>bool
```

 ***Note:**  But in Python 3 we have only input() method and raw_input() method is not available.
 Python3 input() function behaviour exactly same as raw_input() method of Python2. i.e every input value is treated as str type only.

 raw_input() function of Python 2 is renamed as input() function in Python3

**Eg:**

```python
1)  >>> type(input("Enter value:"))
2) Enter value:10
3) <class 'str'>
4)
5) Enter value:10.5
6) <class 'str'>
7)
8) Enter value:True
9) <class 'str'>
```

## Q. Write a program to read 2 numbers from the keyboard and print sum.

```python
1) x=input("Enter First Number:")
2) y=input("Enter Second Number:")
3) i = int(x)
4) j = int(y)
5) print("The Sum:",i+j)
6)
7) Enter First Number:100
8) Enter Second Number:200
9) The Sum: 300
```

-----------------------------------------------------

```python
1) x=int(input("Enter First Number:"))
2) y=int(input("Enter Second Number:"))
3) print("The Sum:",x+y)
```

-----------------------------------------------------------

```python
1) print("The Sum:",int(input("Enter First Number:"))+int(input("Enter Second Number:")))
```

## Q. Write a program to read Employee data from the keyboard and print that data.

```python
1) eno=int(input("Enter Employee No:"))
2) ename=input("Enter Employee Name:")
3) esal=float(input("Enter Employee Salary:"))
4) eaddr=input("Enter Employee Address:")
5) married=bool(input("Employee Married ?[True|False]:"))
6) print("Please Confirm Information")
7) print("Employee No :",eno)
8) print("Employee Name :",ename)
9) print("Employee Salary :",esal)
10) print("Employee Address :",eaddr)
11) print("Employee Married ? :",married)
12)
13) D:\Python_classes>py test.py
14) Enter Employee No:100
15) Enter Employee Name:Sunny
16) Enter Employee Salary:1000
17) Enter Employee Address:Mumbai
18) Employee Married ?[True|False]:True
19) Please Confirm Information
20) Employee No : 100
21) Employee Name : Sunny
22) Employee Salary : 1000.0
23) Employee Address : Mumbai
24) Employee Married ? : True
```

## How to read multiple values from the keyboard in a single line:

```python
1) a,b= [int(x) for x in input("Enter 2 numbers :").split()]
2) print("Product is :", a*b)
3)
4) D:\Python_classes>py test.py
5) Enter 2 numbers :10 20
6)  Product is : 200
```

**Note:**  split() function can take space as seperator by default      .But we can pass anything as seperator.

## Q. Write a program to read 3 float numbers from the keyboard with , seperator and print their sum.

```python
1) a,b,c= [float(x) for x in input("Enter 3 float numbers :").split(',')]
2) print("The Sum is :", a+b+c)
3)
4) D:\Python_classes>py test.py
5) Enter 3 float numbers :10.5,20.6,20.1
6) The Sum is : 51.2
```

## eval():

eval Function take a String and evaluate the Result.

**Eg:** x = eval("10+20+30")
    print(x)

    Output: 60

**Eg:** x = eval(input("Enter Expression"))
    Enter Expression:  10+2*3/4
    Output11.5

eval() can evaluate the Input to list, tuple, set, etc based the provided Input.

**Eg:** Write a Program to accept list from the keynboard on the display

```python
1) l = eval(input("Enter List"))
2)  print (type(l))
3)  print(l)
```

# Command Line Arguments

- argv is not Array it is a List. It is available sys Module.
- The Argument which are passing at the time of execution are called Command Line Arguments.

**Eg:** D:\Python_classes py test.py 10 20 30
                                  Command Line Arguments

Within the Python Program this Command Line Arguments are available in argv. Which is present in SYS Module.

```
test.py   10   20   30
```

**Note:** argv[0] represents Name of Program. But not first Command Line Argument.
argv[1] represent First Command Line Argument.

**Program:** To check type of argv from sys

```python
import argv
print(type(argv))
```

D:\Python_classes\py test.py

## Write a Program to display Command Line Arguments

```python
1) from sys import argv
2) print("The Number of Command Line Arguments:", len(argv))
3) print("The List of Command Line Arguments:", argv)
4) print("Command Line Arguments one by one:")
5) for x in argv:
6)     print(x)
7)
8) D:\Python_classes>py test.py 10 20 30
9) The Number of Command Line Arguments: 4
10) The List of Command Line Arguments: ['test.py', '10','20','30']
11) Command Line Arguments one by one:
12) test.py
13) 10
14) 20
15) 30
```

```python
1) from sys import argv
2) sum=0
3) args=argv[1:]
4) for x in args   :
5)    n=int(x)
6)    sum=sum+n
7) print("The Sum:",sum)
8)
9) D:\Python_classes>py test.py 10 20 30 40
10) The Sum: 100
```

**Note1:** usually space is seperator between command line arguments. If our command line argument itself contains space then we should enclose within double quotes(but not single quotes)

**Eg:**

```python
1) from sys import argv
2) print(argv[1])
3)
4) D:\Python_classes>py test.py Sunny Leone
5) Sunny
6)
7) D:\Python_classes>py test.py 'Sunny Leone'
8) 'Sunny
9)
10) D:\Python_classes>py test.py "Sunny Leone"
11) Sunny Leone
```

**Note2:** Within the Python program command line arguments are available in the String form. Based on our requirement,we can convert into corresponding type by using type casting methods.

**Eg:**

```python
1) from sys import argv
2) print(argv[1]+argv[2])
3) print(int(argv[1])+int(argv[2]))
4)
5) D:\Python_classes>py test.py 10 20
6) 1020
7) 30
```

**Note3:** If we are trying to access command line arguments with out of range index then we will get Error.

**Eg:**

```python
1) from sys import argv
2) print(argv[100])
3)
4) D:\Python_classes>py test.py 10 20
5)  IndexError: list index out of range
```

**Note:**

In Python there is  argparse module to parse command line arguments and display some help messages whenever end user enters wrong input.

```
    input()
    raw_input()

    command line arguments
```

## output statements:

We can use print() function to display output.

**Form-1:** print() without any argument
Just it prints new line character

**Form-2:**

```python
1) print(String):
2) print("Hello World")
3)   We can use escape characters also
4)  print("Hello \n World")
5)  print("Hello\tWorld")
6)   We can use repetetion operator (*) in the string
7)  print(10*"Hello")
8)  print("Hello"*10)
9)   We can use + operator also
10)  print("Hello"+"World")
```

**Note:**
If both arguments are String type then + operator acts as concatenation operator.

If one argument is string type and second is any other type like int then we will get Error

If both arguments are number type then + operator acts as arithmetic addition operator.

**Note:**

```python
1)  print("Hello"+"World")
2)  print("Hello","World")
3)
4)  HelloWorld
5)  Hello World
```

**Form-3:** print() with variable number of arguments:

```python
1.  a,b,c=10,20,30
2.  print("The Values are :",a,b,c)
3.
4.  Output The Values are : 10 20 30
```

By default output values are seperated by space.If we want we can specify seperator by using "sep" attribute

```python
1.  a,b,c=10,20,30
2.  print(a,b,c,sep=',')
3.  print(a,b,c,sep=':')
4.
5.  D:\Python_classes>py test.py
6.  10,20,30
7.  10:20:30
```

**Form-4:**print() with end attribute:

```python
1.  print("Hello")
2. print("Virat")
3.  print("Soft")
```

**Output:**

```
1.  Hello
2.  Virat
3.  Soft
```

If we want output in the same line with space

```python
1.  print("Hello",end=' ')
2. print("Virat",end=' ')
3.  print("Kohli")
```

**Output:** Hello Virat Kohli

**Note:** The default value for end attribute is \n,which is nothing but new line character.

**Form-5:**  print(object) statement:

We can pass any object (like list,tuple,set etc)as argument to the print() statement.

**Eg:**

```python
1.  l=[10,20,30,40]
2.  t=(10,20,30,40)
3.  print(l)
4.  print(t)
```

**Form-6:** print(String,variable list):

We can use print() statement with String and any number of arguments.

**Eg:**

```python
1. s="Virat"
2.  a=48
3.  s1="java"
4.  s2="Python"
5.  print("Hello",s,"Your Age is",a)
6.  print("You are teaching",s1,"and",s2)
```

**Output:**

```
1)  Hello Virat Your Age is 48
2)  You are teaching java and Python
```

**Form-7:** print(formatted string):

```
%i====>int
%d====>int
%f=====>float
%s======>String type
```

**Syntax:**

print("formatted string"  %(variable list))

**Eg 1:**

```python
1) a=10
2) b=20
3) c=30
4) print("a value is %i" %a)
5) print("b  value is %d and c value is %d" %(b,c))
6)
7) Output
8) a value is 10
9) b  value is 20 and c value is 30
```

**Eg 2:**

```python
1) s="Virat"
2)  list=[10,20,30,40]
3)  print("Hello %s ...The List of Items are %s"  %(s,list))
4)
5)     Output  Hello Virat ...The List of Items are [10, 20, 30, 40]
```

**Form-8:** print() with replacement operator {}

**Eg:**

```python
1) name="Virat"
2)  salary=10000
3)  gf="Sunny"
4)  print("Hello {0} your salary is {1} and Your Friend {2} is waiting".format(name,salary,gf))
5)  print("Hello {x} your salary is {y} and Your Friend {z} is waiting".format(x=name,y=salary,z=
   gf))
6)
7)  Output
8) Hello Virat your salary is 10000 and Your Friend Sunny is waiting
9) Hello Virat your salary is 10000 and Your Friend Sunny is waiting
```
