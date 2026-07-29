from file_handler import save_tasks


def add_task(tasks):

    task = {
        "id": len(tasks) + 1,
        "title": input("Enter Task: "),
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("✅ Task Added Successfully!")


def view_tasks(tasks):

    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n========== YOUR TASKS ==========\n")

    for task in tasks:

        status = "✔" if task["completed"] else "✖"

        print(f'ID : {task["id"]}')
        print(f'Task : {task["title"]}')
        print(f'Status : {status}')
        print("-" * 35)


def delete_task(tasks):

    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks(tasks)

    try:

        task_id = int(input("\nEnter Task ID to Delete: "))

        for task in tasks:

            if task["id"] == task_id:

                tasks.remove(task)

                for index, task in enumerate(tasks, start=1):
                    task["id"] = index

                save_tasks(tasks)

                print("✅ Task Deleted Successfully!")

                return

        print("❌ Task Not Found.")

    except ValueError:

        print("Please enter a valid number.")


def mark_completed(tasks):

    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks(tasks)

    try:

        task_id = int(input("\nEnter Task ID: "))

        for task in tasks:

            if task["id"] == task_id:

                if task["completed"]:

                    print("Task already completed.")

                else:

                    task["completed"] = True

                    save_tasks(tasks)

                    print("✅ Task Marked Completed!")

                return

        print("❌ Task Not Found.")

    except ValueError:

        print("Invalid Input.")


def edit_task(tasks):

    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks(tasks)

    try:

        task_id = int(input("\nEnter Task ID to Edit: "))

        for task in tasks:

            if task["id"] == task_id:

                task["title"] = input("Enter New Task: ")

                save_tasks(tasks)

                print("✅ Task Updated Successfully!")

                return

        print("❌ Task Not Found.")

    except ValueError:

        print("Invalid Input.")


def search_task(tasks):

    if not tasks:
        print("\nNo tasks available.")
        return

    keyword = input("Enter Keyword: ").lower()

    found = False

    print()

    for task in tasks:

        if keyword in task["title"].lower():

            status = "✔" if task["completed"] else "✖"

            print(f'{task["id"]}. {task["title"]} [{status}]')

            found = True

    if not found:

        print("No matching task found.")


def statistics(tasks):

    total = len(tasks)

    completed = sum(1 for task in tasks if task["completed"])

    pending = total - completed

    print("\n========== STATISTICS ==========")

    print(f"Total Tasks      : {total}")
    print(f"Completed Tasks  : {completed}")
    print(f"Pending Tasks    : {pending}")