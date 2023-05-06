import matplotlib.pyplot as plt
import cv2
import numpy as np
import plot
from luminance import to_grayscale
from time import time

from algorithms.by_row import dft_byRow, idft_byRow

"""

Example filetree:
/root
    /resources
        test_1.png
        test_2.png
        test_3.png
    /out
        test_1.csv (made by this script)

"""

def visual_test(transform, inverse, images:list, compression_levels:list):
    for i in images:
        i=i+1

        image = to_grayscale(cv2.imread(f'resources/test_{i}.png'))

        fig = plt.figure()
        fig.suptitle(f'Testing image {i}, size {image.shape[1]}x{image.shape[0]}')

        t = time()
        _transformed = transform(image)
        print(f"[{transform.__name__}] ft in {time()-t} seconds")

        wanted_len = len(_transformed[0])

        for p in compression_levels:
            lim = int((p/100)*wanted_len)
            _transformed = [x[:lim] for x in _transformed]
            transformed = [row+[0]*(wanted_len-lim) for row in _transformed]

            t = time()
            compressed = np.abs(inverse(transformed))
            print(f"[{inverse.__name__}] {p}% ift done in {time()-t} seconds")

            # if p == 50:
            #     with open(f'out/test_{i}.csv', 'w') as f:
            #         for row in compressed:
            #             f.write(','.join([str(x) for x in row])+'\n')

            subplt = fig.add_subplot(2, 5, compression_levels.index(p)+1)
            subplt.set_title(f'{p}%')
            subplt.imshow(compressed, cmap='gray')
            subplt.set_xticks([])
            subplt.set_yticks([])

    plt.show()

def raw_speed_test(transform, inverse, images:list, compression_levels:list):
    time_results = {'ft':{}, 'ift':{}}

    for i in images:
        i=i+1

        image = to_grayscale(cv2.imread(f'resources/test_{i}.png'))
        locator = f'test_{i}.png'
        time_results['ift'][locator] = {}

        t = time()
        _transformed = transform(image)
        time_results['ft'][str(image.shape[0]*image.shape[1])] = time()-t
        print(f"[{transform.__name__}] ft in {time()-t} seconds")

        wanted_len = len(_transformed[0])

        for p in compression_levels:
            lim = int((p/100)*wanted_len)
            _transformed = [x[:lim] for x in _transformed]
            transformed = [row+[0]*(wanted_len-lim) for row in _transformed]

            t = time()
            compressed = np.abs(inverse(transformed))
            time_results['ift'][locator][p] = time()-t

            print(f"[{inverse.__name__}] {p}% ift done in {time()-t} seconds")
    
    return time_results

if __name__ == "__main__":

    # visual_test(
    #     dft_byRow, idft_byRow,
    #     [1,2,3], 
    #     [
    #         100, 75, 50, 40, 30,
    #         25, 20, 15, 10, 5
    #     ]
    # )

    import json

    test = raw_speed_test(
        dft_byRow, idft_byRow,
        [1,2,3],
        [
            100, 75, 50, 40, 30,
            25, 20, 15, 10, 5
        ]
    )

    with open('out/test_1.json', 'w') as f:
        f.write(json.dumps(test, indent=4))
    
    plot.fromDict(test)