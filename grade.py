def average(scores):
    return sum(scores) / len(scores) if scores else 0

scores = [70, 80, 90]
print("Average:", average(scores))
