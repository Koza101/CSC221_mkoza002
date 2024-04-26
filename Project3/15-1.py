# TIY 15 - 1

import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8-dark')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

#set chart title and label axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

# Set size of tick labels
ax.tick_params(labelsize=14)

plt.show()