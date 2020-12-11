import os
import sys

project_name = sys.argv[1]
os.system("mkdir Destination")
os.system(f"cd Destination && django-admin startproject {project_name}")
os.system(f"python routjango\srv_init.py {project_name}")
