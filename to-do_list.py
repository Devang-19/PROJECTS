task = []

def show_task():
    if not task:
        print("Your Task List is Empty !!!")
    else :
        print("Your To - Do List : ")
        for i,task in enumerate(task,1) :
            status = "Done" if task ['done'] else "Not Done"
            print((f"{i}. {task['title']} - {status}"))