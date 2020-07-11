import numpy as np
import matplotlib.pyplot as plt

size = 10000
rate = 0.25
data = np.random.random(size)


# Swap out random indices random amount of times
if rate < 1:
  data = np.sort(data)
  for i in range(np.random.randint(1, size * rate, 1)[0]):
    i = np.random.randint(0, size)
    j = np.random.randint(0, size)
    data[i], data[j] = data[j], data[i]


# Regression
def linear_regression(x, y):
  x_hat = np.mean(x)
  y_hat = np.mean(y)
  beta = (np.sum( (x - x_hat) * (y - y_hat) ) ) / ( np.sum( np.power(x - x_hat, 2) ) )

  alpha = y_hat - beta * x_hat

  return (beta, alpha)


x = range(len(data))
slope, intercept = linear_regression(x, data)
print(slope)
print(intercept)


plt.plot(x, data)
plt.plot(x, slope * x + intercept )
plt.show()