import datetime
import webbrowser
import mainbot

def show_time():
    now = datetime.datetime.now()
    print("Current time is:", now.strftime("%H:%M:%S"))

def set_reminder():
    reminder = input("Enter your reminder: ")
    time_str = input("Enter the reminder time (HH:MM): ")
    try:
        reminder_time = datetime.datetime.strptime(time_str, "%H:%M")
        now = datetime.datetime.now()
        delta = reminder_time.replace(year=now.year, month=now.month, day=now.day) - now
        if delta.total_seconds() < 0:
            delta += datetime.timedelta(days=1)
        print("Reminder set for:", reminder_time.strftime("%H:%M"))
        # You can use a library like 'time' or 'threading' to schedule the reminder.
        # For simplicity, we'll just wait here until the reminder time.
        import time
        time.sleep(delta.total_seconds())
        print("Reminder:", reminder)
    except ValueError:
        print("Invalid time format. Please use HH:MM.")

def search_web():
    query = input("What do you want to search for? ")
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)
    print("Opening search results for:", query)
    main()

def main():
    print("Welcome to your Personal Assistant!")
    while True:
        print("Available commands:")
        print("1. Show time")
        print("2. Set a reminder")
        print("3. Search the web")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            show_time()
        elif choice == '2':
            set_reminder()
        elif choice == '3':
            search_web()
        elif choice == '4':
            print("Exiting Personal Assistant.\n")
            mainbot.robo()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
