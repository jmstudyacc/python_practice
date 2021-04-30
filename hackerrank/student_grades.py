if __name__ == '__main__':
    marks = []
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks.append([name, score])
        scores.add(score)

    marks.sort()
    second_lowest = (sorted(scores)[1])
    for i in range(len(marks)):
        if marks[i][1] == second_lowest:
            print(marks[i][0])

"""
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""