from django import forms

class AddCourseForm(forms.Form):
    title = forms.CharField( label="Course Title", max_length=50, required=True)
    duration = forms.IntegerField(label = "Course Duration", required=True, min_value=1)
    fee = forms.IntegerField(label = "Course Fee" , required=True, min_value=1000)




