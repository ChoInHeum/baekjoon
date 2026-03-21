answers = []

while True:
    test_value = input()

    digits = [int(d) for d in str(test_value)]

    if (digits[0] == 0):
        break

    reverse_digits = [rd for rd in reversed(digits)]

    if (digits == reverse_digits):
        answers.append("yes")
    else:
        answers.append("no")


for answer in answers:
    print(answer)