filename = "tasks.txt"
filename2 = "saved_tasks.txt"

def load_task(filename):
    tasks = []
    with open(filename, 'r', encoding='utf-8') as file:
        tasks = file.read().splitlines()
    return tasks

def save_task(filename2, tasks):
    with open(filename2, 'w', encoding='utf-8') as file:
        for task in tasks:
            file.write(task + '\n')
def add_task():
    pass
add_task()
def edit_task():
    pass
edit_task()

def delete_task(filename):
    tasks = load_task(filename)
    task_to_delete = input("Введіть завдання яке ви хочете видалити: ")
    updated_tasks = [task for task in tasks if task != task_to_delete]
    save_task(filename, updated_tasks)
def mark_ready_task():
    pass
mark_ready_task()
def main():
    choice = (input("\nВведіть номер дії, яку ви хотіли б виконати: "))
    while choice != "6":
        if choice == "1":
            add_task()
        elif choice == "2":
            edit_task()
        elif choice == "3":
            delete_task(filename,input("Введіть завдання, яке ви хочете видалити: "))
        elif choice == "4":
            mark_ready_task()
        elif choice == "5":
            save_task(filename2, tasks)
        choice = input("\nВведіть номер дії, яку ви хотіли б виконати: ")
    save_task(filename2, tasks)
    print("Дякуємо за користування!")
print("Меню ToDo листа.")
print("*" * 100)
print("1. Введення нового завдання.")
print("2. Редагування завдання.")
print("3. Видалення завдання.")
print("4. Відмітити виконане завдання.")
print("5. Зберегти завдання.")
print("6. Вийти з програми.")
print("*" * 100)
main()