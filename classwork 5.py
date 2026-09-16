import matplotlib.pyplot as plt
plt.style.use("ggplot")
weeks=[1,2,3,4]
engagement=[120,180,260,340]
plt.plot(weeks,engagement,linewidth=2,color="green",alpha=0.8)
plt.title("CAMPAIGN ENGAGEMENT GROWTH")
plt.xlabel("weeks")
plt.ylabel("engagement")
plt.grid(True)
plt.tight_layout()
plt.show()