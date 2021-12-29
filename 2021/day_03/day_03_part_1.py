
numbers = open('full_input_3', 'r')
# determine number of digits
num = numbers.readline()
ones_counter = [int(digit) for digit in num.strip()]
num_len = len(ones_counter)

total_counter = 0

for num in numbers:
    num_digits = [int(digit) for digit in num.strip()]
    for i in range(len(num_digits)):
        ones_counter[i] += num_digits[i]
    total_counter += 1

gamma_rate = ""
epsilon_rate = ""

for one_count in ones_counter:
    zero_count = total_counter - one_count
    if one_count > zero_count:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"



power = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(f"The power consumption is {power}. "
      f"\n Gamma Rate: {gamma_rate, int(gamma_rate, 2)} "
      f"\n Epsilon Rate: {epsilon_rate, int(epsilon_rate, 2)}")


