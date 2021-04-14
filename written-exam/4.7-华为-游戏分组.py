'''
6
Jack Tom
Alice John
Jessica Leonie
Tom Alice
John Jack
Leonie Jessica
'''
'''
2
Jack Alice
Bob John
'''

num = int(input())
relation = {}

students = set()

for _ in range(num):
    line = input()
    source, target = line.split(' ')

    if source not in relation:
        relation[source] = [target]
    else:
        if target not in relation[source]:
            relation[source].append(target)

    if target not in relation:
        relation[target] = [source]
    else:
        if source not in relation[target]:
            relation[target].append(source)

    students.add(source)
    students.add(target)

students = list(students)
visited = set()
ans = 0


def dfs(source):
    if source in relation:
        for target in relation[source]:
            if target not in visited:
                visited.add(target)
                dfs(target)


for student in students:
    if student not in visited:
        dfs(student)
        ans += 1

print(ans)
