def hashing(l, word):
    sum = 0
    for i in range(l):
        sum += (ord(word[i]) - ord('a') + 1) * pow(31, i)

    return sum % 1234567891

l = int(input())
word = input()

hashing_value = hashing(l, word)


print(hashing_value)