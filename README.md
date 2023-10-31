# Here is my HackerRank Solutions

>The repository contains the solutions to various HackerRank problems.Organize the solutions so they are easy to navigate and understand. Each solution includes a reference to the problem statement and is well-documented to explain the logic and approach.

## 1.Simple Array Sum

  - [Problem](https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true)
  - [Solution]()
  - Explanation:
  >In this problem, we will be calculating the sum of elements in an array using Python. The code prompts the user to enter the number of elements in the array and then takes input for each element. It then calculates the sum of the array and prints the result.
>
1.The program starts by asking the user to input the number of elements they want to have in the array (n).

2.An empty array (arr) is initialized to store these elements.

3.A loop runs from 0 to (n-1), where the user is prompted to enter each element for the array. It handles the ValueError exception if the user enters something that's not a valid number.

4.The calculate_sum function takes the array as an argument and calculates the sum of its elements.

5.The calculated sum is then printed.
### Program
```python
# Function to calculate the sum of elements in an array
def calculate_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Get user input for the array size
n = int(input("Enter the number of elements in the array: "))

# Initialize an empty array
arr = []

# Get user input for the elements of the array
for i in range(n):
    try:
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)
    except ValueError:
        print("Please enter a valid number for element {i + 1}.")

# Calculate the sum of the array using the defined function
result = calculate_sum(arr)

# Print the sum
print(f"The sum of the array is: {result}")

```
#### Sample input & output
input
```
Enter the number of elements in the array: 5
Enter element 1: 10
Enter element 2: 20
Enter element 3: 30
Enter element 4: 40
Enter element 5: 50
```
output
```
The sum of the array is: 150
```
****
## 2.Time Conversion

  - [Problem](https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true) 
  - [Solution](Time_Conversion/timeconversion.py) 
  - Explanation:
  >In this problem, i write a function called timeConversion that takes a time string in 12-hour format as input and converts it to 24-hour format. The code then prompts the user to enter a time string and calls the timeConversion function to convert the input time.
>
1.Import the datetime module to work with date and time objects.

2.Define a function called timeConversion that takes one parameter, s, which is the input time in a 12-hour format.

3.Inside the function, it uses datetime.strptime to parse the input string s into a datetime object. The '%I:%M:%S%p' format string is used to specify how the input time is formatted. %I represents the hour (01-12), %M represents the minute (00-59), %S represents the second (00-59), and %p represents either 'AM' or 'PM'.

4.Then, it formats the datetime object in 24-hour format using strftime with the format string '%H:%M:%S', where %H represents the hour (00-23), %M represents the minute (00-59), and %S represents the second (00-59).

5.The function returns the time in the 24-hour format.

6.In the if __name__ == '__main__': block, it takes user input for a time in 12-hour format.

7.Calls the timeConversion function with the user input as the argument and stores the result in the result variable.

8.Finally, it prints the converted time (in 24-hour format) using print(result).

### Program
```python
from datetime import datetime

def timeConversion(s):
    # Parse the input time string in the 12-hour format
    time_12hr = datetime.strptime(s, '%I:%M:%S%p')
    
    # Format the time in the 24-hour format
    time_24hr = time_12hr.strftime('%H:%M:%S')
    
    return time_24hr

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
```
#### Sample input & output
input
```
07:05:45PM
```
output
```
19:05:45
```
****
## 3.Mini-Max Sum

  - [Problem](https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true)
  - [Solution](Mini-Max_Sum/minimaxsum.py) 
  - Explanation:
  >This problem  takes an array of integers as input and calculates the minimum and maximum sums of four out of the five elements in the array.

#### The miniMaxSum function takes an array (arr) as input and performs the following steps:

1.The program first takes user input as a space-separated list of integers and stores them in the arr list.

2.It calculates the total_sum of all the numbers in the arr list by using the sum function.

3.It then computes the minimum and maximum sums:

  ->min_sum is calculated by subtracting the maximum number in the list (found using the max function) from the total_sum.
  ->max_sum is calculated by subtracting the minimum number in the list (found using the min function) from the total_sum.
  
4.Finally, the program prints both the min_sum and max_sum.
### Program
```python
def miniMaxSum(arr):
    total_sum = sum(arr)
    min_sum = total_sum - max(arr)
    max_sum = total_sum - min(arr)
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)

 ```
#### Sample input & output
input
```
1 2 3 4 5
```
output
```
10 14
```
****
## 5.Grading Students
  - [Problem](https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true)
  - [Solution](Grading_Students/gradingstudents.py) 
  - Explanation:
  > In this problem, I created a program that takes input for the number of grades to be entered, and then prompts the user to enter each grade. The program then rounds each grade according to a specific rule and prints the rounded grades.
> 
1.The gradingStudents function takes a list of grades as input.

2.It initializes an empty list called rounded_grades to store the rounded grades.

3.It iterates through each grade in the input list using a for loop.

4.For each grade, it first checks if the grade is less than 38. If it is, the grade remains unchanged because no rounding is needed. It appends the grade to the rounded_grades list.

5.If the grade is greater than or equal to 38, it calculates the next multiple of 5 greater than or equal to the grade. This is done by adding 4 to the grade and then using integer division by 5, followed by multiplication by 5. This step ensures that the grade is rounded up to the nearest multiple of 5.

6.It then checks if the difference between the next multiple of 5 and the original grade is less than 3. If it is, the program rounds up the grade to the next multiple of 5. Otherwise, it keeps the original grade as is.

7.The program continues this process for each grade in the input list and appends the rounded grades to the rounded_grades list.

8.The function returns the list of rounded grades.

9.The main part of the program begins by taking an integer grades_count as input, which represents the number of grades to be entered.

10.It then iterates grades_count times, taking individual grades as input from the user and appending them to the grades list.

11.Next, the gradingStudents function is called with the grades list as an argument, and the result is stored in the result variable.

12.Finally, the program prints each of the rounded grades in the result list one by one.

### Program
```python
def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            # If the grade is less than 38, no rounding is needed.
            rounded_grades.append(grade)
        else:
            next_multiple_of_5 = ((grade + 4) // 5) * 5
            if next_multiple_of_5 - grade < 3:
                # If the difference between the next multiple of 5 and the grade is less than 3, round up.
                rounded_grades.append(next_multiple_of_5)
            else:
                # Otherwise, keep the original grade.
                rounded_grades.append(grade)
    return rounded_grades

# Input
grades_count = int(input().strip())
grades = []
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

# Call the gradingStudents function
result = gradingStudents(grades)

# Output
for res in result:
    print(res)
write an short and understandable explanation for this program ```
#### Sample input & output
input
```
4
73
67
38
33
```
output
```
75
67
40
33
```
****
## 2.Birthday Cake Candles

  - [Problem](https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](Birthday_Cake_Candles/birthdaycakecandles.py) (navigate to the Solution file)
  - Explanation:
  > In this problem, we write a function called birthdayCakeCandles that takes in a list of candle heights as input and returns the count of the tallest candles. The code also includes an input section where the user can provide the number of candles and their heights.

###--Program--
```python
def birthdayCakeCandles(candles):
    max_height = max(candles)
    tallest_candles = candles.count(max_height)
    return tallest_candles

if __name__ == '__main__':
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    print(result)
```python


#### Sample input & output
input
```
4
3 2 1 3
```
output
```
2
```
In this example, we have a list of candle heights [3,2,1,3]. The tallest candles have a height of 3, and there are 2 candles with that height. Therefore, the output is 2.

****

## 3.Compare The Tripplets
  - [Problem](https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](Compare_The_Tripplets/comparethetriplets.py) (navigate to the Solution file)
  - Explanation:
  > In this problem, we have a function called ```compareTriplets``` that takes in two lists, a and b, representing the ratings of two people in three different categories. The function compares the ratings of each category and returns the number of points each person has earned.

```python
def compareTriplets(a, b):
    points = [0, 0]
    for i in range(3):
        if a[i] > b[i]:
            points[0] += 1
        elif a[i] < b[i]:
            points[1] += 1
    return points

```
 The ```compareTriplets``` function is defined, which takes in two lists, a and b.

 Inside the function, a ```list called points``` is initialized with two elements, representing the ```points earned by Alice and Bob```.

 A for loop is used to iterate over the ratings in the a and b lists.

Inside the loop, an if statement is used to compare the ratings of each category.

If ``` a is greater than b```, ```Alice earns a point```.

If  ```a is less than  b```, ```Bob earns a point```.

Finally, the ```points list is returned```.

```python
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = compareTriplets(a, b)
print(*result)
```
 In this part, we take ```input from the user``` for the ratings of the two people. The ratings are entered as space-separated values. The map function is used to convert the input values to integers and store them in lists a and b. Then, we call the compareTriplets function with the a and b lists as arguments. The result is stored in the result variable. Finally, we use the print function with the * operator to unpack the elements of the result list and print them.


#### Sample input & output
input
```
4 5 6
7 5 3
```
output
```
1 1
```
****
## 4.Diagonal Difference

  - [Problem](https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](Diagonal_Difference/diagonaldifference.py) (navigate to the Solution file)
  - Explanation:
  > In this problem, we have to calculate the diagonal difference in a square matrix. The diagonal difference is the absolute difference between the sums of its diagonals.

The diagonalDifference function takes a square matrix as input and calculates the diagonal difference.

```python
def diagonalDifference(arr):
    n = len(arr)
    s1, s2 = 0, 0

    for i in range(n):
        s1 += arr[i][i]
        s2 += arr[i][n - i - 1]

    return abs(s1 - s2)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = diagonalDifference(arr)
print(result)
```
 
It uses two variables, s1 and s2, to store the sums of the elements on the primary and secondary diagonals, respectively. 

It iterates over the rows of the matrix and adds the corresponding element to the sums. Finally, it returns the absolute difference between s1 and s2.

The main program prompts the user to enter the size of the matrix (n) and then takes n lines of input, each containing n space-separated integers. It creates a 2D list arr to store the matrix. 

It then calls the diagonalDifference function with arr as the argument and assigns the result to the variable result. 

Finally, it prints the result.

#### Sample input & output
input
```
3
1 2 3
4 5 6
7 8 9
```
 the size of the matrix = 3

The primary diagonal elements are 1, 5, and 9, and their sum is 1 + 5 + 9 = 15. 

The secondary diagonal elements are 3, 5, and 7, and their sum is 3 + 5 + 7 = 15.

The absolute difference between the sums of the primary and secondary diagonals is |15 - 15| = 0.

output
```
0
```
****
## 5.Grading Students
  - [Problem](https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](Grading_Students/gradingstudents.py) (navigate to the Solution file)
  - Explanation:
  > In this problem, I created a program that takes input for the number of grades to be entered, and then prompts the user to enter each grade. The program then rounds each grade according to a specific rule and prints the rounded grades.
```python
n = int(input().strip())

for _ in range(n):
    grade = int(input().strip())
    
    if grade >= 38 and grade % 5 >= 3:
        grade += 5 - (grade % 5)

    print(grade)

```

It takes input for the number of grades to be entered as n.

 It uses a for loop to iterate over the range of the number of grades.

 Inside the loop, it takes input for each grade.

 It checks if the grade is greater than or equal to 38 and if the remainder of the grade divided by 5 is greater than or equal to 3.

 If the condition is true, it rounds the grade by adding the difference between 5 and the remainder of the grade divided by 5.
 
 Finally, it prints the rounded grade.

```
n = int(input().strip())  # Enter the number of grades: 3

for _ in range(n):
    grade = int(input().strip())  # Enter the grades: 73, 67, 41
    
    if grade >= 38 and grade % 5 >= 3:
        grade += 5 - (grade % 5)
    
    print(grade)
Output:

75
67
41
```
In this example, we entered 3 grades: 73, 67, and 41. The first grade, 73, is rounded up to 75 because the remainder of 73 divided by 5 is 3, which is greater than or equal to 3. The second grade, 67, remains the same because the remainder of 67 divided by 5 is 2, which is less than 3. The third grade, 41, also remains the same because it is less than 38.
****

## 7.Plus Minus

  - [Problem](https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true) (navigate to the Problem)
  - [Solution](Plus_Minus/plusminus.py) (navigate to the Solution file)
  - Explanation:
  >The plusMinus function is a Python function that takes an array of integers as input and calculates the ratio of positive, negative, and zero elements in the array. It then prints these ratios with a precision of 6 decimal places.

```python
def plusMinus(arr):
    n = len(arr)
    countPositive = sum(1 for num in arr if num > 0)
    countNegative = sum(1 for num in arr if num < 0)
    countZero = n - countPositive - countNegative

    print(f"{countPositive/n:.6f}")
    print(f"{countNegative/n:.6f}")
    print(f"{countZero/n:.6f}")
```
 ```sum(1 for num in arr if num > 0)```: This expression uses a generator expression to count the number of positive elements in the array. It iterates over each element num in the array arr and increments the count by 1 if the element is greater than 0.

 ```sum(1 for num in arr if num < 0)```: This expression counts the number of negative elements in the array using a similar approach as above, but checks if the element is less than 0.

 ```n - countPositive - countNegative```: This expression calculates the number of zero elements in the array by subtracting the counts of positive and negative elements from the total number of elements in the array.


 The function takes an array arr as input and performs the calculations to determine the ratios of positive, negative, and zero elements. It then prints these ratios.

```python
#Input
n = int(input())
arr = list(map(int, input().split()))

plusMinus(arr)
```
 In this part, the user is prompted to enter the number of elements in the array (n). Then, the user is asked to enter the elements of the array separated by spaces. 
 
 The map function is used to convert the input string into a list of integers. Finally, the plusMinus function is called with the array as the argument.

#### Sample input & output
input
```
3
5 -3 2
```
output
```
0.666667
0.333333
0.000000
```
****

## 9.StairCase

  - [Problem](https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true) (navigate to the Problem)
  - [Solution](Staircase/Staircase.py) (navigate to the Solution file)
  - Explanation:
  >To create the staircase pattern, we will use nested loops and the print() function in Python. The outer loop will iterate over the number of steps, and the inner loops will handle the printing of spaces and "#" symbols.


```python
def print_stair(n):
    for i in range(1, n+1):
        for j in range(i, n):
            print(" ", end="")
        
        for k in range(1, i+1):
            print("#", end="")
        
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of steps: "))
    print_stair(n)
```
The ``` print_stair() ``` function takes an integer n as input, which represents the number of steps in the staircase. The function uses two nested loops to print the spaces and "#" symbols.

The outer loop iterates from 1 to n+1, representing the rows of the staircase. The inner loop, ``` for j in range(i, n)```, prints the spaces before the "#" symbols. The number of spaces decreases as we move down the rows.

The second inner loop, ```for k in range(1, i+1)```, prints the "#" symbols. The number of "#" symbols increases as we move down the rows.

Finally, the ```print()``` function is used to print a new line after each row of the staircase.

In the main block, the user is prompted to enter the number of steps. The input is converted to an integer using the int() function. Then, the print_stair() function is called with the user-provided input.

#### Sample input & output
input
```
Enter the number of steps: 5
```
output
```
    # 
   ##
  ###
 ####
#####
```

by Anandha krishnan
