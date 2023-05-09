from django.shortcuts import render
from django.shortcuts import redirect
from our_plan_live.util import *
import sqlite3

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

db_file = "ourplan.db" 
def load(request):
    if request.method == "POST": #and request.headers.get("contentType": "application/json"):
        success = False
        data = {"success":False}

        conn = create_or_open_db(db_file)
        cursor = conn.execute("SELECT * FROM users;")
        users = cursor.fetchall()
        users_string = "\n".join([str(user) for user in users])
        success = True
        return JsonResponse({
            'success':success,
            'users':users_string,
#            'data':json.dumps(data)
            })

def save(request):
    # We need to save whatever data the user entered into SQLite
    if request.method == "POST": #and request.headers.get("contentType": "application/json"):
        try:
            data = json.loads(request.POST.get('data'))
            # print(data['first_name'])
            conn = create_or_open_db(db_file)
            cur = conn.cursor()
            cur.execute("INSERT INTO users (first_name, last_name) VALUES (?, ?)", (data['first_name'],data['last_name']) )
            conn.commit()
            conn.close()
            success=True
            
            # put the data into sqlite
        except:
            success=False
        
        return JsonResponse({
            'success':success,
        })
    else: 
        print("save fail")


