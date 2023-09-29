from numpy import e, pi

def dft(image: list[list[int]], u:int, v:int):
    W = len(image)
    H = len(image[0])

    return sum([
        sum([
            image[n][m] * e**(-2j*pi*(u*n/W + v*m/H))
            for n in range(W)
        ])
        for m in range(H)
    ])

def idft(dft_image: list[list[int]], u:int, v:int):
    W = len(dft_image)
    H = len(dft_image[0])

    return sum([
        sum([
            dft_image[n][m] * e**(2j*pi*(v*m/H + u*n/W))
            for m in range(H)
        ])
        for n in range(W)
    ])