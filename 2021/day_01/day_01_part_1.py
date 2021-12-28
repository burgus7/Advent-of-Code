print('DAY 1 PART 1')

measurements = open('input_1', 'r')

answer = 0
previous = int(measurements.readline())
for num in measurements:
    current = int(num)
    if current > previous:
        answer += 1
    previous = current

print (f"The answer is {answer}")