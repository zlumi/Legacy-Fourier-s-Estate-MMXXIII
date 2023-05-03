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

    with open ('sequence.txt', 'w') as f:
        for i in range(len(data)):
            f.write(str(data[i]) + '\n')

    plt.plot(sequence, color='red', label='signal sequence', linewidth=5)
    plt.bar(np.arange(len(data)), np.abs(data), color='blue', label='dft', width=0.25)
    plt.plot(inverse_fourier_transform(data), color='orange', label='inverse dft')

    plt.bar(np.arange(len(data)), np.abs(np.fft.fft(sequence)), color='green', label='fft (numpy)', width=0.2)
    plt.plot(np.fft.ifft(np.fft.fft(sequence)), color='purple', label='inverse fft (numpy)')

    plt.legend()
    plt.grid()
    plt.show()