# WEEK 6 CONSOLIDATION TASK: TO DO LIST MANAGER
# This Python task manager uses functions for each part of its functionality.
# The programme's functions will include: Add, Complete and Display. Tasks are saved in a JSON file for long-term storage.


# Python imports the json function and os path-fiding function.
import json
import os


# This is the path to the folder that contains the JSON file for long-term storage
location = r"C:\Users\uchec\OneDrive\Software Dev Module code for backup\Week 6"
TASKFILE = os.path.join(location, 'taskStorage6.json')


# ADD TASKS FUNCTION
def add(description):
    tasks = []  # Initialising tasks as a new empty list

    # This opens and reads the file: taskStorage6.json
    if os.path.exists(TASKFILE):
        with open(TASKFILE, "r") as f: 
            tasks = json.load(f)
           
    # The below creates a new task as a dictionary with id, description and completed fields
    task = {                
        "id": len(tasks) +1,  # ID is the next consecutive number from previous task
        "description": description,  # task name is description entered from input at main menu
        "completed": False  # Initial completion status is automatically false
    }
    tasks.append(task)  # Append adds the newly created task to the end of the tasks list
    
    # The below saves TASKFILE
    with open(TASKFILE, "w") as f:
        json.dump(tasks, f, indent =2)  # The indent parameter prints each task attribute on a new line for better readability 
    print(f" ✓ New Task Added: {description}")


# LIST TASK FUNCTION
def showAll():
    # This loads the JSON file:
    if os.path.exists(TASKFILE):
        with open(TASKFILE, "r") as f:  # This opens and reads saved_tasks.json
            tasks = json.load(f)
    for task in tasks:
        status = "✓" if task["completed"] else "X"  # This shows a tick beside the task if the boolean value in the task completed field is True
        print(f" {status} [{task['id']}] {task['description']}")
    if not tasks:
        print(" No tasks found. Please return to main menu and add a task.")
        return
        

# COMPLETE TASK FUNCTION
def complete(id):

    # This loads the JSON file:
    if os.path.exists(TASKFILE):
        with open(TASKFILE, "r") as f:
            tasks = json.load(f)  # opens and reads the saved tasks file
   
    # This stores the ID entered by the user as task_id for later use within this function.
    task_id = id  

    # The below checks that the relevant task can be found among those available
    for task in tasks:
        # The below marks the task with the matching id as complete
        if task["id"] == id:    
            task["completed"] = True
            with open(TASKFILE, "w") as f:
                # The JSON file will be indented by 1 space for readability
                json.dump(tasks, f, indent=1) 

            print(f"✓ Task {task_id} is now marked complete. Returning to main menu...")
            print("=" *50 + "\n")  # Line for decoration and neatness.
            return

    # If the task is not found, the following error message is returned.
    if ValueError:
        print(f"Task {task_id} was not found. Returning to main menu...")
    else:
        print(f"Task {task_id} was not found")



# Main Menu
def menu(): 
    while True:
        print ("\n==== Main Menu ======= ")
        print("1. Add a Task ")
        print("2. List all Tasks ")
        print("3. Mark a Task as Complete ")
        print("4. Exit the Task Manager ")
        print("======================")  # CAN REMOVE if it looks untidy
        menu_input = input("\n Enter a choice from above (1-4): ").strip()  # Strip removes hanging spaces from the input

        # The user's main menu choice is accepted as a string.
        if menu_input == "1":
            description = input(" \n Please enter the task description: \n")
            if description.strip():  # Strip removes any leading or trailing spaces from the input
            # The if statement triggers the add_task function if a valid name is entered, and can print an error message or handle an exception if no input is entered
                try:
                    add(description)
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("You must enter something in the task description field to proceed. \nPlease return to main menu and try again") 

        elif menu_input == "2":  # Lists all tasks
            print("\n ===== CURRENT TASKS ======")
            showAll()

        elif menu_input == "3":  # Marks task as Complete
            try:
                showAll()  # This calls the function defined above and lists the tasks saved, so the user can choose which to mark complete
                id = int(input("From the list above, please enter the ID of the task to mark complete. \n"))
                complete(id)
            except ValueError:
                print("Invalid task ID. Enter a TASK ID from the list")  # This is triggered if the task ID entered is not in the list
            except Exception as e:
                print(f"Error: {e}")  # This is triggered for other errors

        elif menu_input == "4":  # Exits the task manager
            # The request for input will make the CLI software stay open after the user selects Exit
            stayopen = input("Goodbye!") 
            break
        
        else: 
            print(" ")
            print("\nInvalid choice. Please enter a number from among the menu options (1 -4)")
            menu()  # This is recursive and it returns to the main menu if the user enters an invalid choice.

if __name__ == "__main__":
    menu()  # This runs the mainmenu function when the script is executed directly.