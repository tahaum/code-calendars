import input_utils as iu
from collections import deque, Counter

def main():
    path = '../data/10-1.txt'
    data = iu.read_text_file_standard(path)
    o = ['(', '[', '{', '<']
    c = [')', ']', '}', '>']
    counter = Counter({')': 0, ']': 0, '}': 0, '>': 0})
    corrupted_lines = [0] * len(data)
    for n, line in enumerate(data):
        q = deque()
        for char in line:
            if char in o:
                q.append(char)
            else:
                if o[c.index(char)] == q[-1]:
                    q.pop()
                else:
                    counter[char] += 1
                    corrupted_lines[n] = 1
                    break
    error_score = { ')': 3, ']': 57,  '}': 1197, '>': 25137}
    ans = sum([counter[char] * error_score[char] for char in c])
    print('Part 1:', ans)

    scores = { ')': 1, ']': 2,  '}': 3, '>': 4}
    missing_ends = list()
    for corrupted, line in zip(corrupted_lines, data):
        if not corrupted:
            q = deque()
            for char in line:
                if char in o:
                    q.append(char)
                else:
                    q.pop()
            q.reverse()
            missing = [c[o.index(char)] for char in q]
            missing_ends.append(missing) 
            
    total_points = list()   
    for end in missing_ends:
        print(end)
        points = 0
        for char in end:
            points = (5 * points) + scores[char]
        total_points.append(points)
    total_points.sort()
    print(total_points)
    print('Part 2:', total_points[len(total_points) // 2])
    
            
            
            
        
    
if __name__ == '__main__':
    main()