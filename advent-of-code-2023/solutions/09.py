from utils import *

# Part 1
path = "../data/09.txt"
data = read_text_file_standard(path)

sum_ = 0
for line in data:
    hists = list()
    hists.append(list(map(int, line.split())))
    while not all(v == 0 for v in hists[-1]):
        next_line = [hists[-1][i] - hists[-1][i-1] for i in range(1, len(hists[-1]))]
        hists.append(next_line)
    for i_r, hist in enumerate(hists[::-1]):
        i = len(hists) - i_r - 1
        if i_r == 0:
            hist.append(0)
        else:
            hist.append(hist[-1] + hists[i+1][-1])
    sum_ += hists[0][-1]
    
print("p1:", sum_) 