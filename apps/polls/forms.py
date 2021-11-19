from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from apps.polls.models import Exercise, Question, TYPES


class ExerciseForm(forms.Form):
    pass


class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=125, min_length=10, required=True)
    image = forms.ImageField(required=False)


class AnswerFormForCreator(forms.Form):
    answer_type = forms.ChoiceField(choices=TYPES)
    score = forms.IntegerField()
    answer_text = forms.CharField(max_length=60)
    is_valid = forms.BooleanField()


class AnswerFormForPupil(forms.Form):
    answer_input = forms.CharField()