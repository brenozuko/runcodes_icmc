t = int(input())
for _ in range(t):
    input()
    n = int(input())
    T = [int(x) for x in input().split()]
    S = [int(x) for x in input().split()]
    res = list(range(n))
    for i, (t, s) in enumerate(zip(T, S)):
        for j in range(n - 1):
            if T[res[j]] * S[res[j + 1]] > S[res[j]] * T[res[j + 1]]:
                res[j], res[j + 1] = res[j + 1], res[j]
            elif (
                T[res[j]] * S[res[j + 1]] == S[res[j]] * T[res[j + 1]]
                and res[j] > res[j + 1]
            ):
                res[j], res[j + 1] = res[j + 1], res[j]
    print(" ".join(str(x + 1) for x in res))
    if _ != t - 1:
        print()
