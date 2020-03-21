from django.shortcuts import render

def home(r):
    return render(r, "start.html")
def search(q):
    return render(q, "components/search.html")