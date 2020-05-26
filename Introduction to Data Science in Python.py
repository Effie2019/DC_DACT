# From matplotlib, import pyplot under the alias plt
from matplotlib import pyplot as plt

# LINE PLOT
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')
# Make the legend display
plt.legend()
#Adding floating text
plt.text(2.5, 80,"Missing June data")
# Color
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix", color="DarkCyan")
# Linestyle to dotted (':'), dashed('--'), or no line ('').
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles", linestyle=':')
# Add markers as circle ('o'), diamond('d'), or square ('s').
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia", marker='s')
#Styles
'fivethirtyeight' - Based on the color scheme of the popular website
'grayscale' - Great for when you don't have a color printer!
'seaborn' - Based on another Python visualization library
'classic'- The default color scheme for Matplotlib
# Display plot
plt.show()

#SCATTER PLOT
# Change the transparency to 0.1
plt.scatter(cellphone.x, cellphone.y,
           color='red',
           marker='s',
           alpha=0.1)
# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

#BAR CHART
plt.bar(x,y,label,yerr,bottom)
# Add error bars
plt.bar(hours.officer, hours.avg_hours_worked, yerr=hours.std_hours_worked)
# Stacked Bar plor
plt.bar(hours.officer,hours.field_work,bottom=hours.desk_work,label="Field Work")
# Add a legend
plt.legend()

#HISTGRAM
plt.hist(gravel.radius,
         bins=40,
         range=(2, 8),
         density=1)
# Display the plot
plt.show()
