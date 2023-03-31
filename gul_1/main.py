t = int(input())
for _ in range(t):
    input()
    n = int(input())
    T = [0] * n
    S = [0] * n

    res = list(range(n))

    for i in range(n):
        T[i], S[i] = map(int, input().split())

    for i in range(n):
        for j in range(n - 1):
            if T[res[j]] * S[res[j + 1]] > S[res[j]] * T[res[j + 1]]:
                res[j], res[j + 1] = res[j + 1], res[j]
            elif (
                T[res[j]] * S[res[j + 1]] == S[res[j]] * T[res[j + 1]]
                and res[j] > res[j + 1]
            ):
                res[j], res[j + 1] = res[j + 1], res[j]

    print(res[0] + 1, end="")

    for i in range(1, n):
        print(" {}".format(res[i] + 1), end="")
    print()

    if _ != t - 1:
        print()
