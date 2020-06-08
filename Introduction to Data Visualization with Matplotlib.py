#1.Introduction to Matplotlib
#(1)Creat the plot
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])
#(2)Customizing the plot
ax.set_xlabel("Time (months)")
ax.set_ylabel("Precipitation (inches)")
ax.set_title( "Weather patterns in Austin and Seattle")
#(3)Small multiples
fig, ax = plt.subplots(2, 1, sharey=True)
# Plot Seattle precipitation data in the top axes
ax[0].plot(seattle_weather['MONTH'], seattle_weather[ "MLY-PRCP-NORMAL"], color = 'b')
ax[0].plot(seattle_weather['MONTH'], seattle_weather["MLY-PRCP-25PCTL"], color = 'b', linestyle = '--')
ax[0].plot(seattle_weather['MONTH'], seattle_weather["MLY-PRCP-75PCTL"],color = 'b', linestyle = '--')
# Plot Austin precipitation data in the bottom axes
ax[1].plot(austin_weather['MONTH'], austin_weather[ "MLY-PRCP-NORMAL"], color = 'r')
ax[1].plot(austin_weather['MONTH'], austin_weather["MLY-PRCP-25PCTL"] ,color = 'r', linestyle = '--')
ax[1].plot(austin_weather['MONTH'], austin_weather["MLY-PRCP-75PCTL"],color = 'r', linestyle = '--')

#2.time-series
