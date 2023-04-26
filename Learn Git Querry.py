# querries you should to know
# 1. ls : Lists the files and directories in the current directory.
# 2. ls -a : show the hidden file on current directory
# 3. cd: Changes the current directory to the specified directory.
# 4. mkdir: Creates a new directory.


# git and github

# 1. git : git is a open source version control system that can store our file on internet and we can track the file where i store the file 

# 2. gitHub : gitHub is a file store cloud where we can store the file and get the file from anywhere if where we have internet there.  

# 1) we introduced ourself in gitHub

# 1. git config --global user.name "Arsh"
# 2. git config --global user.email "arshahmad235@gmail.com"

# we can check the user name and email of querry is 
# git config --global user.name
# git config --global user.email

# 2) initialize the file directory 
# 1. git init : make a git file on that file directory

# 3) see the status of that file directory
# 1. git status : show the all changes file

# 4) add the changes file in staging area
# 1. git add <file name> : one by one add like this 
# 2. git add . : if we want to add once time to put all the file in staging area

# 5) then commit the changes when add all the file in staging area
# 1. git commit -m 'first commit' 
# 2. git commit -m 'changed by arsh add the sticky navbar '

# 6) if we want to push the file on github then querry is
# 1. git remote add origin SSH Link
# 2. git push -u origin master

# -------------------------- New Branch -----------------------
# if we want to create a new branch and work on that branch and add feature 

# 1) see the all branch by default is master branch 
# 1. git branch : show the all branch we have

# 2) we want to add new branch then querry is 
# 1. git branch <branch name> : make a new branch <Arsh> branch name

# 3) we want to go another branch then querry is 
# 1. git checkout <branch name>

# 4) go another branch and work on any project to add any new feature. if we successful to change and add new feature then merge the this branch into master branch
# 1. go to master branch : git checkout master
# 2. merge the both file : git merge <another branch name>


# --------------- go to the there where i changed and commit the file -------------

# 1) first see the all commit querry is 
# 1. git log : show the all commit and see the every commit have a unique SHA key 

# 2) if we want to go that changes or commit
# 1. git checkout <commit SHA key>
# 2. if you want to go previous commit then querry is : git checkout <that SHA key>

