#1.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#(1)Scatter Plot
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location",
                hue_order=["Rural","Urban"])
#(2)Count plot
palette_colors = {"Rural": "green", "Urban": "blue"} #Create a dictionary mapping subgroup values to colors
sns.countplot(x="school",
              data=student_data,
              hue="location",
              palette=palette_colors) #location is the subgroups
plt.show()
