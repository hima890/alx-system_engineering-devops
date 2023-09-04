import sys
import os


########check for the file name argument, if its there continue else exit with message#######
if len(sys.argv) > 2:
    print("This script takes one arguments but {} where found!".format(len(sys.argv)))
    sys.exit()
    
elif len(sys.argv) < 2:
    print("No file name where found")
    sys.exit()
###############################################################################################

########definde the file name and path#######
file_to_be_created = str(sys.argv[1])
path_to_the_file = "./{}".format(file_to_be_created) #change it to .\ for windows user
check_file = os.path.isfile(path_to_the_file)
###############################################

#######check if the file exist and ex the commands#######
if not check_file:
    cmd_create_file = 'touch {}'.format(file_to_be_created)
    cmd_add_executable_mode = 'chmod a+x {}'.format(file_to_be_created)
    cmd_list = [cmd_create_file, cmd_add_executable_mode]
    for command in cmd_list:
        os.system(command)
##########################################################

#######write the file content and close it#######
    with open("{}".format(file_to_be_created), "w") as my_file:
        my_file.write("""#!/bin/bash

        """)
#######################


else:
    print("Can't create the file, file alredy exist!")
#############################################################