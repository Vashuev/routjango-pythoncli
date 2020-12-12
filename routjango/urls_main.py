import sys
import re
import copy

# getting the project name
project_name = sys.argv[1]
filename = "urls.py"


# open the urls.py file and reading it into a urls_data variable
try:
    
    with open(f"Destination\{project_name}\{project_name}\{filename}", "r") as fp:
        urls_data = fp.read()
    fp.close()
except:
    print(f"  ERROR : Unable to open urls.py in {project_name} directory to read it's content")
    exit(1)

# makign a copy of urls_data
urls_for_url = copy.copy(urls_data)

# matching the regrex 
string1_to_search = "from django.urls import path"
string2_to_search = "urlpatterns = \[\n"
string1_to_subtitute = "from django.urls import path, include"
string2_to_subtitute = "urlpatterns =  [\n\tpath('', include('srv.urls')),\n"

regex1 = re.compile(string1_to_search)
urls_data = regex1.sub(string1_to_subtitute, urls_data)

regex2 = re.compile(string2_to_search)
urls_data = regex2.sub(string2_to_subtitute, urls_data)


# open the urls.py file and writing new path into it
try:
    with open(f"Destination\{project_name}\{project_name}\{filename}", "w") as fp:
        fp.truncate(0)
        fp.write(urls_data)
    fp.close()
except:
    print(f"  ERROR : Unable to open urls.py in {project_name} directory to write it's content")
    exit(1)


# adding views import in urls_for_url variable
string_to_search = "from django.contrib import admin"
string_to_subtitute = "from . import views"

regex = re.compile(string_to_search)
urls_for_url = regex.sub(string_to_subtitute, urls_for_url)

string_to_del = "urlpatterns = ["
string_to_add = "\nurlpatterns = []"
indx = urls_for_url.index(string_to_del)
urls_for_url = urls_for_url[:(indx-1)]
urls_for_url = urls_for_url+string_to_add

# making a new urls.py file in srv directory
try:
    with open(f"Destination\{project_name}\srv\{filename}", "w+") as fp:
        fp.write(urls_for_url)
    fp.close()
except:
    print("  ERROR : Unable to open urls.py in srv directory to write initial content")
    exit(1)



