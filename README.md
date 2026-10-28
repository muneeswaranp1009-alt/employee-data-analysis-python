
# Employee Data Analysis (Python)

An easy to follow data analysis project using Python and the pandas libraries to analyse employee data.
The program reads in a CSV dataset of employees, it will show you how many rows and columns there are, what the column names are and will show you some sample data. It will also give a basic summary of the data. If the required columns are present, it will calculate the average salaries per department.
## Features

Read in employee data from a CSV file
Shows how many rows and columns there are.
Shows what the column names are.
Shows the first 5 rows of data.
Basic summary of data.
If the correct columns are present, it will calculate the average monthly salary per department.
Handles missing files and empty datasets.
Exception handling so any unexpected errors are handled.

## Technologies Used
Python
Pandas
CSV File Handling
Exception Handling

## Project Hierarchy

employee-data-analysis-python/
Employee Data analyse(csv).py
employee_dataset.csv
README.md

## How It Works
The program uses the Pandas library to read in and analyse the employee data.

### 1. Read in the Data
Reads in the employee data from the CSV file using pd.read_csv().

### 2. See the Data Structure
Shows how many rows and columns there are, and shows what the column names are.

### 3. See Some Sample Data
Shows the first 5 rows using df.head(5).

### 4. Get Basic Summary
Using df.describe() it will show some descriptive statistics for the relevant numerical columns.

### 5. Salary Per Department
Groups the data by Department and calculates the mean value of Monthly_Salary. This will only work if both columns are present.

### 6. Error Handling
Handles any missing files, empty CSV files and any other unexpected errors.

## Installation
Ensure you have Python installed on your computer.
Install pandas:
pip install pandas

## How To Run
Clone the repo.
Ensure the python file and employee_dataset.csv are in the same directory.
Navigate to the project directory in your terminal.
Run:
python "Employee Data analyse(csv).py"
You will now see the analysis in your terminal.

## Key Concepts Used
Reading in CSV files using pandas
Seeing the structure of the dataset using shape and columns.
Seeing sample data using head().
Getting a descriptive summary using describe().
Grouping data using groupby().
Calculating averages using mean().
Handling errors with files.
Creating reusable functions in Python.

## What I Have Learned
I have practised working with structured datasets, seeing the employee data, getting summary statistics and basic grouping analysis using pandas.

## Future Improvements
Handle missing data.
Add number of employees per department.
Compare salary statistics between departments.
Create visualisations using Matplotlib/Seaborn.
Export the analysis into a CSV file.
Add more employee insights.

## Note
This is a learning project to practise using Python and pandas. The analysis will depend on what columns and data are present in the CSV file provided.

## Author
Created as part of my learning journey with Python and Data Analysis.
