import numpy as np
import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

print("x: ", end = '')
for i in x:
    print(i, end = ' ')
print()
print("y1: ", end = '')
for i in y1:
    print(i, end = ' ')
print()
print("y2: ", end = '')
for i in y2:
    print(i, end = ' ')
print()

plt.figure(figsize = (4, 3), dpi = 160)
plt.plot(x, y1, label = "sin")
plt.plot(x, y2, label = "cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend()
plt.savefig("python_graph.png")
