# Netflix Analysis Numpy Pandas
This project performs a basic exploratory data analysis (EDA) on the Netflix dataset using Python, Pandas, and NumPy. It demonstrates how to clean, transform, and analyze data to extract insights about content trends, top genres, popular countries, and content growth over time.
The dataset used is: netflix_titles.xlsx
It contains metadata for Netflix content including titles, genres, countries, release year, date added, type (Movie or TV Show), duration, and more.

# Technologies Used
Python 3.x, 
 Pandas, 
 NumPy

# Key Operations Performed
# 1. Data Loading & Overview
Loaded the Excel file with pandas.read_excel()
Checked shape and columns
Identified missing values

# 2. Data Cleaning
Filled missing values in key columns (director, cast, country, rating) with placeholders
Converted date_added to datetime format
Extracted year_added from date_added
Separated the duration into duration_int and duration_unit

# 3. Genre Analysis
Split the listed_in column (which contains genres)
Flattened the nested list of genres using np.hstack()
Counted occurrences of each genre

# 4. Country Analysis
Counted the number of shows/movies per country
Displayed the top 10 countries with the most content
Yearly Content Addition
Counted how many titles were added each year

# 5. Movies vs TV Shows Trend
Grouped data by year_added and type
Created a pivot to show how many movies and TV shows were added each year

# How to Run
Clone the repository or download the .ipynb file.
Place the netflix_titles.xlsx file in the same directory.
Install dependencies if needed
