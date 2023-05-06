import matplotlib.pyplot as plt

def fromDict(dict:dict):
    fig = plt.figure()

    subplt = fig.add_subplot(1, 2, 1)
    subplt.set_title('FT')
    subplt.plot(
        list(dict['ft'].keys()),
        list(dict['ft'].values()),
        marker='o'
    )
    subplt.set_xlabel('Image size (Pixels)')
    subplt.set_ylabel('Time (Seconds)')

    subplt = fig.add_subplot(1, 2, 2)
    subplt.set_title('IFT')
    for img in dict['ift'].keys():
        subplt.plot(
            dict['ift'][img].keys(),
            dict['ift'][img].values(),
            label=str(img), marker='o'
        )
        subplt.legend()
        subplt.set_xlabel('Quality (%)')
        subplt.set_ylabel('Time (Seconds)')

    plt.show()

if __name__ == "__main__":
    import json

    with open('out/test_1.json', 'r') as f:
        dct = json.loads(f.read())

    fromDict(dct)