import matplotlib.pyplot as plt
list_days=["Monday", "Tuesday", "Wednesday", "Thursday"]
list_visitors=[120,150,130,180]
plt.plot(list_days, list_visitors)
plt.plot(list_days, list_visitors, marker='o', color="blue", linestyle='--')
plt.xlabel("days")
plt.ylabel("number of visitors")
plt.figure(figsize=(8,4))
plt.show()