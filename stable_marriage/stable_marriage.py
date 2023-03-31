t = int(input())


def stableMarriage(men_pref, women_pref, n):
    pass


for j in range(t):
    # Numero de homens e mulheres
    n = int(input())
    men_pref = []
    women_pref = []

    for i in range(n):
        input_line = input().split()
        aux_list = [int(y) for y in input_line[1:]]
        women_pref.append(aux_list)

    for i in range(n):
        input_line = input().split()
        aux_list = [int(y) for y in input_line[1:]]
        men_pref.append(aux_list)

    stableMarriage(men_pref, women_pref, n)
