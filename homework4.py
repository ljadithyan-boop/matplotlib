import matplotlib.pyplot as plt
import datetime
dates=[datetime.date(2025,1,d)for d in range(1,6)]
values=[100,120,150,180,220]
plt.figure(1)
plt.title("DATE BASED SALES TREND")
plt.xlabel("dates")
plt.ylabel("values")
plt.plot(dates,values)
plt.show()
x=[1,2,3,4]
sales=[100,200,300,400]
profit=[20,50,90,150]
plt.figure(2)
plt.title("SALES VS PROFIT(TWIN Y AXIS)")
fig,ax1=plt.subplots()
ax2=ax1.twinx()
ax1.plot(x,sales)
ax2.plot(x,profit)
plt.show()
x=[1,2,3,4]
y=[10,100,1000,10000]
plt.figure(3)
plt.title("EXPONENTIAL GROWTH ANALYSIS")
plt.plot(x,y)
plt.yscale("log")
plt.show()
x=[1,2,3,4]
product_a=[30,40,50,60]
product_b=[20,30,40,50]
plt.figure(4)
plt.title("STACKED SALES CONTRIBUTION")
plt.xlabel("product_a")
plt.ylabel("product_b")
plt.stackplot(x,product_a,product_b)
plt.show()
