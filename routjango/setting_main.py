import sys
import re

# getting the project name and template name
project_name = sys.argv[1]
templates_folder = sys.argv[2]

# open the settings.py file and save it into a setting_data variable
try:
    with open(f"Destination\{project_name}\{project_name}\settings.py", "r") as fp:
        setting_data = fp.read()
    fp.close()
except:
    print("  ERROR : Unable to open settings.py file to read it's content file")
    exit(1)

# matching the regrex 
string1_to_search = "from pathlib import Path\n"
string1_to_subtitute = "from pathlib import Path\nimport os\n"
string2_to_search = "INSTALLED_APPS = \[\n"
string2_to_subtitute = "INSTALLED_APPS = [\n\t'srv.apps.SrvConfig',\n"
string3_to_search = "'DIRS': \[\]"
string3_to_subtitute = str(f"'DIRS': [os.path.join(BASE_DIR, '{templates_folder}')]")

# subtituting first string
regex = re.compile(string1_to_search)
setting_data = regex.sub(string1_to_subtitute, setting_data)

# subtituting first string
regex = re.compile(string2_to_search)
setting_data = regex.sub(string2_to_subtitute, setting_data)

# subtituting first string
regex = re.compile(string3_to_search)
setting_data = regex.sub(string3_to_subtitute, setting_data)

# open the settings.py file and writing the app configuration into it
try:
    with open(f"Destination\{project_name}\{project_name}\settings.py", "w") as fp:
        fp.truncate(0)
        fp.write(setting_data)
    fp.close()
except:
    print("  ERROR : Unable to open setting.py file to write it's content file")
    exit(1)




