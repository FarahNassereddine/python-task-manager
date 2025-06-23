# Task class to hold task details
class Task:
    def __init__(t, title, duration, priority):
        t.title = title
        t.duration = duration
        t.priority = priority

# Queue class to manage tasks
class TaskQueue:
    def __init__(t):
        t.tasks = []

    def insert(t, task):
        t.tasks.append(task)

    def extract(t):
        if not t.tasks:  # Check if queue is empty
            return None
        
        # Find task with highest priority
        highest_index = 0
        for i in range(1, len(t.tasks)):
            if t.tasks[i].priority < t.tasks[highest_index].priority:
                highest_index = i
        
        # Remove and return the highest priority task
        return t.tasks.pop(highest_index)

    def peek(t):
        if not t.tasks:  # Check if queue is empty
            return None
        
        # Find task with highest priority
        highest_priority = t.tasks[0]
        for task in t.tasks:
            if task.priority < highest_priority.priority:
                highest_priority = task
        
        return highest_priority

    def is_empty(t):
        return len(t.tasks) == 0

def complete_next_task(queue):
    task = queue.extract()
    if task:
        print(f"Completing: {task.title} ({task.duration} mins, Priority {task.priority})")
    else:
        print("No tasks to complete")

def title_key(task):
    return task.title

def search_for_task(queue, title):
    # Create sorted copy by title
    sorted_tasks = sorted(queue.tasks, key=title_key)
    
    # Binary search
    left = 0
    right = len(sorted_tasks) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_tasks[mid].title == title:
            return sorted_tasks[mid]
        elif sorted_tasks[mid].title < title:
            left = mid + 1
        else:
            right = mid - 1
    
    return None  # Not found

def duration_key(task):
    return task.duration

def sort_tasks(queue):
    # Create new sorted list by duration
    return sorted(queue.tasks, key=duration_key)

def main():
    task_queue = TaskQueue()
    num_tasks = int(input("How many tasks? "))
    
    for i in range(num_tasks):
        print(f"\nTask {i+1}:")
        title = input("Title: ")
        duration = int(input("Duration (mins): "))
        priority = int(input("Priority (lower=higher): "))
        task_queue.insert(Task(title, duration, priority))
    
    print("\nCurrent tasks:")
    for task in task_queue.tasks:
        print(f"- {task.title} ({task.duration} mins, Priority {task.priority})")
    
    print("\nCompleting next task:")
    complete_next_task(task_queue)
    
    search_word = input("\nSearch for task (title): ")
    found = search_for_task(task_queue, search_word)
    if found:
        print(f"Found: {found.title}")
    else:
        print("Task not found")
    
    print("\nTasks sorted by duration:")
    sorted_list = sort_tasks(task_queue)
    for task in sorted_list:
        print(f"- {task.title}: {task.duration} mins")

if __name__ == "__main__":
    main()
