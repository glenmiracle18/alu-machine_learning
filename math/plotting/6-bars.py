#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))


people = (
    'Farah', 'Fred', 'Felicia',
)

colors = {
    'apples': 'red',
    'bananas': 'yellow',
    'oranges': '#ff8000',
    'peaches': '#ffe5b4',
}

fig, ax = plt.subplots( figsize=(10, 8))
bottom = np.zeros(3)  # [0., 0., 0.]
width = 0.5

for i in range(4):
    ax.bar(people, fruit[i], bottom=bottom, width=width, label=list(colors.keys())[i], color=list(colors.values())[i])
    bottom += fruit[i]

ax.set_title("Number of penguins with above average body mass")
ax.set_ylabel("Quality of Fruit")
ax.set_yticks(range(0, 81, 10))
ax.legend()

plt.show()
