# Rate Calculation System

This application consists of three conceptual parts: parse arguments, import csv and calculate loan. The modules that implement the Rate Calculation system are the following:

lenders_inventory : Creates a UUID for each lender and stores the mapping in a dictionary. Given a UUID the module can resolve the lender.  

loan_calculator : Calculates the loan rate, the monthly  and total repayment.

market_importer : Imports the market file.

validators : A set or rules imposed on the arguments and the market file. 

This application is implemented with Python3 and uses numpy package for the calculations.


A docker image is available on DockerHub (dimivas/rate_calculation_system).
