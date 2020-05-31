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
my_dict = {
   "key1":"value1",
   "key2":"value2",
}
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])
# Add italy to europe
europe['italy']='rome'
del(europe['australia'])

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }
# Create sub-dictionary data
data={'capital':'rome','population':59.83}

# Add data to europe under key 'italy'
europe['italy']=data
#3.logic, Control Flow and Filtering
#(1)Boolean Operators with Numpy
np.logical_and(my_house > 13, 
               your_house < 15)
#(2)if, elif, else
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")
#(3)Filtering pandas DataFrames
cpc=cars['cars_per_cap']
between=np.logical_and(cpc > 100,cpc< 500)
medium=cars[between]
