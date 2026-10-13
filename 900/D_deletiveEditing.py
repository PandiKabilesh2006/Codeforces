import sys
 
def solve():
    # Fast I/O reading all at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(n):
        s = input_data[idx]
        t = input_data[idx+1]
        idx += 2
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
            
        j = len(t) - 1
        possible = True
    
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            
            if count_t.get(c, 0) > 0:
                if j >= 0 and c == t[j]:
                    count_t[c] -= 1
                    j -= 1
                else:
                    possible = False
                    break
                    
        if possible and j < 0:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))
 
if __name__ == '__main__':
    solve()