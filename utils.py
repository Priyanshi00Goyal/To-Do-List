def display_menu():

    print("\n" + "=" * 40)
    print("         TO-DO LIST MANAGER")
    print("=" * 40)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Edit Task")
    print("6. Search Task")
    print("7. Statistics")
    print("8. Exit")

    print("=" * 40)


def get_choice():

    return input("Enter your choice: ").strip()


def pause():

    input("\nPress Enter to continue...")