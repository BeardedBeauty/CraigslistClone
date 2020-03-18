from django.shortcuts import render

def home(r):
    return render(r, "start.html")
def new_search(q):
    print(q)