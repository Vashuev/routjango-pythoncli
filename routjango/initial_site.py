import sys

# getting the project name and template name
project_name = sys.argv[1]
templates_folder = sys.argv[2]

html_data = '<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Django Site</title>\n\t\t<meta charset="UTF-8">\n\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t</head>\n\t<body>\n\t\t<nav class="navbar navbar-expand-lg navbar-dark bg-primary">\n\t\t<a class="navbar-brand" href="#">TODO LIST</a>\n\t\t</nav>\n\t<h2>Django Initial Page</h2>\n\t</body>\n</html>'

# making a django_site.html page
with open(f"Destination\{project_name}\{templates_folder}\django_site.html", "w") as fp:
    fp.write(html_data)
fp.close()