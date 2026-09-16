import matplotlib.pyplot as plt
months = [1, 2, 3, 4]
product_a = [200, 250, 300, 350]
product_b = [180, 220, 260, 310]
fig, ax = plt.subplots()
ax.plot(
    months,
    product_a,
    color="green",
    linestyle="-",
    marker="o",
    label="Product A"
)
ax.plot(
    months,
    product_b,
    color="red",
    linestyle="--",
    marker="s",
    label="Product B"
)
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.set_title("Sales Comparison of Product A and Product B")
ax.legend()
plt.show()


# =========================================================
# Part 2: Subplots with Shared X-Axis
# =========================================================

fig, ax = plt.subplots(2, 1, sharex=True)
ax[0].plot(
    months,
    product_a,
    color="green",
    linestyle="-",
    marker="o"
)
ax[0].set_ylabel("Sales")
ax[0].set_title("Product A Sales")
ax[1].plot(
    months,
    product_b,
    color="red",
    linestyle="--",
    marker="s"
)
ax[1].set_xlabel("Month")
ax[1].set_ylabel("Sales")
ax[1].set_title("Product B Sales")
plt.tight_layout()
plt.show()