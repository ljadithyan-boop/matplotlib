import matplotlib.pyplot as plt
months=[1,2,3,4]
product_a=[100,150,200,250]
product_b=[120,170,210,260]
plt.title("MONTHLY PRODUCT SALES COMPARISON",fontsize=20)
plt.xlabel("months",fontsize=15)
plt.ylabel("sales(units)",fontsize=15)
plt.legend(product_a,product_b)
plt.plot(product_a,product_b)
plt.grid(True)
plt.ylim(0,300)
plt.xticks([1,2,3,4],["jan","feb","mar","apr"])
plt.show()