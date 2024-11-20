import os
import matplotlib.pyplot as plt

submissions = []
for file in os.listdir('data/submissions'):
    data = open(f"data/submissions/{file}", 'r')
    data = data.read()
    data = data.split("|")
    student_id = data[0]
    assignment_id = data[1]
    grade = int(data[2])
    submission = {"student_id": student_id, "assignment_id": assignment_id, "grade": grade}
    submissions.append(submission)

students = {}
for line in open('data/students.txt', 'r'):
    id = line[:3]
    name = line[3:]
    name = name.rstrip()
    students[name] = id

assignments = {}
assignment_data = open('data/assignments.txt', 'r').read()
assignment_data = assignment_data.split('/n')
for i in range(0, len(assignment_data)-2, 3):
    name = assignment_data[i]
    id = assignment_data[i+1]
    points = assignment_data[i+2]
    assignments[id] = (name, int(points))


def print_menu():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    print()
    selection = int(input("Enter your selection: "))
    return selection

def student_grade():
    name = input("What is the student's name: ")
    if name in students.keys():
        id = students[name]
        points = 0
        for submission in submissions:
            if submission["student_id"] == id:
                score = submission["grade"] * assignments[submission["assignment_id"]][1] / 100
                points += score
        print(f"{round(points / 10)}%")
    else:
        print("Student not found")

def assignment_stats():
    assignment = input("What is the assignment name: ")
    id = None
    for k,v in assignments.items():
        if v[0] == assignment:
            id = k
    if id == None:
        print("Assignment not found")
        return
    scores = []
    for submission in submissions:
        if submission["assignment_id"] == id:
            scores.append(submission["grade"])
    print(f"Min: {min(scores)}%")
    avg = (sum(scores) // len(scores))
    print(f"Avg: {avg}%")
    print(f"Max: {max(scores)}%")


def assignment_graph():
    assignment = input("What is the assignment name: ")
    id = None
    for k,v in assignments.items():
        if v[0] == assignment:
            id = k
    if id == None:
        print("Assignment not found")
        return
    scores = []
    for submission in submissions:
        if submission["assignment_id"] == id:
            scores.append(submission["grade"])
    plt.hist(scores, bins=[50, 60, 70, 80, 90, 100])
    plt.show()

def main():
    selection = print_menu()
    if selection == 1:
        student_grade()
    elif selection == 2:
        assignment_stats()
    elif selection == 3:
        assignment_graph()
    else:
        print("Invalid selection")

if __name__ == "__main__":
    main()
