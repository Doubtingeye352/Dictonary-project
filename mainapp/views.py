from django.shortcuts import render
from PyDictionary import PyDictionary

def home(request):
    return render(request,'index.html')

def final(request):
    
    if request.method == "POST":
        txt = request.POST.get("txt")
        
        dictionary = PyDictionary()
        
        v = dictionary.meaning(str(txt))
        
        
    return render(request,'final.html', {'txt':txt,'meaning':v})