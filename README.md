# python Fundamentals - Simple Interest Calculator

## project Description
In this project yo will be accessing a simple interest calculator. This calculator allows the user to input their name, interest rate as a percentage, as well as principal amoint and payment length. Once the user enters the proper values and information the calculator will print your name as well as pricipal and interest summed together with its break down of inputs.

## Simple Interest Formula
Simple Interest = (Principal * Rate * Time) / 100
The principal is the amount or value of an item. Example: Car, loan etc.
Rate is the interest rate percentage given
Time is the amount of months-years taken to pay off

## Python Concepts Used
input() Collects information.
float() Converts input into decimal numbers.
while loops Repeats questions until valid information is entered.
if/else Checks whether information meets requirements.
try/except Handles invalid numeric input.
strip() Removes extra spaces.
title() Formats the user's name.
len() Counts characters in the name.

## How to Run the Program
1. Open Visual Studio Code.
2. Open the project folder.
3. Open the terminal.
4. Enter the command below.
simple_interest_calculator.py

## Example Calculation 
Principal: $50000
Interest rate: 9.5%
Time: 6 years
(1000 * 5 * 2) / 100 = 100
the simple interesr is $100, and the total amount is $1,100.

## Testing and Edge Cases
Test                                 Input      Expected behavior
Valid Principal                      1000       Accepted
Letters instead of numbers           hello      Error or retry
Negative principal                   -500       Rejected
Negative interest                    -5         Rejected
Zero interest                         0         Accepted
Empty name                           Blank      Error and retry

## Conclusion
This program allows the user to input their values which consists of principal amount, interest rate percentage, name and time as how long it the payments will last. It will complete simple math to give you an interest amount out come and add the interest to your principal.