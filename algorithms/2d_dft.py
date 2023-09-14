from numpy import sin, e, pi

def fourier_transform_2d(input_sequence):
    N = len(input_sequence)
    output_sequence = []

    for k in range(N):
        output_sequence.append(
            sum([
                input_sequence[n] * e**(-2j*pi*k*n/N) for n in range(N)
            ])
        )

    return output_sequence