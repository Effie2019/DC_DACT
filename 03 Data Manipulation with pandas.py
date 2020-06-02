#1.Inspect DataFrames and perform fundamental manipulations
#(1) Inspecting a DataFrame
.values: A two-dimensional NumPy array of values.
.columns: An index of columns: the column names.
.index: An index for the rows: either row numbers or row names.
#(2)Sorting rows
homelessness_reg_fam = homelessness.sort_values(['region','family_members'],ascending=[True,False]) 
#(3)Subsetting columns
ind_state = homelessness[["individuals","state"]]
#(4)Subsetting rows
fam_lt_1k_pac = homelessness[(homelessness['family_members']<1000) &
                             ( homelessness['region']=='Pacific')]
cities =['Moscow',"Saint Petersburg"]
print(temperatures[temperatures["city"].isin(cities)])

#2.Summary Statistics
#(1)agg.
def iqr(column):
  return column.quantile(0.75) - column.quantile(0.25)
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr,np.median]))
sales_stats = sales.groupby('type')["weekly_sales"].agg([np.min, np.max, np.mean,np.median])
#(2)Cumulative statistics
sales_1_1["weekly_sales"].cumsum()
sales_1_1["weekly_sales"].cummax()
#(3)Dropping duplicates
sales.drop_duplicates(subset=["store","department"])
#(3)Count the number of each department number and sort
departments["department_num"].value_counts(sort=True, normalize=True)
#(4)Calculations with .groupby()
sales.groupby("type")["weekly_sales"].sum()
#(5)Pivot Table
sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True)
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c",index=["country","city"],columns="year")
#3 Slicing and indexing
#(1)index
temperatures.set_index("city")
temperatures.set_index(["country","city"])
temperatures_ind.reset_index()# Reset the index, keeping its contents
temperatures_ind.reset_index(drop=True)# Reset the index, dropping its contents
temperatures_ind.loc[['Moscow',"Saint Petersburg"]]
#(2)Setting multi-level indexs
temperatures_ind = temperatures.set_index(["country","city"])
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]# List of tuples
print(temperatures_ind.loc[rows_to_keep])
#(3)Sort the index 
temperatures_srt = temperatures_ind.sort_index()
#(4)Slicing rows
# Subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan":"Russia"])
# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[("Pakistan", "Lahore"):("Russia", "Moscow")])
#(5)Slicing columns
# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:,"date":"date to avg_temp_c"])
# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq","Baghdad"),"date":"date to avg_temp_c"])
# (6).iloc
# Use slicing in both directions at once
print(temperatures.iloc[0:5,2:4])

#4.Missing Value
print(avocados_2016.isna())# Check individual values for missing values
print(avocados_2016.isna().any())# Check each column for missing values
avocados_2016.isna().sum().plot(kind="bar")# Bar plot of missing values by variable
