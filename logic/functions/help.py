import json

def show_help():
    with open('data/tasks.json', 'r') as file:
        tasks_data = json.load(file)
    print("Here are the tasks you can ask me to do:")
    for task, details in tasks_data["tasks"].items():
        if task=="help" or task=="greet_user":
            continue
        print(f"- {details['description']}")

if __name__ == "__main__":
    show_help()