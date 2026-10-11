t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    z = (n + 1) // 2
    o = n // 2

    R = n - k

    def build(start):
        if start == '0':
            zr = (R + 1) // 2
            orr = R // 2
        else:
            orr = (R + 1) // 2
            zr = R // 2

        if zr > z or orr > o:
            return None

        zlen = [1] * zr
        olen = [1] * orr

        zlen[0] += z - zr
        if orr:
            olen[0] += o - orr

        ans = []
        zi = oi = 0

        for i in range(R):
            if (i % 2 == 0 and start == '0') or (i % 2 == 1 and start == '1'):
                ans.append('0' * zlen[zi])
                zi += 1
            else:
                ans.append('1' * olen[oi])
                oi += 1

        return "".join(ans)

    res = build('0')
    if res is None:
        res = build('1')

    print(res if res is not None else -1)

