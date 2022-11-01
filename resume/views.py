import django
from django.shortcuts import render
from django.views.generic.edit import FormView
from resume import forms
from . models import Language, Education, Expertise, Skills,Profile

def Index(request):
    language = Language.objects.all()
    education = Education.objects.all()
    expertise = Expertise.objects.all()
    skill = Skills.objects.all()
    profile = Profile.objects.all()

    return render(request,'resume/index.html', {'language':language, 'education':education, 
    'expertise':expertise, 'skill':skill, 'profile': profile} )



class ContactFormView(FormView):
    template_name = "resume/index.html"
    form_class = forms.ContactForm
    success_url = ('/')


    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)
