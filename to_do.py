print("Put a list of things you want to get done in the available prompts. If you have no set time for a task, just put \"na\" or just nothing")
print("if you wish to stop just say \"quit\" when it asks for task")

file = open("to-do-list.txt", "w+")

#do you wnt to emoty file

while True:
    task = input("Add a task: ")
    time = input("Set a time: ")

    file.write(f"task: {task} \n time: {time} \n")

    if task.lower() == "quit":
        break

file.close()

print("Thank you, your to-do list has been created and made to a file in this same folder")