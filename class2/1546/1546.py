count = int(input())
scores = [int(a) for a in input().split()]
max_score = max(scores)
new_sum = 0
for score in scores:
    new_sum += score/max_score*100

print(new_sum/count)