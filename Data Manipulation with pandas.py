#1.Inspect DataFrames and perform fundamental manipulations
#(1) Inspecting a DataFrame
.values: A two-dimensional NumPy array of values.
.columns: An index of columns: the column names.
.index: An index for the rows: either row numbers or row names.
#(2)Sorting rows
homelessness_reg_fam = homelessness.sort_values(['region','family_members'],ascending=[True,False])  
#(3)Subsetting rows
fam_lt_1k_pac = homelessness[(homelessness['family_members']<1000) &
                             ( homelessness['region']=='Pacific')]
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]
#2.Summary Statistics
import numpy as np
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr,np.median]))
Cumulative statistics
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()

# Count the number of each department number and sort
dept_counts_sorted = departments["department_num"].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = departments["department_num"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)

# Import NumPy with the alias np
import numpy as np
unemp_fuel_stats = sales.groupby('type')["unemployment","fuel_price_usd_per_l"].agg([np.min, np.max, np.mean,np.median])
# Print unemp_fuel_stats
print(unemp_fuel_stats)

#3
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop=True))
temperatures_ind.loc[['Moscow',"Saint Petersburg"]]

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country","city"])
# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]
# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()
# Subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan":"Russia"])
# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc["Lahore":"Moscow"])
# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[("Pakistan", "Lahore"):("Russia", "Moscow")])
# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq","Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:,"date":"date to avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq","Baghdad"),"date":"date to avg_temp_c"])

#4.
