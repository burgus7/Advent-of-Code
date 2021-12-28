print('DAY 1 PART 1')

measurements = open('input_1', 'r')

answer = 0

previous_three = []
for i in range(3):
    previous_three.append(int(measurements.readline()))

for num in measurements:
    previous_sum = sum(previous_three)
    removed_num = previous_three.pop(0)
    previous_three.append(int(num))
    current_sum = sum(previous_three)
    if current_sum > previous_sum:
        answer += 1

print (f"The answer is {answer}")