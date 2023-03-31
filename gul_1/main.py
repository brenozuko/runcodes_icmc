t = int(input())
for _ in range(t):
    input()
    n = int(input())
    T = [int(x) for x in input().split()]
    S = [int(x) for x in input().split()]
    ans = list(range(n))
    for i, (t, s) in enumerate(zip(T, S)):
        for j in range(n - 1):
            if T[ans[j]] * S[ans[j + 1]] > S[ans[j]] * T[ans[j + 1]]:
                ans[j], ans[j + 1] = ans[j + 1], ans[j]
            elif T[ans[j]] * S[ans[j + 1]] == S[ans[j]] * T[ans[j + 1]] and ans[j] > ans[j + 1]:
                ans[j], ans[j + 1] = ans[j + 1], ans[j]
    print(' '.join(str(x + 1) for x in ans))
    if _ != t - 1:
        print()
