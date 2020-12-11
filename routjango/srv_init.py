import os
import sys

# making a srv app inside the Django Project
project_name = sys.argv[1]
change_Dir = f"cd Destination\\{project_name}"
new_app_cmd = "python manage.py startapp srv"

try:
    os.system(f"{change_Dir} && {new_app_cmd}")
except:
    print("  ERROR : Unable to make srv app in the Django-Project")
    exit(1)
