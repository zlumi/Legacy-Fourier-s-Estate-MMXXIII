from numpy import e, pi

def dft_2d(image: list[list[int]], u:int, v:int):       # u=frequency/width, v=frequency/height
    W = len(image)                                      # W = width of the image
    H = len(image[0])                                   # H = height of the image

    return sum([                                        # The sum of (
        sum([                                           # the sum of (
            image[n][m]                                 # the (n,m) in the image
            *e**(-2j*pi*(u*n/W + v*m/H))                # times e^(-2j*pi*(u*n/W + v*m/H))
            for n in range(W)                           # ) for all n in the width of the image
        ]) for m in range(H)                            # ) for all m in the height of the image
    ])

def idft_2d(dft_image: list[list[int]], n:int, m:int):  # (n,m) = position of pixel in the image
    W = len(dft_image)                                  # W = width of the image
    H = len(dft_image[0])                               # H = height of the image

    return sum([                                        # The sum of (
        sum([                                           # the sum of (
            dft_image[n][m]                             # the (n,m) in the DFT Matrix
            *e**(2j*pi*(v*m/H + u*n/W))                 # times e^(2j*pi*(v*m/H + u*n/W))
            for v in range(H)                           # ) for all v part of the array of frequencies along the height
        ]) for u in range(W)                            # ) for all u part of the array of frequencies along the width
    ])

