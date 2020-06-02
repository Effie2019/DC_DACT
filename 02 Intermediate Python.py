#1.Basic plots with Matplotlib
#(1)Line Plot
#(2)Scatter Plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2,c = col,alpha=0.8)
#(3)Histogram Plot
plt.hist(life_exp,bins=5)
#(4)Customize your plot
plt.xscale('log')# Put the x-axis on a logarithmic scale
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)
plt.yticks([0,1,2], ["one","two","three"])
plt.text(1550, 71, 'India')
plt.grid(True)
#(5)Show and clean up plot
plt.show()
plt.clf()

#2.Dictionaries & Pandas
#(1)Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } } #Dictionary of dictionaries
#(2)Print out all the keys 
print(europe.keys())
#(3)Print out a specic value 
print(europe['norway'])
#(4)Add new key and value to a dictionary
europe['italy']='rome'
data={'capital':'rome','population':59.83}# Create sub-dictionary data
#(5)Delete a key and value from a dictionary
del(europe['australia'])

#3.logic, Control Flow and Filtering
#(1)Boolean Operators with Numpy
np.logical_and(my_house > 13, your_house < 15)
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

#4.Loops
#(1)While Loop
#(2)For Loop
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Change for loop to use enumerate() and update print()
for index, y in enumerate(areas) :
    print("room" + str(index)+":" +str(y))
#Loop over Numpy array
for x in my_array :
   for x in np.nditer(my_array) :#2d
      for lab, row in cars.iterrows():
    print(lab)
    print(row)
      
      cars["COUNTRY"]=cars["country"].apply(str.upper)
      
