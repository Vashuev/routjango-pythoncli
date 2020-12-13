import sys

# getting the project name and template name
project_name = sys.argv[1]
templates_folder = sys.argv[2]

# opening django_site.html 
try:
    with open("routjango\django_site.html", 'r') as fp:
        page_source = fp.read()
    fp.close()
except:
    print("  ERROR : Unable to read django_site.html page source")
    page_source = "<h2> DJANGO SITE</h2>\n<p> this page is showing because the django_site couldn't read</p>"

# making a django_site.html in template
try:
    with open(f"Destination\{project_name}\{templates_folder}\django_site.html", "w") as fp:
        fp.write(page_source)
    fp.close()
except:
    print(f"  ERROR : Unable to write content in {templates_folder}django_site.html")
    
    