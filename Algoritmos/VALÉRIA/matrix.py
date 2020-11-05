answers = ["a", "b", "b", "a", "c", "d", "e", "e", "a", "b"]


def grade(tests):
    grades = []
    for i in range(3):  # mudar o número 2 para o número de provas
        singular_grade = 0
        for j in range(10):
            if tests[i][j] == answers[j]:
                singular_grade += 1
        grades.append(singular_grade)
    return grades


provas = [
    ["a", "b", "c", "d", "e", "a", "b", "c", "d", "e"],
    ["a", "a", "b", "b", "c", "c", "d", "d", "e", "e"],
    ["a", "b", "b", "a", "c", "d", "e", "e", "a", "b"],
]

print(grade(provas))