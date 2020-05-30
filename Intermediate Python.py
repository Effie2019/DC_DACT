#1.Basic plots with Matplotlib
Line Plot
Scatter Plot
# Put the x-axis on a logarithmic scale
plt.xscale('log')

Histogram Plot
# Build histogram with 5 bins
plt.hist(life_exp,bins=5)
# Show and clean up plot
plt.show()
plt.clf()

plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)
plt.yticks([0,1,2], ["one","two","three"])
plt.text(1550, 71, 'India')
plt.grid(True)
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2,c = col,alpha=0.8)

#2.Dictionaries & Pandas
