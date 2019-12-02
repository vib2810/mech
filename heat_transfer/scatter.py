import numpy as np
import matplotlib.pyplot as plt

# # Create data
# x = [150, 300, 450]
# y = [1.375, 1.75, 2.5]
# area = np.pi*3

# # Plot
# plt.scatter(x, y, c='b', alpha=1)
# plt.title('Friction Force vs Load')
# plt.xlabel('Load(N)')
# plt.ylabel('Friction Force(N)')
# plt.show()

# sample points 
X = [150, 300, 450]
Y = [17.32, 22.05, 31.49]

# Y= [ 0.24,0.36,0.48 ]

# solve for a and b
def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    print('best fit line:\ny = {:.5f} + {:.5f}x'.format(a, b))

    return a, b

a, b = best_fit(X, Y)

plt.scatter(X, Y)
plt.title('Friction Force vs Load')
plt.xlabel('Load(N)')
plt.ylabel('Friction Force(N)')
yfit = [a + b * xi for xi in X]
plt.plot(X, yfit)
plt.ylim([0, 35])
plt.xlim([0, 500])
	
for i_x, i_y in zip(X,Y):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))

plt.text(0.4*500,0.9*35, 'Best fit line:\ny = {:.5f} + {:.5f}x'.format(a, b))

plt.show()