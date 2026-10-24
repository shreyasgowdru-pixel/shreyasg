#2.1

#1. git is software too running on computer, while github is website that stores projects in cloud
#2. terminal is the app that gives access to command line, which is the text based innnterface where you can type commands
#3. local repository is the version of your project inn your own computer while remmote is a copy hosted on a network like github
#4. version control = system that records changes to files over time to recall specific versions later
#5. staging area is a place where you prepare files before saving them permanently in git
#6. git add moves changes from working dir to staging area
#7. git commit brings changes to staging area and waits to commit
#8. git push sends changes from local to remote repository
#9. git status checks the state of your working directory and staging area
#10. git pull downnloads and merges changes from remote repository to your computer
#11. pwd is print working directory that shows the full file path of the folder
#12. ls is list that displays all files/folders in current directory
#13. cd is change directory that allows you to move between folders
#14. nano edits the file
#15. touch creates a new file
#16. mv moves AND renames files/folders
#17. rm PERMANENTLY deletes files/folders
#18. cat displays the contents of a file

#2.2

#pwd
#ls
#cd python_decal_fa26/judy AND git pull
#mv homework.py homework/
# .. cd homework
#cat homework.py
#git add . AND git commit -m "added homework.py" AND git push
#git push origin main
#cd /Users/judy/Recents/

#2.3: in folder

#3.1

def checkDataType(data):
    if type(data) == str:
        print("string")
    elif type(data) == int:
        print("integer")
    elif type(data) == float:
        print("float")
    elif type(data) == bool:
        print("boolean")
    else:
        print("unknown data type")

#3.2

def evenOrOdd(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"

#4

def sumWithLoop(list):
    sum = 0
    for i in list:
        sum += i
    print(sum)

#5.1

def duplicateList(list):
    newList = []
    for i in list:
        for j in range(2):
            newList.append(i)
    return newList

#5.2 
#error was it was missing colon for function, and it didn't check to see if it was a num or string

def square(num):
    if num == str:
        return "input is not a number"
    else:
        return num * num