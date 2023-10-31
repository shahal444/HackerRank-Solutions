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
 ```
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

## 6.Forming a Magic Square

  - [Problem](https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true)
  - [Solution]()
  - Explanation:

1.magic_squares is a list of all possible 3x3 magic squares, represented as nested lists.

2.min_cost is initialized with positive infinity (float('inf')). It will be used to keep track of the minimum cost to transform the input square into a magic square.

3.The program defines a loop to iterate through each of the possible magic squares in magic_squares.

4.For each magic square, it calculates the cost of transforming the input square s into that magic square. The cost is computed as the sum of absolute differences between the corresponding elements of the input square and the magic square.

5.It keeps track of the minimum cost encountered among all magic squares.

6.After looping through all magic squares, the function returns the min_cost, which represents the minimum cost to transform the input square into a magic square.

7.In the if __name__ == '__main__': block, the program reads a 3x3 square from the user as input, stores it in the s list, and then calls the formingMagicSquare function to compute the minimum cost. Finally, it prints the result.

### Program
```python
def formingMagicSquare(s):
    # List of all possible 3x3 magic squares
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]

    min_cost = float('inf')

    for magic_square in magic_squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(s[i][j] - magic_square[i][j])
        min_cost = min(min_cost, cost)

    return min_cost

if __name__ == '__main__':
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    result = formingMagicSquare(s)
    print(result)

```
#### Sample input & output
input
```
5 3 4
1 5 8
6 4 2
```
output
```
8 3 4
1 5 9
6 7 2
```
****
## 7.Missing Numbers

  - [Problem](https://www.hackerrank.com/challenges/missing-numbers/problem?isFullScreen=true)
  - [Solution]()
  - Explanation:

  1.Two dictionaries, count_arr and count_brr, are created to store the counts of numbers in the arr and brr lists, respectively.

2.The program then iterates through the arr list and populates the count_arr dictionary, counting how many times each number appears in arr.

3.Similarly, it iterates through the brr list and populates the count_brr dictionary with counts of numbers in brr.

4.An empty list called missing_numbers is initialized to store the missing numbers.

5.The program compares the counts of numbers in the arr and brr lists. If a number is present in brr but not in arr, or if it appears more times in brr than in arr, it is considered a missing number, and it is added to the missing_numbers list.

6.The missing_numbers list is sorted in ascending order.

7.The function returns the sorted list of missing numbers.

### Program
```python
#!/bin/python3

import math
import os
import random
import re
import sys

def missingNumbers(arr, brr):
    # Create dictionaries to store the counts of numbers in arr and brr
    count_arr = {}
    count_brr = {}
    
    # Populate count_arr with counts from arr
    for num in arr:
        if num in count_arr:
            count_arr[num] += 1
        else:
            count_arr[num] = 1
    
    # Populate count_brr with counts from brr
    for num in brr:
        if num in count_brr:
            count_brr[num] += 1
        else:
            count_brr[num] = 1
    
    # Initialize a list to store the missing numbers
    missing_numbers = []
    
    # Compare the counts in arr and brr to find missing numbers
    for num, count in count_brr.items():
        if num not in count_arr or count_arr[num] < count:
            missing_numbers.append(num)
    
    return sorted(missing_numbers)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

```
#### Sample input & output
input
```
10
203 204 205 206 207 208 203 204 205 206
13
203 204 204 205 206 207 205 208 203 206 205 206 204
```
output
```
204 205 206
```
****
## 8.Compare The Tripplets
  - [Problem](https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true)
  - [Solution]
  - Explanation:
  > In this problem, we have a function called ```compareTriplets``` that takes in two lists, a and b, representing the ratings of two people in three different categories. The function compares the ratings of each category and returns the number of points each person has earned.

1.Import necessary libraries and modules.

2.Define a function called compareTriplets that takes two lists, 'a' and 'b', as input.

3.Initialize two variables, alice_score and bob_score, to 0. These variables will keep track of Alice and Bob's total scores in the game.

4.Use a loop to iterate through the three elements of the lists (representing the three categories of the game).

5.Inside the loop, compare the scores in the current category:

6.If Alice's score is greater than Bob's score, increment alice_score by 1.
If Bob's score is greater than Alice's score, increment bob_score by 1.
After looping through all three categories, the function returns a list containing two values: Alice's total score and Bob's total score.

7.In the if __name__ == '__main__': block, the program takes input for the lists 'a' and 'b' from the user. It assumes that these lists contain three integers each.

8.The compareTriplets function is called with 'a' and 'b' as arguments, and the result is stored in the 'result' variable. The result is a list of two integers, representing Alice's and Bob's total scores.

9.The program opens an output file specified by the environment variable 'OUTPUT_PATH' and writes the two scores to the file.

70.Finally, the output file is closed, and the program finishes.

```python
#!/bin/python3

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0

    # Iterate through the elements of a and b
    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1

    return [alice_score, bob_score]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

```
#### Sample input & output
input
```
5 6 7
3 6 10
```
output
```
1 1
```
****
## 9.Candies

  - [Problem](https://www.hackerrank.com/challenges/candies/problem?isFullScreen=true)
  - [Solution]()
  - Explanation:

1.The program starts by reading an integer 'n' representing the number of students and an array 'arr' containing their performance scores.

2.It initializes another array 'candies' of the same length as 'arr' and sets all elements to 1. This array will keep track of the number of candies each student receives.

3.It then iterates through the 'arr' from left to right. If a student's performance is better than the previous student, their 'candies' value is set to one more than the previous student's 'candies'. This ensures that students with higher scores receive more candies.

4.After the left-to-right pass, the program calculates the total number of candies distributed so far.

5.It then iterates through 'arr' from right to left. If a student's performance is better than the next student and they have fewer candies, their 'candies' value is updated to one more than the next student's 'candies'. This ensures that students with higher scores also receive more candies when moving from right to left.

6.After the right-to-left pass, the program calculates the total number of candies distributed.

7.The function returns the total number of candies distributed, and the result is written to the output file.

### Program
```python
#!/bin/python3

import math
import os
import random
import re
import sys

def candies(n, arr):
    # Write your code here
    # Initialize an array of the same length as 'arr' with all elements set to 1
    candies = [1] * n

    # Traverse 'arr' from left to right
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies[i] = candies[i - 1] + 1

    total_candies = candies[-1]

    # Traverse 'arr' from right to left and update 'candies'
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1

        total_candies += candies[i]

    return total_candies
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
```
#### Sample input & output
input
```
10
2
4
2
6
1
7
8
9
2
1
```
output
```
19
```
****
