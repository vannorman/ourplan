from django.shortcuts import render
from django.shortcuts import redirect
from our_plan_live.util import *

def party(request):
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLScHjksqOaBXrBiPuGtu6W5v1tSK9NE_YJr9xjjTkINkhQR9lA/viewform?usp=sf_link")

def simple_page(template):
    def handler(request):
        context = {}
        return render(request,template,context)
    return handler


def main(request):
    obj = {}
    obj['works'] = []
    obj['works'].append({
        "title" : "Test",
        "content" : { "header": "content", "img" : "img.jpg" },
        })
    return renderWithNav(request,'index.html', obj)

    
def load(request):
    if request.method == "POST": #and request.headers.get("contentType": "application/json"):
        ip = get_client_ip(request)
        path =  settings.STATICFILES_DIRS[0]+"/user_settings/"+str(get_client_ip(request)+".settings.txt")
        success = False
        data = {"success":False}
        if os.path.isfile(path):
            f = open(path)
            data = json.load(f)

            f.close()
            success = True
        return JsonResponse({
            'success':success,
            'data':json.dumps(data)
            })

def save(request):
    print("save start")
    if request.method == "POST": #and request.headers.get("contentType": "application/json"):
        
        print("SAVE settings ???") 
        ip = get_client_ip(request)
        path =  settings.STATICFILES_DIRS[0]+"/user_settings/"+str(get_client_ip(request)+".settings.txt")
        print('path:'+path)
        try:
            f = open(path,"w+")
            user_settings = request.POST.get('settings')
            # print("user settings:"+user_settings)
            f.write(user_settings)
            f.close()
            success=True
        except:
            success=False
            user_settings="blah"
        return JsonResponse({
            'success':success,
            'data':user_settings
        })
    else: 
        print("save fail")


