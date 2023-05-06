from . import dft

def dft_byRow(image):
    transformed_image = []
    for i, row in enumerate(image):
        transformed_image.append(dft.fourier_transform(row))
        print(f"[{i}/{len(image)}]", end='\r')
    return transformed_image

def idft_byRow(image):
    inverse_transformed_image = []
    for i, row in enumerate(image):
        inverse_transformed_image.append(dft.inverse_fourier_transform(row))
        print(f"[{i}/{len(image)}]", end='\r')
    return inverse_transformed_image