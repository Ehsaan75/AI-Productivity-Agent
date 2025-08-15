# agent.py
import os
from openai import OpenAI
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

class ProductivityAgent:
    def __init__(self, todo_file='todo.json'):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.todo_file = todo_file
        self._ensure_todo_file_exists()

    def _ensure_todo_file_exists(self):
        if not os.path.exists(self.todo_file):
            with open(self.todo_file, 'w') as f:
                json.dump([], f)

    def add_task(self, task):
        """Adds a task to the todo list."""
        try:
            with open(self.todo_file, 'r') as f:
                tasks = json.load(f)
            
            tasks.append({"task": task, "status": "pending"})
            
            with open(self.todo_file, 'w') as f:
                json.dump(tasks, f, indent=4)
            
            return f"Task '{task}' added to the todo list."
        except Exception as e:
            return f"Error adding task: {e}"

    def view_tasks(self):
        """Displays all tasks in the todo list."""
        try:
            with open(self.todo_file, 'r') as f:
                tasks = json.load(f)
            
            if not tasks:
                return "No tasks found."
            
            formatted_tasks = "--- Your Tasks ---\n"
            for i, task in enumerate(tasks):
                formatted_tasks += f"{i+1}. {task['task']} - {task['status']}\n"
            return formatted_tasks
        except Exception as e:
            return f"Error viewing tasks: {e}"

    def complete_task(self, task_number):
        """Marks a task as complete."""
        try:
            with open(self.todo_file, 'r') as f:
                tasks = json.load(f)
            
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]['status'] = 'completed'
                
                with open(self.todo_file, 'w') as f:
                    json.dump(tasks, f, indent=4)
                
                return f"Task {task_number} marked as completed."
            else:
                return "Invalid task number."
        except Exception as e:
            return f"Error completing task: {e}"
    
    def delete_task(self, task_number):
        """Deletes a task from the todo list."""
        try:
            with open(self.todo_file, 'r') as f:
                tasks = json.load(f)
                
            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                
                with open(self.todo_file, 'w') as f:
                    json.dump(tasks, f, indent=4)
                
                return f"Task '{deleted_task['task']}' deleted from the todo list."
            else:
                return "Invalid task number."
        except Exception as e:
            return f"Error deleting task: {e}"

    def summarise_tasks(self):
        """Asks the LLM to summarise and prioritise the current to-do list."""
        tasks_str = self.view_tasks()
        if "No tasks found" in tasks_str:
            return "Nothing to summarize."
        
        prompt = f"""
        Here is my current to-do list:
        {tasks_str}
        Please provide a brief, one-paragraph summary of my workload and
        suggest which single task I should focus on next.
        """
        return self.ask(prompt)


    def ask(self, prompt):
        """Sends a prompt to the LLM and gets a response."""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a concise and helpful productivity assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            return None

if __name__ == "__main__":
    agent = ProductivityAgent()
    
    # Test todo functionality
    print(agent.add_task("Learn Python"))
    print(agent.add_task("Build a project"))
    print(agent.view_tasks())
    print(agent.complete_task(1))
    print(agent.view_tasks())
    print(agent.delete_task(2))
    print(agent.view_tasks())
    print(agent.summarise_tasks())
    
    # Test LLM functionality
    response = agent.ask("What are three tips for improving productivity?")
    print(response)

