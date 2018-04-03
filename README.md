 # Programming and Scripting GMIT
## This repository contains exercises submissions for the 2018 GMIT Programming and Scripting marked course work. It also contains three additional folders

The .vscode folder contains shortcuts for Visual Studio code

The Problem Sets folder contains Python Scripts attempting to solve the problem sets given in Week 8

The Weekly Exercises folder contains rough work following the materials provided during the weekly lectures and from the Official Python Tutorial

### To run the files:
1. Download and install Anaconda https://www.anaconda.com/download/
2. I recommend using visual studio to run the files https://www.visualstudio.com/downloads/
3. To run the file open it in visual studio terminal, type Python then the full file name, and don't forget to include the .py file        extension. You may also copy the tasks.json file to create the shortcut Ctrl Shift b to automatically run the active file in the      Visual Studio Terminal.

#### Respository content, descriptions of exercises and instructions how to run the associated scripts:

Note: separate file versions have also been added for some exercises the respository, these are versions where I made changes to the code in the weeks after the exercises were due to be completed. 

Topic 1: Basics of programming and Topic 2: State, variables and Statements

Exercise 1: Contained in the file Exercise_1_and_2_v1.0.py. run the example program given in topic one and post your result to the discussion topic in the discussion forum. Here is a copy of my post to the discussion forum. My name is Simon, so the first and last letter of my name (S + N = 19 + 14) give the number  33, the 33rd Fibonacci number is 352,4578. 

Exercise 2: Also contained in the file Exercise_1_and_2_v1.0.py. Copy and run the program contained in https://github.com/ianmcloughlin/python-fib/blob/master/fibname.py. I changed the string variable to my own surname and re-ran it to give the following results:

My surname is: McLain
The first letter M is number: 77
The last letter n is number: 110
Fibonacci number 187 is: 538522340430300790495419781092981030533
The ord() function is used to return an integer of the given single Unicode character. The returned integer represents the Unicode code point.(reference: https://www.jquery-az.com)

If you wish to use this on your own name change row 29 from "McLain" to "yoursurname". 

The explaination of the Python ord() Function as described on the https://www.jquery-az.com website: The ord() function is used to return an integer of the given single Unicode character. The returned integer represents the Unicode code point.

Topic 3: Conditions, loops and flow control

Exercise3: Contained in Exercise_3_v1.0.py. Write a single Python script that starts with an integer and repeatedly applies the Collatz function (divide by 2 if even, multiply by three and 1 if odd) using a while loop and if statement. At each iteration, the current value of the integer should be printed to the screen. You can specify in your code the starting value of 17. Exercise_3_v1.1.py has been enhanced to ask the user for an input instead of using a starting value of 17. 

My solution was researched on YouTube and combined the content of several videos to produce the code https://www.youtube.com/results?search_query=collatz+conjecture+python

Topic 4: Lists

Exercise 4: Contained in the file named Exercise_4_v1.0.py. Write a script to solve problem 5 from Project Euler: https://projecteuler.net/problem=5. 

In the v.1.1 I copied code from https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution 
I modified this code slightly so it would run, changing xrange to range and adding parentheses to the print statements.
This code runs much faster than my original v1.0

Exercise 5. Topic 5: Input and output

Write a Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format. On the screen should be printed the petal length, petal width, sepal length and sepal width, and these values should have the decimal places aligned, with a space between the columns. I researched the solution on YouTube https://www.youtube.com/results?search_query=euler+problem+5+python combining the content of several videos listed to produce the code. 

Exercise 6. Topic 6: Functions

Write a Python script containing a function called factorial() that takes a single input/argument which is a positive integer and returns its factorial. The solution I created was based on the GMIT lecture content. 
