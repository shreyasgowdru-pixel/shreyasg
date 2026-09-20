# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
# Git is an open source software tracking history of code, GitHub is cloud-based service to store Git repositories, Git Bash is commmand line programm (Windows)
# 2) What’s the difference between the terminal and the command line?
#command linne is where you type text instructions, terminal is the program that runs the interface to talk to the computer
# 3) How does Windows PowerShell differ from Git Bash?
# Powershell uses windows syntax adn git bash uses linux scripting
# 4) What’s the difference between Anaconda, conda, and Python?
# anaconda is a larrge software distribution with several packages, conda is a package and downloads python libraries, python is the core commuter programming language
# 5) What is VS Code? 
# VSCode is a code ediitor
# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
# Jupyter NB is a document format that lets you mix live executable code, equations, etc while Jupyter Lab is the next gen user interface for Jupyter
# 7) What does ~/ mean?
# Home directory
# 8) What’s the difference between an absolute path and a relative path?
# absolute is complete and fixed that works identically no matter what directory you're in. relative uses current dirrectory as starting rreference point
# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
# absolute: /Users/Shreya/python_decal_f26/shreyasg/homework2\
# relative: shreyasg/homework2
# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
# cd ..
# 11) What would rm ./ do in your current directory? (Don’t try it!)
# deletes current directory
# 12) What do the following commands do?
# git add: moves changes from working in directory to a temporary area
# git commit: permanently saves staged changes to local project history
# git push: uploads all locally committed snapshots to remote server cloud
# 13) What's the difference between "git add ." and "git add <file>"?
# first one adds all files across current directory, the second one only restricts its modification to the one file you write
# 14) What do "git status" and "git log -1" do?
# git status shows how the project directory is currently, while git log -1 shows the history of past work
# 15) What’s the difference between cloning a repository and pulling from it?
# cloning is done only once at the beginning, which downloads a repository. pulling can be one regularly to a repo you've already cloned (dowloads latest changes and merges to existing files)
# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
# trying to do the git clone command not realizing the link does not lie in between <>. I fixed it by looking up the error it gave me (and i was told it was a syntax error) and realized I need to remove the <>
# 17) What’s a question you still have? What’s something you’re confused about?
# I am confused about how exactly the git works; what is the add, commit, and push for? just files? I realize github is a place to share code, and I understand how it works but I dont understand the core of what all these things really mean.
# 18) Tell me a fun fact!
# I am an only child!
# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)
import math

x = math.e
y = math.pi

z = x
z+=y

print(x, y, z, x*y)