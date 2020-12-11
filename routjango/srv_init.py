import os
import sys

# making a srv app inside the Django Project
project_name = sys.argv[1]
change_Dir = f"cd Destination\\{project_name}"
new_app_cmd = "python manage.py startapp srv"

os.system(f"{change_Dir} && {new_app_cmd}")