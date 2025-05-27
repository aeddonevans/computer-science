# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Problem Set 1b
# Name: Aeddon Evans
# Time Spent: 10 Minutes

# User inputs and definitions
yearlySalary = float(input("Enter your yearly salary: "))
percentageSaved = float(input("Enter the percentage of your salary you save each month, as a decimal: "))
homeCost = float(input("Enter the cost of your dreamhome: "))
raisePercentage = float(input("Enter your semi annual raise ammount, as a decimal:"))

downPaymentPercent = 0.25
annualReturn = 0.05

totalSaved = 0.0
totalMonths = 0

# Calculations based upon user inputs
monthlySavings = (yearlySalary * percentageSaved)/12
monthlyReturn = 1 + annualReturn/12
semiAnnualRaise = 1 + raisePercentage
necessarySavings = homeCost * downPaymentPercent

while totalSaved <= necessarySavings:
    totalSaved *= monthlyReturn
    totalSaved += monthlySavings
    totalMonths += 1
    
    if ((totalMonths % 6) == 0): 
        yearlySalary *= semiAnnualRaise
        monthlySavings = (yearlySalary * percentageSaved)/12
        
print(f'You will need to save for {totalMonths} months.')