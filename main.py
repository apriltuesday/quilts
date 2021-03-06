import numpy as np
import matplotlib.pyplot as plt


PI = np.pi
EPS = 1e-5
N = 256
IMAGE_DIR = 'images'


def quilt(a, b, c, d, k):
    A = np.zeros((N, N)) + EPS
    x = 0.1
    y = 0.3

    def f(X, Y):
        val = (
            a * np.sin(2 * PI * X)
            + b * np.sin(2 * PI * X) * np.cos(2 * PI * Y)
            + c * np.sin(4 * PI * X)
            + d * np.sin(6 * PI * X) * np.cos(4 * PI * Y)
            + k * X
        )
        return val - int(val) if val >= 0 else val - int(val) + 1

    # eliminate transients
    for n in range(50):
        new_x = f(x, y)
        new_y = f(y, x)
        x = new_x
        y = new_y

    # draw
    for n in range(100000):
        new_x = f(x, y)
        new_y = f(y, x)
        x = new_x
        y = new_y
        A[int(N * x), int(N * y)] += 1

    # save image
    result = np.block([[A, A], [A, A]])
    plt.imsave('{}/q_{},{},{},{},{}.png'.format(IMAGE_DIR, a, b, c, d, k), result, cmap='viridis')


if __name__ == '__main__':
    a = np.random.rand() * 2 - 1
    b = np.random.rand() * 2 - 1
    c = np.random.rand() * 2 - 1
    d = np.random.rand() * 2 - 1
    k = np.random.randint(-2, 3)
    quilt(a, b, c, d, k)
