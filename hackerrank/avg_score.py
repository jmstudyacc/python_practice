if __name__ == '__main__':
    total = 0
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # find the scores relevant to the target query by getting values associated with key
    query_scores = student_marks.get(query_name)

    for i in range(len(query_scores)):
        total += query_scores[i]

    # remembering the below f-string will print to 2dp
    print(f"{(total / 3):.2f}")
