# Rate Calculation System

[![CircleCI](https://circleci.com/gh/dimivas/rate_calculation_system/tree/master.svg?style=shield)](https://circleci.com/gh/dimivas/rate_calculation_system/tree/master)

## Overview
This application consists of three conceptual parts: parse arguments, import csv and calculate loan. The modules that implement the Rate Calculation system are the following:

lenders_inventory : Creates a UUID for each lender and stores the mapping in a dictionary. Given a UUID the module can resolve the lender.  

loan_calculator : Calculates the loan rate, the monthly  and total repayment.

market_importer : Imports the market file.

validators : A set or rules imposed on the arguments and the market file. 

## Requirements
- python3
- numpy 1.10.0 or later

## Docker image

Give it a try:
```
docker run -i -t dimivas/rate_calculation_system
```
