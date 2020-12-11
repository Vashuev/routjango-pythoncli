import sys
import re

# getting the project name
project_name = sys.argv[1]

# open the settings.py file and save it into a setting_data variable
try:
    with open(f"Destination\{project_name}\{project_name}\settings.py", "r") as fp:
        setting_data = fp.read()
    fp.close()
except:
    print("  ERROR : Unable to open settings.py file to read it's content file")
    exit(1)

# matching the regrex 
string_to_search = "INSTALLED_APPS = \[\n"
string_to_subtitute = "INSTALLED_APPS = [\n\t'srv.apps.SrvConfig',\n"

regex = re.compile(string_to_search)
setting_data = regex.sub(string_to_subtitute, setting_data)

# open the settings.py file and writing the app configuration into it
try:
    with open(f"Destination\{project_name}\{project_name}\settings.py", "w") as fp:
        fp.truncate(0)
        fp.write(setting_data)
    fp.close()
except:
    print("  ERROR : Unable to open setting.py file to write it's content file")
    exit(1)

print("App has registered in the setting.py file fo Django Project")



