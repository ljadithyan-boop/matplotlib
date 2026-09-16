import matplotlib.pyplot as plt
import numpy as np
days=[1,2,3,4,5]
sales=np.array([100,150,np.nan,200,250])
highest_sales=np.nanmax(sales)
highest_index=np.nanargmax(sales)
plt.title("DAILY SALES REPORT")
plt.xlabel("day")
plt.ylabel("sales amount")
plt.annotate("Highest Sale",xy=(5,250),xytext=(4,200),arrowprops=dict(arrowstyle="->"))
plt.plot(days,sales,marker="o",color="red")
plt.plot(days[highest_index],highest_sales,'ro',markersize=15)
plt.show()