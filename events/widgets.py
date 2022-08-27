from datetime import date, datetime
from time import time
from django import forms

class DatePickerInput(forms.DateInput):
    input_type: date

class DateTimeInput(forms.DateTimeInput):
    input_type: datetime

class TimeInput(forms.TimeInput):
    input_type: time