#1Stat.
#(1)Pmf
age = gss['age']
pmf_age = Pmf(age)
pmf_age.bar()
#(2)Cdf
income = gss['realinc']
cdf_income = Cdf(income)
cdf_income.plot()
income = gss['realinc']
#(3)Multiple CDFs
Cdf(income[high]).plot(label='High school')
Cdf(income[assc]).plot(label='Associate')
Cdf(income[bach]).plot(label='Bachelor')
#(4)Compare  with normal distribution
xs = np.linspace(2, 5.5)
ys = dist.cdf(xs) #Evaluate the normal distribution function 
ys = dist.pdf(xs)
plt.plot(xs, ys, color='gray') # Plot of the Cdf/pdf of normal dist.
Cdf(log_income).plot() #Plot of Cdf
sns.kdeplot(log_income) #Plot of Pdf
#(5)CORR
columns = ['AGE', 'INCOME2',  '_VEGESU1']
subset =brfss[columns]
print(subset.corr())# Compute the correlation matrix

#2.Other Plots
#(1)Jittering in scatter plot
age = brfss['AGE'] + np.random.normal(0,2.5,size=len(brfss)) # Add jittering to age, since age is categorial data,
weight = brfss['WTKG3']
plt.plot(age,weight,'o',alpha=0.2,markersize=5)
#(2)Violin Plot
data = brfss.dropna(subset=['INCOME2', 'HTM4'])
sns.violinplot(x="INCOME2", y="HTM4", data=data, inner=None)
sns.despine(left=True, bottom=True)# Remove unneeded lines and label axes

# 3.Regression
from scipy.stats import linregress
import statsmodels.formula.api as smf
#(1)Extract the variables
subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
xs = subset['INCOME2']
ys = subset['_VEGESU1']
#(2)linear regression1
res = linregress(xs,ys)
fx = np.array([xs.min(),xs.max()])
fy = res.intercept+res.slope*fx
plt.plot(fx, fy, '-', alpha=0.7)
#(3)linear regression2
results = smf.ols('_VEGESU1 ~ INCOME2', data =brfss).fit()
print(results.params)
#(3)Multiple Regression
results =smf.ols('realinc ~ educ+educ2+age+age2',data=gss).fit()
results = smf.logit('grass~age+age2+educ+educ2+C(sex)',data=gss).fit()
#(4)Prediction
df = pd.DataFrame() # Make the DataFrame
df['educ'] = np.linspace(0,20)
df['age'] = 30
df['educ2'] = df['educ']**2
df['age2'] = df['age']**2
grouped = gss.groupby('educ')
mean_income_by_educ = grouped['realinc'].mean()
plt.plot(mean_income_by_educ,'o',alpha=0.5) # Original Plot 
pred = results.predict(df)
plt.plot(df['educ'], pred, '-', label='Age 30') # Prediction Plot
