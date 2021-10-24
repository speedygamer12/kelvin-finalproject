from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Surveyor
from .forms import SurveyorForm
from .serializer import SurveyorSerializers

import pickle
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd


def status(df):
    try:
        scaler = pickle.load(open('static/scalar.sav', 'rb'))
        model = pickle.load(open("static/model.sav", 'rb'))
        X = scaler.transform(df)
        y_pred = model.predict(X)
        return round(y_pred[0])

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def home_view(request):
    
    if request.method == 'POST':
        form = SurveyorForm(request.POST or None)

        if form.is_valid():
            STDE = form.cleaned_data['STDE']
            MTDE = form.cleaned_data['MTDE']
            SUDEM = form.cleaned_data['SUDEM']
            SUDEC = form.cleaned_data['SUDEC']
            MVDEH = form.cleaned_data['MVDEH']
            MVDEV = form.cleaned_data['MVDEV']
            MVDEA = form.cleaned_data['MVDEA']
            SVDEH = form.cleaned_data['SVDEH']
            SVDEV = form.cleaned_data['SVDEV']
            FD = form.cleaned_data['FD']

            df = pd.DataFrame({"STDE":[STDE],"MTDE":[MTDE],"SUDEM":[SUDEM],"SUDEC":[SUDEC],"MVDEH":[MVDEH],
                            "MVDEV":[MVDEV],"MVDEA":[MVDEA],"SVDEH":[SVDEH],"SVDEV":[SVDEV], "FD":[FD]})
            result = status(df)

            return render(request, 'DjangoAPI/status.html', {'data':result})

    form = SurveyorForm()
    return render(request, 'DjangoAPI/form.html', {'form':form})

