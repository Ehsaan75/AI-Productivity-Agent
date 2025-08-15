import argparse
from agent import ProductivityAgent

def main():
    parser = argparse.ArgumentParser(description="Your Personal Productivity Assistant")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 'ask' command
    ask_parser = subparsers.add_parser("ask", help="Ask the agent a question")
    ask_parser.add_argument('prompt', type=str, help="The question to ask the agent")

    # 'add' command
    add_parser = subparsers.add_parser("add", help="Add a task to the todo list")
    add_parser.add_argument('task', type=str, help="The task description")

    # 'view' command
    view_parser = subparsers.add_parser("view", help="View all tasks in the todo list")

    # 'complete' command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
    complete_parser.add_argument('task_number', type=int, help="The task number to complete")

    # 'delete' command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument('task_number', type=int, help="The task number to delete")

    # 'summarise' command
    summarise_parser = subparsers.add_parser("summarise", help="Get a smart summary of all tasks")

    args = parser.parse_args()
    agent = ProductivityAgent()

    if args.command == "ask":
        print(agent.ask(args.prompt))
    elif args.command == "add":
        print(agent.add_task(args.task))
    elif args.command == "view":
        print(agent.view_tasks())
    elif args.command == "complete":
        print(agent.complete_task(args.task_number))
    elif args.command == "delete":
        print(agent.delete_task(args.task_number))
    elif args.command == "summarise":
        print(agent.summarise_tasks())

if __name__ == "__main__":
    main()

