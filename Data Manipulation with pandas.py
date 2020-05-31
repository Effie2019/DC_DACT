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
#.


