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
def delete_task():
    pass
delete_task()
def mark_ready_task():
    pass
mark_ready_task()
def main():
    pass
main()