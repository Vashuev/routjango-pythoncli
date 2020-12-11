import os
import sys

project_name = sys.argv[1]

# making a Destination directory
try:
    os.system("mkdir Destination")
except:
    print("  ERROR : Unable to make Destination directory")
    exit(1)

# making a django project 
try:
    os.system(f"cd Destination && django-admin startproject {project_name}")
except:
    print("  ERROR : Unable to make Django project")
    exit(1)


# # making srv app withing the django project
try:
    os.system(f"python routjango\srv_init.py {project_name}")
except:
    print("  ERROR : Unable to call routjango\srv_init.py file")
    exit(1)

# adding srv-app in the danago project setting.py
try: 
    os.system(f"python routjango\setting_main.py {project_name}")
except:
    print("  ERROR : Unable to call routjango\setting_main.py file")
    exit(1)


# adding srv-urls.py in the danago project urls.py
try: 
    filename = "urls"
    os.system(f"python routjango\{filename}_main.py {project_name}")
except:
    print(f"  ERROR : Unable to call routjango\{filename}_main.py file")
    exit(1)
