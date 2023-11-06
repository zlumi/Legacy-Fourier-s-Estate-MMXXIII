import numpy as np

seq = [0,0,0,1,1,1,0,0,0]
fourier = np.fft.fft(seq)
total = ""

with open('fourier.txt', 'w') as f:
    for i in range(len(fourier)):
        f.write(
            f"\\sin({fourier[i].real}x\\frac{{2\\pi}}{{{len(seq)}}})+\\cos({fourier[i].imag}x\\frac{{2\\pi}}{{{len(seq)}}})\n"
        )
        total += f"\\sin({fourier[i].real}x\\frac{{2\\pi}}{{{len(seq)}}})+\\cos({fourier[i].imag}x\\frac{{2\\pi}}{{{len(seq)}}})+"
    
    f.write("\n"+total[:-1])