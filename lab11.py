def print_menu():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    print()
    selection = int(input("Enter your selection: "))
    return selection

def student_grade():
    name = input("What is the student's name: ")

def assignment_stats():
    assignment = input("What is the assignment name: ")

def assignment_graph():
    assignment = input("What is the assignment name: ")

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