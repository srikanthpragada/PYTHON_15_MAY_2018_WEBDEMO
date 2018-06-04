from django import forms
from . import database

class AddCourseForm(forms.Form):
    title = forms.CharField( label="Course Title", max_length=50, required=True)
    duration = forms.IntegerField(label = "Course Duration", required=True, min_value=1)
    fee = forms.IntegerField(label = "Course Fee" , required=True, min_value=1000)


class AddTopicForm(forms.Form):
    topic = forms.CharField( label="Topic Name", max_length=50, required=True)
    duration = forms.IntegerField(label = "Topic Duration", required=True, min_value=1)
    # Dropdownlist with Title as text and Id as value
    course = forms.ChoiceField(label='Course', choices=database.get_course_titles())




