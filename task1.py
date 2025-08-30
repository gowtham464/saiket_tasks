#create a empty list to store
todo_list=[]

#Function to add a new task
def add_task():
    task=input("enter your task: ")
    todo_list.append({"task":task,"status":"pending"})
    print("new tash added successfilly...")
#function to view all task
def view_task():
    print("your todo list: ")
    if len(todo_list) == 0:
        print("no pending tasks!")
    else:
        for index, task in enumerate(todo_list,1):
            print(f"{index}:{task["task"]} - {task['status']}")
    
    print("\n")
#function to mark a task as done
def mark_done():
    if len(todo_list)==0:
        print("list is empty")
    else:
        try:
            search_index=int(input("enter a task number that you want to mark as done:")) -1
            if 0 <= search_index <len(todo_list):
                todo_list[search_index]['status'] ='done'
                print(f"task {todo_list[search_index]['task']} has been mark done")
            else:
                print("invalid task number")
        except ValueError:
            print("please enter a valid task num")
#function to display a option
def option():
    while(True):
        print("*** Main Option ***")
        print("1, Add a new Task")
        print("2, View All Task")
        print("3, Mark a Task as complete")
        print("4, Exit")
        
        selection=input("Enter your selection:")
        if selection=="1":
            add_task()
        elif selection=="2":
            view_task()
        elif selection=="3":
            mark_done()
        elif selection=="4":
            print("Exiting the application...")
            exit()
        else:
            print("invalid selcetion!:",selection,"Try again!!")

option()
    
        
       
    
