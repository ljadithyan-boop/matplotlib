import matplotlib.pyplot as plt
days=[1,2,3,4,5]
sales=[100,120,140,130,160]
plt.figure(1)
plt.title("SALES TREND")
plt.xlabel("day")
plt.ylabel("sales")
plt.plot(days,sales)
categories=["Electronics", "Clothing", "Grocery"]
values = [50, 30, 40]
plt.figure(2)
plt.title("CATEGORY WISED SALES")
plt.barh(categories,values)
age=[22,25,30,35,40]
purchase=[200,400,600,650,800]
plt.figure(3)
plt.title("CUSTOMER AGE VS PURCHASE AMOUNT")
plt.scatter(age,purchase)
plt.show()
