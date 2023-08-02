#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3
x0 = np.arange(0, 11)

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
# Setup
plt.figure(figsize=(12, 12))
plt.rcParams.update({'font.size': 8})

# Line
plt.subplot(3, 2, 1)
plt.xlim(0, 10)
plt.plot(x0, y0, color='red')

# Scatter
plt.subplot(3, 2, 2)
plt.xlabel('Height (in)')
plt.ylabel('Weight (lbs)')
plt.title('Men\'s Height vs Weight')
plt.scatter(x1, y1, color='magenta', s=10)
plt.savefig('1-scatter.png')

# Scale
plt.subplot(3, 2, 3)

plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of C-14')
plt.xlim(0, 28650)
plt.yscale('log')
plt.plot(x2, y2, color='cornflowerblue')
plt.savefig('2-change_scale.png')

# Two
plt.subplot(3, 2, 4)
plt.xlim(0, 20000)
plt.ylim(0, 1)

plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of Radioactive Elements')
plt.plot(x3, y31, color='red', linestyle='--', label='C-14')
plt.plot(x3, y32, color='green', label='Ra-226')
plt.legend()
plt.savefig('3-two.png')

# Frequency
plt.subplot2grid((3, 2), (2, 0), colspan=2)
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.ylim(0, 30)
plt.xlim(0, 100)
plt.title('Project A')
plt.hist(student_grades, bins=np.arange(40, 110, 10), edgecolor='black')
plt.xticks(np.arange(0, 110, 10))
plt.savefig('4-frequency.png')

plt.subplots_adjust(left=0.23, right=0.77, bottom=0.50, top=0.92,
                    wspace=0.13, hspace=0.42)

plt.suptitle('All in One', fontsize=14, y=0.98)
plt.show()
