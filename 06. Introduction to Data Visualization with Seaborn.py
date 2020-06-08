#1.AxesSubplot
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#(1)Scatter Plot
sns.scatterplot(x="absences", y="G3", data=student_data, hue="location",hue_order=["Rural","Urban"])
#(2)Count plot
palette_colors = {"Rural": "green", "Urban": "blue"} #Create a dictionary mapping subgroup values to colors
sns.countplot(x="school",data=student_data, hue="location",palette=palette_colors) #location is the subgroups
#2.FacetGrid:relplot
#(1)Scatter Plot
sns.relplot(x="acceleration",y="mpg",
            data=mpg, style="origin",
            hue="origin",kind="scatter")
#(2)Line Plot
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin",dashes=False,
            markers=True)
#3.FacetGrid:catplot
#(1)count
sns.catplot(y="Internet usage",  data=survey_data,
            kind="count",col="Age Category")

#(2)bar
sns.catplot(x="study_time", y="G3",
            data=student_data,kind="bar",
            order=["<2 hours", 
                   "2 to 5 hours", 
                   "5 to 10 hours", 
                   ">10 hours"],
            ci=None)
#(3)box
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]
sns.catplot(x="study_time",y="G3",
            order=study_time_order,
            data=student_data,
            kind="box")
#(4)point plot
sns.catplot(x="famrel", y="absences",
			      data=student_data,
            kind="point",capsize=0.2,join=False)# Remove the lines joining the points
from numpy import median
sns.catplot(x="romantic", y="absences",
			      data=student_data,
            kind="point",hue="school",ci=None,
            estimator=median)# Plot the median number of absences instead of the mean
#4.Customizing
sns.set_style("whitegrid")
sns.set_palette(["#39A7D0","#36ADA4"])
sns.set_context("paper"/"notebook"/"talk"/"poster")
#(1)FacetGrid
g.fig.suptitle("Car Weight vs. Horsepower")
plt.xticks(rotation=90)
#(2)AxesSubplot
g.set_title( "Average MPG Over Time")
g.set(xlabel="Car Model Year",
        ylabel="Average MPG")
