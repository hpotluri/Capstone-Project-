# Driving Change: Electric Vehicles in Modern Transportation
## Project Overview
This project aims to predict electric vehicle (EV) registrations across different states using historical registration data from 2016 to 2022. The focus is on utilizing various statistical and machine learning models to understand trends and make predictions for future years. This repository contains the data, Jupyter notebooks, and Python scripts used for the analysis and modeling.

## Installation
Before running the Jupyter notebooks, you will need to install the necessary Python packages. You can do this by running the following command in your terminal:

```bash
pip install pandas numpy matplotlib scikit-learn statsmodels
```

This will install:

Pandas: For data manipulation and analysis.
NumPy: For numerical operations.
Matplotlib: For creating static, interactive, and animated visualizations in Python.
Scikit-Learn: For machine learning and predictive data analysis.
Statsmodels: For statistical modeling, testing, and analysis.

## Project Structure
The repository is structured as follows:

data/: This folder contains the CSV files for each year detailing the EV registrations by state.
notebooks/: This directory contains Jupyter notebooks that demonstrate the data preprocessing, exploratory data analysis, and each step of the modeling process.
scripts/: This directory contains Python scripts for data cleaning, model training, and prediction.
README.md: Provides an overview and instructions for the project.

## How to Run
1.Clone the repository to your local machine.
2.Ensure you have Jupyter Notebook or JupyterLab installed. If not, you can install it via:
```bash
pip install notebook
```
3.Navigate to the notebooks/ directory and launch Jupyter Notebook:
```bash
cd notebooks
jupyter notebook
```
4.Open the desired notebook and run the cells sequentially to replicate the analysis and modeling steps.

## Key Components
Data Cleaning: Consolidates and cleans data across multiple CSV files to create a coherent dataset for analysis.
Exploratory Data Analysis (EDA): Analyzes trends and patterns in the data to inform the modeling process.
Model Training: Implements several forecasting models, including ARIMA and SARIMA, to predict future EV registrations.
Evaluation: Assesses the performance of each model using metrics such as R² and RMSE.

## Model Result 
### R² Scores for Each State

| State                | R² Score   |
|----------------------|------------|
| Alabama              | -384.63    |
| Alaska               | -22.68     |
| Arizona              | -203.64    |
| Arkansas             | -1480.54   |
| California           | -57.98     |
| Colorado             | -139.18    |
| Connecticut          | -124.88    |
| Delaware             | -1232.70   |
| District of Columbia | -326.06    |
| Florida              | -667.68    |
| Georgia              | -161.89    |
| Hawaii               | -44.19     |
| Idaho                | -134.72    |
| Illinois             | -220.14    |
| Indiana              | -270.79    |
| Iowa                 | -358.58    |
| Kansas               | -91.74     |
| Kentucky             | -610.73    |
| Louisiana            | -403.26    |
| Maine                | -251.03    |
| Maryland             | -457.10    |
| Massachusetts        | -172.94    |
| Michigan             | -718.42    |
| Minnesota            | -288.49    |
| Mississippi          | -297.24    |
| Missouri             | -219.08    |
| Montana              | -535.50    |
| Nebraska             | -159.40    |
| Nevada               | -385.92    |
| New Hampshire        | -407.64    |
| New Jersey           | -428.08    |
| New Mexico           | -452.61    |
| New York             | -240.84    |
| North Carolina       | -374.57    |
| North Dakota         | -10.60     |
| Ohio                 | -298.72    |
| Oklahoma             | -212.85    |
| Oregon               | -74.02     |
| Pennsylvania         | -606.93    |
| Rhode Island         | -753.72    |
| South Carolina       | -546.25    |
| South Dakota         | 0.00       |
| Tennessee            | -2591.48   |
| Texas                | -535.73    |
| Utah                 | -217.24    |
| Vermont              | -43.25     |
| Virginia             | -266.75    |
| Washington           | -47.71     |
| West Virginia        | 0.00       |
| Wisconsin            | -2451.18   |
| Wyoming              | 0.00       |

### Model Results for ARIMA Predictions

| State                | Best ARIMA Order | AIC                   | BIC                   |
|----------------------|------------------|-----------------------|-----------------------|
| Alabama              | (3, 1, 2)        | 12.0                  | 9.6566                |
| Alaska               | (3, 3, 1)        | 32.41                 | 27.90                 |
| Arizona              | (2, 3, 0)        | 6.0                   | 3.296                 |
| Arkansas             | (3, 3, 0)        | 8.0                   | 4.394                 |
| California           | (2, 3, 2)        | 10.0                  | 5.493                 |
| Colorado             | (0, 3, 0)        | 63.93                 | 63.03                 |
| Connecticut          | (2, 3, 0)        | 6.0                   | 3.296                 |
| Delaware             | (2, 3, 0)        | 33.59                 | 30.88                 |
| District of Columbia | (3, 3, 0)        | 8.0                   | 4.394                 |
| Florida              | (3, 1, 2)        | 12.0                  | 9.6566                |
| Georgia              | (0, 3, 0)        | 60.90                 | 60.00                 |
| Hawaii               | (1, 3, 0)        | 54.95                 | 53.15                 |
| Idaho                | (1, 3, 0)        | 4.0                   | 2.197                 |
| Illinois             | (2, 1, 0)        | 6.0                   | 4.828                 |
| Indiana              | (2, 3, 0)        | 39.79                 | 37.09                 |
| Iowa                 | (2, 3, 0)        | 36.55                 | 33.84                 |
| Kansas               | (2, 3, 0)        | 6.0                   | 3.296                 |
| Kentucky             | (3, 3, 1)        | 10.0                  | 5.493                 |
| Louisiana            | (2, 3, 0)        | 38.40                 | 35.70                 |
| Maine                | (2, 3, 0)        | 37.76                 | 35.05                 |
| Maryland             | (3, 2, 0)        | 8.0                   | 5.545                 |
| Massachusetts        | (2, 1, 0)        | 6.0                   | 4.828                 |
| Michigan             | (2, 0, 0)        | 8.0                   | 7.167                 |
| Minnesota            | (3, 3, 0)        | 8.0                   | 4.394                 |
| Mississippi          | (2, 3, 0)        | 36.16                 | 33.46                 |
| Missouri             | (3, 1, 3)        | 14.0                  | 11.27                 |
| Montana              | (2, 3, 0)        | 35.73                 | 33.03                 |
| Nebraska             | (2, 3, 1)        | 8.0                   | 4.394                 |
| Nevada               | (0, 3, 0)        | 57.69                 | 56.79                 |
| New Hampshire        | (3, 2, 1)        | 10.0                  | 6.931                 |
| New Jersey           | (3, 2, 0)        | 8.0                   | 5.545                 |
| New Mexico           | (2, 3, 0)        | 36.22                 | 33.52                 |
| New York             | (2, 1, 2)        | 10.0                  | 8.047                 |
| North Carolina       | (2, 1, 2)        | 10.0                  | 8.047                 |
| North Dakota         | (1, 3, 0)        | 41.0                  | 39.19                 |
| Ohio                 | (0, 3, 0)        | 55.53                 | 54.63                 |
| Oklahoma             | (0, 3, 1)        | 60.56                 | 58.76                 |
| Oregon               | (0, 3, 0)        | 60.40                 | 59.50                 |
| Pennsylvania         | (2, 3, 1)        | 8.0                   | 4.394                 |
| Rhode Island         | (2, 3, 0)        | 33.30                 | 30.59                 |
| South Carolina       | (2, 3, 0)        | 40.44                 | 37.74                 |
| South Dakota         | (2, 3, 0)        | 30.97                 | 28.27                 |
| Tennessee            | (0, 3, 0)        | 54.83                 | 53.93                 |
| Texas                | (2, 3, 2)        | 10.0                  | 5.493                 |
| Utah                 | (2, 1, 0)        | 6.0                   | 4.828                 |
| Vermont              | (3, 3, 0)        | 8.0                   | 4.394                 |
| Virginia             | (2, 3, 2)        | 10.0                  | 5.493                 |
| Washington           | (3, 2, 2)        | 12.0                  | 8.318                 |
| West Virginia        | (2, 3, 0)        | 34.23                 | 31.53                 |
| Wisconsin            | (0, 3, 0)        | 51.69                 | 50.79                 |
| Wyoming              | (2, 3, 0)        | 34.72                 | 32.02                 |
