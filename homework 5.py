import matplotlib.pyplot as plt
import numpy as np
plt.style.use("ggplot")
months=[1,2,3,4]
sales_2024=[200,260,300,380]
sales_2025=[220,280,330,420]
plt.title("SALES COMPARISON LINE CHART")
plt.figure(1)
plt.xlabel("sales_2024")
plt.ylabel("sales_2025")
plt.plot(months,sales_2024,alpha=0.7)
plt.plot(months,sales_2025,alpha=0.7)
plt.grid(True)
plt.savefig("sales_report.png",dpi=200)
np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)
sales = np.random.randint(100, 1000, 50)
plt.figure(2)
plt.scatter(x, y, c=sales, cmap='viridis', s=80)
plt.colorbar(label='Sales Intensity')
plt.title("Sales Intensity Distribution")
plt.xlabel("X")
plt.ylabel("Y")
x=[1,2,3,4,5]
y=[20,30,50,60,70]
plt.figure(3,figsize=(8,4))
plt.plot(x,y)
plt.tight_layout()
plt.savefig("report_charts.pdf",dpi=300)
plt.savefig("report_charts.svg",dpi=300)
plt.show()