from numpy import sin, e, pi

def fourier_transform(input_sequence:list):
    N = len(input_sequence)
    output_sequence = []

    for k in range(N):
        output_sequence.append(
            sum([
                input_sequence[n] * e**(-2j*pi*k*n/N) for n in range(N)
            ])
        )

    return output_sequence

def inverse_fourier_transform(input_sequence:list):
    N = len(input_sequence)
    output_sequence = []

    for n in range(N):
        output_sequence.append(
            sum([
                input_sequence[k] * e**(2j*pi*k*n/N) for k in range(N)
            ]) / N
        )

    return output_sequence

if __name__ == "__main__":
    """
    Testing module
    """

    import numpy as np
    import matplotlib.pyplot as plt
    from random import random

    periods = [1,5]
    amplitudes = [1,1]
    sequence = [0*(random()-0.5) + sum([amplitudes[i]*sin((2*pi)/T*x) for i,T in enumerate(periods)]) for x in np.arange(0, 5, 0.1)]

    data = np.abs(fourier_transform(sequence))
    inv_data = inverse_fourier_transform(fourier_transform(sequence))
    np_data = np.abs(np.fft.fft(sequence))

    plt.plot(sequence, color='black', label='signal sequence', marker="o",markersize=0.75,linewidth=2,linestyle='dashed',dashes=(5,5))
    plt.plot(np_data, color='red', label='fft (numpy)', marker="o",markersize=0.75,linewidth=2,linestyle='dashed',dashes=(5,5))

    plt.plot(np.arange(0, len(data), 1),        data, label='dft',              marker="o",color='orange',markersize=1,linewidth=0.5)
    plt.plot(np.arange(0, len(sequence), 1),    inv_data, label='inverse dft',  marker="o",color='blue',markersize=1,linewidth=0.5)

    plt.legend()
    plt.grid()
    plt.show()