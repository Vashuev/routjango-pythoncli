import sys
import re
from routes_function import render_route, redirect_route, api_route

project_name = sys.argv[1]

#########################################
def path_maker(path):
    path_parts = path.split('/')                # spliting the path 
    parameters = []
    for i in range(len(path_parts)):
        if path_parts[i].find("<")!= -1:           # checking for parameter
            parameter = path_parts.pop(i)              # if found getting out the parameter
            start = parameter.find(":")+1
            end = parameter.find(">")
            parameter = parameter[start:end]
            parameters.append(parameter)
            path_parts.insert(i, parameter)
            
    fullpath = "_".join(path_parts)             # making function name for views
    return str(f'\tpath("{path}/", views.{fullpath}, name="{fullpath}"),\n'), fullpath, parameters

#########################################

# reading the routes.json data
with open("routjango\\routes.json", "r") as fp:
    routes_data = eval(fp.read())
fp.close()

routes = routes_data["routes"]

# urlpatterns list for the url.py file
urlpatterns = "\nurlpatterns = [\n# comment the below route to if you don't want to render the django_site page\n\tpath('', views.django_site, name='django_site'),\n"

# viewsfunction list for the views.py file
viewsfunctions = "from django.shortcuts import render\nfrom django.http import HttpResponseRedirect, HttpResponse\n" 
viewsfunctions += "\n# Please comment the django_site function stop it rendering on route: 127.0.0.8080/\ndef django_site(request):\n\treturn render(request, 'django_site.html')\n\n"

for route in routes:
    path = route["path"]
    route_type = route["type"]

    url_field, fullpath, parameters = path_maker(path)
    urlpatterns += url_field

    if route_type == "render":
        renderpath = route["render_path"]
        jsondata = route["json_data"]
        requestmethod = route["request_method"]
        formdata = route["form_data"]
        # calling render_route
        viewsfunction = render_route(fullpath, renderpath, jsondata, parameters, requestmethod, formdata)
        viewsfunctions += ("\n" + viewsfunction + "\n")


    elif route_type == "redirect":
        redirectpath = route["redirect_path"]
        requestmethod = route["request_method"]
        formdata = route["form_data"]
        # calling redirect_route
        viewsfunction = redirect_route(fullpath, redirectpath, parameters, requestmethod, formdata)
        viewsfunctions += ("\n" + viewsfunction + "\n")

    elif route_type == "api":
        jsondata = route["json_data"]
        requestmethod = route["request_method"]
        formdata = route["form_data"]
        # calling api_route
        viewsfunction = api_route(fullpath, jsondata, parameters, requestmethod, formdata)
        viewsfunctions += ("\n" + viewsfunction + "\n")


urlpatterns += "]"

# print(urlpatterns)

# addin all the urls into urls.py file of srv
string_to_del = "urlpatterns = ["
try:
    filename = "urls.py"
    with open(f"Destination\{project_name}\srv\{filename}", "r") as fp:
        urls_data = fp.read()
    fp.close()
    indx = urls_data.index(string_to_del)
    urls_data = urls_data[:(indx-1)]
    urls_data += urlpatterns
    with open(f"Destination\{project_name}\srv\{filename}", "w") as fp:
        fp.truncate(0)
        fp.write(urls_data)
    fp.close()
except:
    print("  ERROR : Unable to open urls.py in srv directory to write urlspattern")
    exit(1)

# adding all the viewsfunctions into views.py file of srv
try:
    filename = "views.py"
    with open(f"Destination\{project_name}\srv\{filename}", "w") as fp:
        fp.truncate(0)
        fp.write(viewsfunctions)
    fp.close()
except:
    print("  ERROR : Unable to open views.py in srv directory to write viewsfunctions")
    exit(1)

