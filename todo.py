import os

TASKS_FILE = "tasks.txt"

# --- Utility Functions ---

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")


def print_header():
    print("\n" + "="*45)
    print("        ✨ TO-DO LIST APPLICATION ✨")
    print("="*45 + "\n")


def show_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("📌 No tasks found. Add your first task!")
        return

    print("\nYour Tasks:")
    print("-" * 30)
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print("-" * 30)


# --- Core Features ---

def add_task(tasks):
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added successfully!")
    else:
        print("⚠️ Task cannot be empty.")


def remove_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to remove: "))
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Removed: {removed}")
    except (ValueError, IndexError):
        print("❌ Invalid task number.")


def edit_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to edit: "))
        new_text = input("Enter updated task: ").strip()
        if new_text:
            tasks[index - 1] = new_text
            save_tasks(tasks)
            print("✏️ Task updated successfully!")
        else:
            print("⚠️ New task cannot be empty.")
    except (ValueError, IndexError):
        print("❌ Invalid task number.")


def clear_tasks(tasks):
    confirm = input("Are you sure you want to delete ALL tasks? (yes/no): ").lower()
    if confirm == "yes":
        tasks.clear()
        save_tasks(tasks)
        print("🧹 All tasks cleared!")
    else:
        print("❌ Cancelled.")


# --- Main Menu ---

def main():
    tasks = load_tasks()

    while True:
        print_header()
        print("1. 📋 View Tasks")
        print("2. ➕ Add Task")
        print("3. 🗑️ Remove Task")
        print("4. ✏️ Edit Task")
        print("5. 🧹 Clear All Tasks")
        print("6. ❌ Exit")
        print("-" * 45)

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            clear_tasks(tasks)
        elif choice == "6":
            print("✨ Exiting... Your tasks are saved. Bye bestie! ✨")
            break
        else:
            print("❌ Invalid choice, try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
