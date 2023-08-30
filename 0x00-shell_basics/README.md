**This file explaine some luinx commands.**
**Every file start with #!/bin/bash**

First here is the steps to prepir the files:
1. ls -l > to check the file rights
2. chmod u+x > change the rights and make it executable
3. when running the ls -l shoud output -rwxrw-r-- instande of -rw-rw-r--
4. run the file using ./file-name

**Files:-**
0. script that prints the absolute path name of the current working directory
1. Display the contents list of your current directory.
2. script that changes the working directory to the user’s home directory.
3. Display current directory contents in a long format
4. Display current directory contents, including hidden files (starting with .). Use the long format.
5. Display current directory contents.
Long format
with user and group IDs displayed numerically
And hidden files (starting with .)
6. Create a script that creates a directory named my_first_directory in the /tmp/ directory.
7. Move the file betty from /tmp/ to /tmp/my_first_directory.
8. Delete the file betty.
The file betty is in /tmp/my_first_directory
9. Delete the directory my_first_directory that is in the /tmp directory.
10. Write a script that changes the working directory to the previous one.
11. Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
12. Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
13. Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.
14. Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
You can consider that all HTML files have the extension .html