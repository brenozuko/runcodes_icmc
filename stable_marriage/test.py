def stable_marriage(men_free, m_pref, w_pref):
    dict_m = {i + 1: 0 for i in range(n)}
    wdict = dict()

    while len(men_free) != 0:
        m = men_free.pop()
        pref = m_pref[m - 1][dict_m[m]]
        eng = wdict.get(pref, -1)
        if eng == -1:
            wdict[pref] = m
        else:
            if w_pref[pref - 1][wdict[pref] - 1] > w_pref[pref - 1][m - 1]:
                dict_m[wdict[pref]] += 1
                men_free.add(wdict[pref])
                wdict[pref] = m
            else:
                men_free.add(m)
                dict_m[m] += 1
    tuple_sorted = sorted(wdict.items(), key=lambda x: x[1])
    return tuple_sorted


T = int(input())
for _ in range(T):
    n = int(input())
    w_pref = []
    m_pref = []

    for _ in range(n):
        w_l = [0 for _ in range(n)]
        aux_list = list(map(int, input().split()))
        for i in range(1, len(aux_list)):
            w_l[aux_list[i] - 1] = i

        w_pref.append(w_l)
    for _ in range(n):
        aux_list = list(map(int, input().split()))
        m_pref.append(aux_list[1:])

    men_free = set([i + 1 for i in range(n)])
    output = stable_marriage(men_free, m_pref, w_pref)

    for k, v in output:
        print(f"{v} {k}")
