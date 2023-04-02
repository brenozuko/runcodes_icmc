def match_bachelors_and_spinsters(bachelors, spinsters):
    # Sort the bachelors and spinsters by age
    bachelors.sort(reverse=True)
    spinsters.sort(reverse=True)

    # Keep track of the number of bachelors left and the age of the youngest bachelor left
    remaining_bachelors = len(bachelors)
    youngest_bachelor_left = 0

    # Match the bachelors and spinsters based on age
    for i in range(len(bachelors)):
        # Find the spinster whose age is closest to the bachelor's age
        closest_spinster_index = -1
        closest_spinster_age_diff = int(9999999)

        for j in range(len(spinsters)):
            age_diff = abs(bachelors[i] - spinsters[j])
            if age_diff < closest_spinster_age_diff or (
                age_diff == closest_spinster_age_diff
                and spinsters[j] > spinsters[closest_spinster_index]
            ):
                closest_spinster_age_diff = age_diff
                closest_spinster_index = j

        # If there is a spinster available, marry the oldest bachelor to her and remove her from the list
        if closest_spinster_index != -1:
            spinsters.pop(closest_spinster_index)
            remaining_bachelors -= 1

        # If there are no spinsters available, there will be bachelors left over
        else:
            aux_bachelors = bachelors[i:]
            aux_bachelors.sort()
            youngest_bachelor_left = aux_bachelors[0]
            break

    # Output the number of bachelors left and the age of the youngest bachelor left
    return (remaining_bachelors, youngest_bachelor_left)


case = 1
while True:
    b, s = map(int, input().split())
    bachelors = []
    spinsters = []

    if b == 0 and s == 0:
        break

    for i in range(b):
        bachelors.append(int(input()))

    for i in range(s):
        spinsters.append(int(input()))

    remaining_bachelors, youngest_bachelor = match_bachelors_and_spinsters(
        bachelors, spinsters
    )
    if youngest_bachelor == 0:
        print("Case {}: {}".format(case, remaining_bachelors))
    else:
        print("Case {}: {} {}".format(case, remaining_bachelors, youngest_bachelor))
    case += 1
