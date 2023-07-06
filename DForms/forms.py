from django import forms

type=[('male',"Male"),('female',"Female"),('other',"Prefer not")]
stream=[('python',"Python"),('java',"Java"),('mern',"MERN"),('mean',"MEAN"),('sql',"SQL"),('html',"HTML"),('css',"CSS"),('js',"JS")]
class SignUp(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    # course=forms.MultipleChoiceField(choices=stream,widget=forms.CheckboxSelectMultiple)
    course=forms.MultipleChoiceField(choices=stream)
    email=forms.EmailField(required=True)
    password=forms.CharField(widget=forms.PasswordInput)
    # gender=forms.ChoiceField(choices=type,widget=forms.RadioSelect)
    gender=forms.ChoiceField(choices=type)
    address = forms.CharField(max_length=50,widget=forms.Textarea)

class Topic(forms.Form):
    topic=forms.CharField()

class Webpage(forms.Form):
    topic=forms.CharField()
    name=forms.CharField()
    url=forms.URLField()

class AccessRecord(forms.Form):
    name=forms.CharField()
    date=forms.DateField()
    author=forms.CharField()