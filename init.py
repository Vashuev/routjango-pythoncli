import os
import sys

if len(sys.argv) == 2:
    project_name = sys.argv[1]
else:
    project_name = "DjangoProject"

os.system(f"python routjango\django_init.py {project_name}")