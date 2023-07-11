from django import forms
from DForms.models import *
# Create your forms here

# SignUp form creation
type=[('male',"Male"),('female',"Female"),('other',"Prefer not")]
stream=[('python',"Python"),('java',"Java"),('mern',"MERN"),('mean',"MEAN"),('sql',"SQL"),('html',"HTML"),('css',"CSS"),('js',"JS")]
class SignUp(forms.Form):
    name=forms.CharField(help_text='Enter name',max_length=100)
    age=forms.IntegerField(help_text='Enter age')
    # course=forms.MultipleChoiceField(choices=stream,widget=forms.CheckboxSelectMultiple,)
    course=forms.MultipleChoiceField(choices=stream,help_text='Select courses')
    email=forms.EmailField(help_text='Enter email')
    password=forms.CharField(widget=forms.PasswordInput,help_text='Enter password')
    # gender=forms.ChoiceField(choices=type,widget=forms.RadioSelect)
    gender=forms.ChoiceField(choices=type,help_text='Select gender')
    address = forms.CharField(max_length=100,widget=forms.Textarea,help_text='Enter address details')

# Topic form creation
class Topic(forms.Form):
    topic=forms.CharField(label='Topic Name',help_text='Enter topic name')

# Webpage form creation
class Webpage(forms.Form):
    class Meta:
        model = DTopic
        fields=['topic_name']
    topic=forms.ChoiceField(choices=[('topic','fields')],label='Select topic',help_text='Enter topic name')
    # topic=forms.CharField(label='Topic Name',help_text='Enter a topic name')
    name=forms.CharField(label='Name',help_text='Enter name')
    url=forms.URLField(label='URL',help_text='Enter URL')
  