from utils import *

# Part 1
path = "../data/06.txt"
data = read_text_file_standard(path)
times = list(map(int, data[0].split(":")[1].split()))
dists = list(map(int, data[1].split(":")[1].split()))

wins = list()
for idx, (t, d) in enumerate(zip(times, dists)):
    wins.append(0)
    for test_t in range(t+1):
        v = test_t
        t_rem = t - test_t
        test_d = v * t_rem
        if test_d > d:
            wins[idx] += 1
prod = 1
for w in wins:
    prod *= w
    
print("p1:", prod)


# Part 2
time = int(''.join(data[0].split(":")[1].split()))
dist = int(''.join(data[1].split(":")[1].split()))
wins = 0
for test_t in range(time+1):
    v = test_t
    t_rem = time - test_t
    test_d = v * t_rem
    if test_d > dist:
        wins += 1
    
print("p2:", wins)