
def remove_num(list, val, position):
    new_list = []
    for num in list:
        if num[position] != val:
            new_list.append(num)
    return new_list


def find_oxy(oxy):

    """find oxygen based on most common per position"""

    oxy.sort()
    main = oxy.copy()
    position = 1

    while len(oxy) > 1:
        ones = 0
        zeros = 0

        for num in oxy:
            if num[position] == "1":
                ones += 1
            else:
                zeros += 1

        if ones >= zeros:
            oxy = remove_num(oxy, "0", position)
        else:
            oxy = remove_num(oxy, "1", position)

        position += 1
    return int(oxy[0], 2)


def find_co2(co2):

    """find co2 based on most common per position"""

    co2.sort()
    main = co2.copy()
    position = 1

    while len(co2) > 1:
        ones = 0
        zeros = 0

        for num in co2:
            if num[position] == "1":
                ones += 1
            else:
                zeros += 1

        if zeros > ones:
            co2 = remove_num(co2, "0", position)
        else:
            co2 = remove_num(co2, "1", position)

        position += 1
    return int(co2[0], 2)


numbers = open('full_input_3', 'r')

ones = []
zeros = []

for num in numbers:
    if num[0] == "0":
        zeros.append(num.strip())
    else:
        ones.append(num.strip())

if len(zeros) > len(ones):
    oxy = find_oxy (zeros)
    co2 = find_co2 (ones)
else:
    oxy = find_oxy (ones)
    co2 = find_co2 (zeros)

print (f"oxy: {oxy}, co2: {co2}")
life_support_rating = co2*oxy
print(f"The life support rating is {life_support_rating}")

