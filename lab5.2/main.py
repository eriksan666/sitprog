import os
def create_test_files():
    files = {
        "Sp1.txt": "Кружок информатики\nИванов\nПетров\nСидоров\nСпортсменов",
        "Sp2.txt": "Кружок математики\nИванов\nСмирнов\nКузнецов",
        "Sp3.txt": "Кружок физики\nПетров\nСмирнов\nУченый\nСпортсменов",
        "Sp4.txt": "Отличники\nИванов\nСидоров\nОтличников",
        "Sp5.txt": "Прогульщики\nСидоров\nПрогульщиков",
        "Sp6.txt": "Спортсмены\nПетров\nСпортсменов",
        "Sp7.txt": "Хор\nСмирнов\nХористов",
        "Sp8.txt": "БРСМ\nИванов\nКузнецов\nБРСМовец",
        "Sp9.txt": "Профсоюз\nИванов\nПетров\nСидоров",
        "Sp10.txt": "Наука\nПетров\nСмирнов\nУченый",
        "SpStGr.txt": "Список группы\nИванов\nПетров\nСидоров\nСмирнов\nКузнецов"
    }
    for filename, content in files.items():
        if not os.path.exists(filename):
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
create_test_files()
def read_students(filename):
    students = set()
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i in range(1, len(lines)):
            name = lines[i].strip()
            if name != "":
                students.add(name)
    return students
S1 = read_students("Sp1.txt")
S2 = read_students("Sp2.txt")
S3 = read_students("Sp3.txt")
S4 = read_students("Sp4.txt")
S5 = read_students("Sp5.txt")
S6 = read_students("Sp6.txt")
S7 = read_students("Sp7.txt")
S8 = read_students("Sp8.txt")
S9 = read_students("Sp9.txt")
S10 = read_students("Sp10.txt")
print("--- Задание 1 (Вариант 6) ---")
# Пункт 6: Сколько занимающихся наукой и кто (список) спортсменов посещают кружок физики.
result_task1 = S10 & S6 & S3
print("Количество спортсменов-ученых в кружке физики:", len(result_task1))
print("Их список:", result_task1 if len(result_task1) > 0 else "Список пуст")
print()
print("--- Задание 2.1 (Журнал по видам деятельности) ---")
journal = {
    "Информатика": S1,
    "Математика": S2,
    "Физика": S3,
    "Отличники": S4,
    "Прогульщики": S5,
    "Спортсмены": S6,
    "Хор": S7,
    "БРСМ": S8,
    "Профсоюз": S9,
    "Наука": S10
}
for activity, students in journal.items():
    print(f"{activity}: {len(students)} чел.")
print()
print("--- Задание 2.2 (Характеристика каждого студента группы) ---")
group = read_students("SpStGr.txt")
for student in group:
    activities = []
    if student in S1: activities.append("Информатика")
    if student in S2: activities.append("Математика")
    if student in S3: activities.append("Физика")
    if student in S4: activities.append("Отличник")
    if student in S5: activities.append("Прогульщик")
    if student in S6: activities.append("Спортсмен")
    if student in S7: activities.append("Хор")
    if student in S8: activities.append("БРСМ")
    if student in S9: activities.append("Профсоюз")
    if student in S10: activities.append("Наука")
    if not activities:
        activities.append("Нигде не состоит")
    print(f"{student}: {', '.join(activities)}")
print()
print("--- Задание 3* (Вариант 6: Количество вершин нечетной степени) ---")
K = 5
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 5), (2, 5)]
graph = {}
for i in range(1, K + 1):
    graph[i] = []
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
print(f"Список смежности графа: {graph}")
odd_degree_count = 0
odd_vertices = []
for v in range(1, K + 1):
    degree = len(graph[v])
    if degree % 2 != 0:
        odd_degree_count += 1
        odd_vertices.append(v)
print("Количество вершин с нечетной степенью:", odd_degree_count)
print("Это вершины:", odd_vertices)
