from numpy import sin, e, pi

def fourier_transform(input_sequence):
    N = len(input_sequence)
    output_sequence = []

    for k in range(N):
        output_sequence.append(
            sum([
                input_sequence[n] * e**(-2j*pi*k*n/N) for n in range(N)
            ])
        )

    return output_sequence

def inverse_fourier_transform(input_sequence):
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

    import numpy as np
    import matplotlib.pyplot as plt
    from random import random

    periods = [1,5]
    amplitudes = [1,1]
    sequence = [0*(random()-0.5) + sum([amplitudes[i]*sin((2*pi)/T*x) for i,T in enumerate(periods)]) for x in np.arange(0, 5, 0.1)]

    # save sequence as a txt file seperated by commas
    with open("sequence.txt", "w") as f:
        f.write(",".join([str(x) for x in sequence]))

    data = np.abs(fourier_transform(sequence))
    np_data = np.abs(np.fft.fft(sequence))

    plt.plot(np.arange(0, len(data), 1), data, label='dft', marker="o", color='green', markersize=1, linewidth=0.5)
    plt.plot(np.arange(0, len(np_data), 1), np_data, label='np.fft', marker="o", color='red', markersize=0.75, linewidth=1, linestyle='dashed', dashes=(5, 5))

    plt.plot(np.arange(0, len(sequence), 1), inverse_fourier_transform(data), label='inverse dft', marker="o", color='blue', markersize=1, linewidth=0.5)
    plt.plot(sequence, color='black', label='signal sequence', marker="o", markersize=0.75, linewidth=1, linestyle='dashed', dashes=(5, 5))

    with open("text.csv", "w") as f:
        data = fourier_transform(sequence)
        for x in ["wave", "real", "imag", "abs"]:
            f.write(x + ",")
        f.write("\n")
        for i in range(len(sequence)):
            f.write(str(sequence[i]) + "," + str(np.real(data[i])) + "," + str(np.imag(data[i])) + "," + str(np.abs(data[i])) + "\n")

    plt.legend()
    plt.grid()
    plt.show()