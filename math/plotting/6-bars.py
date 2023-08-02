#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))
Farrah = fruit[:, 0]
Fred = fruit[:, 1]
Felicia = fruit[:, 2]
x_axis = np.arange(len(Farrah))
bar_width = 0.5

fig, ax = plt.subplots(figsize=(7, 7))
plt.yticks(np.arange(0, 81, 10))
plt.ylim(0, 80)
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')

cumulative_Farrah = np.cumsum(Farrah)
cumulative_Fred = np.cumsum(Fred)
cumulative_Felicia = np.cumsum(Felicia)

ax.bar('Farrah', Farrah[0], bar_width, label='apples', color='red')
ax.bar('Farrah', Farrah[1], bar_width, label='bananas', color='yellow',
       bottom=cumulative_Farrah[0])
ax.bar('Farrah', Farrah[2], bar_width, label='oranges', color='#ff8000',
       bottom=cumulative_Farrah[1])
ax.bar('Farrah', Farrah[3], bar_width, label='peaches', color='#ffe5b4',
       bottom=cumulative_Farrah[2])

ax.bar('Fred', Fred[0], bar_width, color='red')
ax.bar('Fred', Fred[1], bar_width, color='yellow',
       bottom=cumulative_Fred[0])
ax.bar('Fred', Fred[2], bar_width, color='#ff8000',
       bottom=cumulative_Fred[1])
ax.bar('Fred', Fred[3], bar_width, color='#ffe5b4',
       bottom=cumulative_Fred[2])

ax.bar('Felicia', Felicia[0], bar_width, color='red')
ax.bar('Felicia', Felicia[1], bar_width, color='yellow',
       bottom=cumulative_Felicia[0])
ax.bar('Felicia', Felicia[2], bar_width, color='#ff8000',
       bottom=cumulative_Felicia[1])
ax.bar('Felicia', Felicia[3], bar_width, color='#ffe5b4',
       bottom=cumulative_Felicia[2])
ax.legend()
plt.show()
