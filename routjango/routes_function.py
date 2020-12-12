# function for making a render route
def render_route(fullpath, renderpath, jsondata, parameters, requestmethod, formdata):
    if len(parameters) == 0:
        viewfunction = str(f"def {fullpath}(request")
    else:
        viewfunction = str(f"def {fullpath}(request")
        for parameter in parameters:
            viewfunction += str(f", {parameter}")
    viewfunction += str("):")
    for data in formdata:
        viewfunction += str(f"\n\t{data} = request.{requestmethod}['{data}']")

    viewfunction += str(f"\n\treturn render(request, '{renderpath}', {jsondata})")
    return viewfunction

def redirect_route(fullpath, redirectpath, parameters, requestmethod, formdata):
    if len(parameters) == 0:
        viewfunction =  str(f"def {fullpath}(request")
    else:
        viewfunction = str(f"def {fullpath}(request")
        for parameter in parameters:
            viewfunction += str(f", {parameter}")
    
    viewfunction += str("):")

    for data in formdata:
        viewfunction += str(f"\n\t{data} = request.{requestmethod}['{data}']")

    viewfunction += str(f"\n\treturn HttpResponseRedirect('{redirectpath}')")
    return viewfunction

def api_route(fullpath, jsondata, parameters, requestmethod, formdata):
    if len(parameters) == 0:
        viewfunction =  str(f'def {fullpath}(request')
    else:
        viewfunction = str(f"def {fullpath}(request")
        for parameter in parameters:
            viewfunction += str(f", {parameter}")
    viewfunction += str("):")

    for data in formdata:
        viewfunction += str(f"\n\t{data} = request.{requestmethod}['{data}']")
    
    viewfunction += str(f"\n\treturn HttpResponse({jsondata})")
    return viewfunction