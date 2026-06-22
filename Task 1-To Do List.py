tl=[]
while True:
  print("1.Add task")
  print("2.View tasks")
  print("3.Exit")
  ch=int(input("Enter choice:"))
  if ch==1:
    task=input("Enter task to be added:")
    tl.append(task)
    print("Task Added")
  elif ch==2:
    if len(tl)==0:
      print("No task available")
    else:
      print("----------------------------------------------------------------------------------------")
      print("                                      To-Do List                                        ")
      print("----------------------------------------------------------------------------------------")
      for i,t in enumerate(tl,start=1):
        print(i,".",t)
      print("----------------------------------------------------------------------------------------")
  elif ch==3:
    print("Program ended")
    break
  else:
    print("Invalid Choice")
