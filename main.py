from file_handler import load_tasks
from task_manager import (
    add_task,
    view_tasks,
    delete_task,
    mark_completed,
    edit_task,
    search_task,
    statistics
)
from utils import display_menu, get_choice, pause


def main():

    tasks = load_tasks()

    while True:

        display_menu()

        choice = get_choice()

        if choice == "1":
            add_task(tasks)
            pause()

        elif choice == "2":
            view_tasks(tasks)
            pause()

        elif choice == "3":
            delete_task(tasks)
            pause()

        elif choice == "4":
            mark_completed(tasks)
            pause()

        elif choice == "5":
            edit_task(tasks)
            pause()

        elif choice == "6":
            search_task(tasks)
            pause()

        elif choice == "7":
            statistics(tasks)
            pause()

        elif choice == "8":

            print("\nThank you for using To-Do List Manager!")
            print("Have a productive day! 🚀")
            break

        else:

            print("\n❌ Invalid Choice.")
            print("Please choose a number between 1 and 8.")
            pause()


if __name__ == "__main__":
    main()