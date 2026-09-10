import matplotlib.pyplot as plt
months=["January", "February", "March", "April"]
product_a=[200,250,300,350]
product_b=[180,220,260,310]
fig, ax = plt.subplots()
ax.plot(months,product_a,marker="o",color="green",linestyle="-")
ax.plot(months,product_b,marker="s",color="red",linestyle="--")
plt.xlabel("month")
plt.ylabel("sales")
plt.plot()
plt.show()


print("---------part2----------")
import matplotlib.pyplot as plt
fig,ax=plt.subplots(2,1,sharex=True)
plt.xlabel("month")
plt.ylabel("sales")
plt.axes[0].plot(["month"], [product_a])
plt.axes[1].plot(["month"], [product_b])
plt.show()


