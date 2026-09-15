import matplotlib.pyplot as plt
sales_data=[10,20,20,30,40,40,50]
plt.figure(1)
plt.title("SALES DISTRIBUTION")
plt.hist(sales_data,bins=6)
plt.show()
labels=["product a","product b","product c"]
sizes=[40,35,25]
explode=(0.3,0,0.1)
plt.figure(2)
plt.title("MARKET SHARE ANALYSIS")
plt.pie(sizes,labels=labels,explode=explode)
salary=[20000,25000,30000,35000,80000]
plt.figure(3)
plt.title("EMPLOYEE SALARY DISTRIBUTION")
plt.boxplot(salary)
plt.show()
x=[1,2,3]
y=[10,20,30]
error=[2,3,4]
plt.figure(4)
plt.title("MEASUREMENT WITH ERROR RANGE")
plt.errorbar(x,y,xerr=error,fmt="o")
plt.show()