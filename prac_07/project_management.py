import datetime

MENU = """- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date
- (A)dd new project\n- (U)pdate project\n- (Q)uit"""
FILENAME = "projects.txt"

from prac_07.project import Project


def main():
    projects = load_project(FILENAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter a filename to load: ")
            projects = load_project(filename)
        elif choice == "S":
            filename = input("Enter a filename to save: ")
            save_projects(projects, filename)
        elif choice == "D":
            get_data(FILENAME)
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            add_projects(projects)
        elif choice == "U":
            get_data(FILENAME)
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_projects(projects, FILENAME)
    print("Goodbye")


def load_project(filename):
    projects = []
    in_file = open(filename, encoding="utf-8")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split()
        # date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        # project = Project(parts[0], date, int(parts[2]), int(parts[3]), int(parts[4]))
        # projects.append(project)
        # print(parts)
    in_file.close()
    return projects


def save_projects(projects, filename):
    """Write to the file and saves the project"""
    out_file = open(filename, "w", encoding="utf-8")
    for project in projects:
        print(f"{project.name}, {project.date}, {project.priority}, {project.cost}, {project.completion}",
              file=out_file)
    out_file.close()


def display_projects(projects):
    """Look at list comprehensions to use is_complete use for ... in ..."""
    print("Incomplete projects: ")
    incomplete_projects = [project for project in projects if not project.is_completed()]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(" ", project)
    print("Completed projects: ")
    complete_projects = [project for project in projects if project.is_completed()]
    complete_projects.sort()
    for project in complete_projects:
        print(" ", project)


def add_projects(projects):
    """Use append to add projects"""
    with open(FILENAME, "a", encoding="utf-8") as in_file:
        for line in in_file:
            name = input("Name: ")
            date_string = input("Date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            print(date.strftime("%d/%m/%Y"))
            priority = int(input("Priority: "))
            percentage = int(input("Percent complete: "))
        projects.append(line)
        print(file=in_file)


def update_project(projects):
    for i, project in enumerate(projects):
        print(i, project)
    update = input("Project choice: ")
    project = projects[update]
    print(project)

    # project_complete = int(input("New Percentage: "))
    # while project_complete != "":
    #     project_complete = int(input("New Percentage: "))
    #     project.project_complete = project_complete
    # return project_complete
    try:
        project_complete = int(input("New Percentage: "))
        project.project_complete = project_complete
    except ValueError:
        pass
    try:
        priority_check = int(input("New Priority"))
        project.priority_check = priority_check
    except ValueError:
        pass


def get_data(filename):
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()
        for line in in_file:
            sections = line.strip().split(',')
            projects.append(sections)
    return projects


if __name__ == '__main__':
    main()
