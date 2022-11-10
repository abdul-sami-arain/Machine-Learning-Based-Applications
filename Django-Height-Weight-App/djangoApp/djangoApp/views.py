from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import pandas as pd
import pickle


filename = 'final.sav'
load_model = pickle.load(open(filename,'rb'))

def home(request):
    return render(request,"home.html")

def result(request):
    height = np.int64(request.POST['height'])
    result = np.int64(request.POST['height'])
    result = load_model.predict([[result]])
    
    return render(request,"result.html",{'result':result.item(),'height':height,})