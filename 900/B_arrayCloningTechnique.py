import sys
from collections import Counter

input = sys.stdin.readline # Fast I/O

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    freq = max(Counter(nums).values())
    ans = 0
    while freq < n:
        ans += 1
        take = min(freq, n - freq)
        ans += take
        freq += take
    print(ans)

