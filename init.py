import os

# it will ask for project_name and template_name
project_name = input("Enter the project_name : ")
template_name = input("Enter the template_name: ")

# making a django project 
if os.path.exists(f"Destination\{project_name}") == True:
    print(f" ERROR: Already have a project with this name : {project_name}")
    print("        Please try again with different project name..")
    exit(0)

# checking the template folder's name
if template_name.lower() == "views":
    print(f" ERROR: Cannot make a folder with name : {template_name}")
    print("        Please try again with different template name..")
    exit(0)

# making a Destination directory
if os.path.exists("Destination") == False:
    try:
        os.system("mkdir Destination")
    except:
        print("  ERROR : Unable to make Destination directory")
        exit(1)

# calling django_init.py file for making all the basic structure
try:
    os.system(f"python routjango\django_init.py {project_name} {template_name}")
except:
    print("  ERROR : Unable to call routjango\django_init.py file")
    exit(1)

# making routes
try:
    os.system(f"python routjango\\routes.py {project_name} {template_name}")
    print(f"routes has build for the {project_name}..")
except:
    print(f"  ERROR : Unable to call routjango\routes.py file")
    exit(1)

