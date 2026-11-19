def average(scores):
    if len(scores) == 0:
        return 0

    for score in scores:
        if score < 0 or score > 100:
            return 0

    result = sum(scores) / len(scores)

    return round(result, 2)


scores = [70, 80, 90]
print("Average:", average(scores))