from math import sin, e, pi

def fourier_transform(values):

    # https://en.wikipedia.org/wiki/Fast_Fourier_transform
    # https://en.wikipedia.org/wiki/Discrete_Fourier_transform

    N = len(values)
    transformed = []

    for k in range(N):
        X = 0

        for n in range(N-1):
            X += values[n] * e**((-2j*pi)/N * k * n)

        transformed.append(X)

    return transformed

def inverse_fourier_transform(values):

    # https://en.wikipedia.org/wiki/Fast_Fourier_transform
    # https://en.wikipedia.org/wiki/Discrete_Fourier_transform

    N = len(values)
    transformed = []

    for n in range(N):
        X = 0

        for k in range(N-1):
            X += values[k] * e**((2j*pi)/N * k * n)

        transformed.append(X/N)

    return transformed

if __name__ == "__main__":

    import numpy as np
    import matplotlib.pyplot as plt
    from random import random

    periods = [1,5]
    amplitudes = [1,3]
    sequence = [2*(random()-0.5) + sum([amplitudes[i]*sin((2*pi)/T*x) for i,T in enumerate(periods)]) for x in np.arange(0, 5, 0.1)]

    data = fourier_transform(sequence)
    np_data = np.fft.fft(sequence)

    plt.scatter(np.arange(0, len(data), 1), [abs(x) for x in data], color='red', label='dft', s=5)
    plt.scatter(np.arange(0, len(np_data), 1), [abs(x) for x in np_data], color='green', label='np.fft', s=5)

    plt.plot(np.arange(0, len(data), 1), [abs(x) for x in data], color='red', label='dft', linewidth=0.5)
    plt.plot(np.arange(0, len(np_data), 1), [abs(x) for x in np_data], color='green', label='np.fft', linewidth=0.5)

    plt.plot(sequence, color='red', label='signal sequence', linewidth=0.5)

    plt.legend()
    plt.grid()
    plt.show()