import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from logic.functions.play_music import play_random_music
from  logic.functions.greet_user import greet_user
from logic.functions.help import show_help
def load_tasks(filename):
    with open(filename, 'r') as file:
        tasks_data = json.load(file)
    return tasks_data['tasks']

def preprocess_input(input_text):
    input_text = input_text.lower()
    tokens = word_tokenize(input_text) 
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words and word.isalnum()]
    return filtered_tokens

def match_task(input_text, tasks):
    for task, data in tasks.items():
        for keyword in data['keywords']:
            if keyword in input_text:
                return task, data['description']
        for keyword in data['keywords']:
            if all(word in input_text for word in keyword.split()):
                return task, data['description']
    return None, None

# Execute task
def execute_task(task):
    if task == 'turn_on_lights':
        print("Turning on the lights...")
    elif task == "play_music":
        play_random_music()
    elif task == "greet_user":
        greet_user()
    else:
        show_help()

# Example usage
def task_executor_main(user_input):
    tasks = load_tasks('data/tasks.json')
    
    task, description = match_task(user_input, tasks)
    if task:
        print(f"Executing task: {description}")
        execute_task(task)
    else:
        print("Sorry, I couldn't understand your command.")
        
        

if __name__ == "__main__":
    task_executor_main()
