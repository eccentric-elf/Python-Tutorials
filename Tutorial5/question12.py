import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 40]
y2 = [5, 15, 20, 25, 35]   
y3 = [2, 10, 18, 28, 38]  


plt.plot(x, y1, marker='o', linestyle='-', color='red', label="Line 1")
plt.plot(x, y2, marker='s', linestyle='--', color='blue', label="Line 2")
plt.plot(x, y3, marker='^', linestyle='-.', color='green', label="Line 3")

plt.xlabel("X-Axis Label") 
plt.ylabel("Y-Axis Label")
plt.title("Multiple Lines on the Same Plot")


plt.legend()

plt.grid(True)

plt.show()
