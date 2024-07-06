if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        if 2 <= n <= 10:
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        else:
            print("Wrong !...Number of students must be between 2 to 10")
    query_name = input()
    if query_name in student_marks:
        scores = student_marks[query_name]
        middle = sum(scores) / len(scores)
        print("{:.2f}".format(middle))
    else:
        print("Error...")
