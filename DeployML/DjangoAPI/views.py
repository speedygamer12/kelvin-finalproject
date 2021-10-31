from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from formtools.wizard.views import SessionWizardView

from .models import Surveyor
from .forms import *

import pickle
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


class HomeViewWizard( SessionWizardView ):
    form_list = [SurveyorForm1, SurveyorForm2]
    instance = None

    def get_form_instance( self, step ):
        if self.instance is None:
            self.instance = Surveyor()
        return self.instance

    def get_template_names(self):
        return 'DjangoAPI/form.html'

    def done( self, form_list, **kwargs ):
        self.instance.save()
        STDE = form_list[0].cleaned_data['STDE']
        MTDE = form_list[0].cleaned_data['MTDE']
        SUDEM = form_list[0].cleaned_data['SUDEM']
        SUDEC = form_list[0].cleaned_data['SUDEC']
        MVDEH = form_list[0].cleaned_data['MVDEH']
        MVDEV = form_list[1].cleaned_data['MVDEV']
        MVDEA = form_list[1].cleaned_data['MVDEA']
        SVDEH = form_list[1].cleaned_data['SVDEH']
        SVDEV = form_list[1].cleaned_data['SVDEV']
        FD = form_list[1].cleaned_data['FD']
        df = pd.DataFrame({"STDE":[STDE],"MTDE":[MTDE],"SUDEM":[SUDEM],"SUDEC":[SUDEC],"MVDEH":[MVDEH],
                        "MVDEV":[MVDEV],"MVDEA":[MVDEA],"SVDEH":[SVDEH],"SVDEV":[SVDEV], "FD":[FD]})
        result = status(df)
        return render(self.request, 'DjangoAPI/status.html', {'data':result})
