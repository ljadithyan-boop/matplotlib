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

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]   # your actual x-axis values
product_a = [200, 250, 300, 350]
product_b = [180, 220, 260, 310]

fig, ax = plt.subplots(2, 1, sharex=True)
ax[0].plot(months, product_a)
ax[1].plot(months, product_b)

plt.xlabel("months")
plt.ylabel("sales")
plt.show()

