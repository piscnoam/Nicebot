import json
import mainbot

def load_goals():
    try:
        with open('goals.json', 'r') as file:
            goals = json.load(file)
    except FileNotFoundError:
        goals = []
    return goals

def save_goals(goals):
    with open('goals.json', 'w') as file:
        json.dump(goals, file)

def add_goal(goals):
    name = input("Enter the goal name: ")
    description = input("Enter the goal description: ")
    deadline = input("Enter the deadline (optional): ")

    goal = {
        'name': name,
        'description': description,
        'status': 'In Progress',
        'deadline': deadline
    }
    goals.append(goal)
    save_goals(goals)
    print("Goal added successfully.")

def update_goal_status(goals):
    name = input("Enter the goal name to update status: ")
    for goal in goals:
        if goal['name'] == name:
            new_status = input("Enter the new status (e.g., In Progress, Completed, Abandoned): ")
            goal['status'] = new_status
            save_goals(goals)
            print("Goal status updated successfully.")
            return
    print("Goal not found.")

def view_goals(goals):
    for goal in goals:
        print(f"Name: {goal['name']}")
        print(f"Description: {goal['description']}")
        print(f"Status: {goal['status']}")
        print(f"Deadline: {goal['deadline']}")
        print("=" * 20)

def main():
    goals = load_goals()

    while True:
        print("Goal Tracker Menu:")
        print("1. Add a new goal")
        print("2. Update goal status")
        print("3. View all goals")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            add_goal(goals)
        elif choice == '2':
            update_goal_status(goals)
        elif choice == '3':
            view_goals(goals)
        elif choice == '4':
            print("Exiting Goal Tracker.\n")
            mainbot.robo()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
