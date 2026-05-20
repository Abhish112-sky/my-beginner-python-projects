def calculate_love_score(name_1, name_2):
    count_t = 0
    for a in name_1:
        if "t" == a:
            count_t += 1
    for a in name_2:
        if "t" == a:
            count_t += 1
    print(f"T occurs a total of: {count_t} in names.")
    count_r = 0
    for a in name_1:
        if "r" == a:
            count_r += 1
    for a in name_2:
        if "r" == a:
            count_r += 1
    print(f"R occurs a total of: {count_r} in names.")
    count_u = 0
    for a in name_1:
        if "u" == a:
            count_u += 1
    for a in name_2:
        if "u" == a:
            count_u += 1
    print(f"U occurs a total of: {count_u} in names.")
    count_e = 0
    for a in name_1:
        if "e" == a:
            count_e += 1
    for a in name_2:
        if "e" == a:
            count_e += 1
    print(f"E occurs a total of: {count_e} in names.")
    count_total_true = count_t + count_r + count_u + count_e
    print(f"Total occurences: {count_total_true}")
    count_l = 0
    for a in name_1:
        if "l" == a:
            count_l += 1
    for a in name_2:
        if "l" == a:
            count_l += 1
    print(f"L occurs a total of: {count_l} in names.")
    count_o = 0
    for a in name_1:
        if "o" == a:
            count_o += 1
    for a in name_2:
        if "o" == a:
            count_o += 1
    print(f"O occurs a total of: {count_o} in names.")
    count_v = 0
    for a in name_1:
        if "v" == a:
            count_v += 1
    for a in name_2:
        if "v" == a:
            count_v += 1
    print(f"V occurs a total of: {count_v} in names.")
    count_e1 = 0
    for a in name_1:
        if "e" == a:
            count_e1 += 1
    for a in name_2:
        if "e" == a:
            count_e1 += 1
    print(f"E occurs a total of: {count_e1} in names.")
    count_total_love = count_l + count_o + count_v + count_e
    print(f"Total occurences: {count_total_love}")
    print(f"Your final love score is: {count_total_true}{count_total_love}")

name_1 = input("Enter the first name: ").lower()
name_2 = input("Enter the second name: ").lower()
calculate_love_score(name_1, name_2)