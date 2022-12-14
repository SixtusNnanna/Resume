from django.core.mail import send_mail
import logging
from django import forms

logger = logging.getLogger(__name__)

class ContactForm(forms.Form):
    name = forms.CharField(label = 'Your Name' ,max_length=100,)
    message = forms.CharField( max_length=600, widget=forms.Textarea)


    def send_mail(self):
        logger.info('Sending email to customer service')
        mesaage = 'From: {0} \n {1}'.format(self.cleaned_data['name'],
         self.cleaned_data['message'])

        send_mail('Site message',
         "\n".join(mesaage), 'site@booktime.domain',
          ['customerservice@booktime.domain'],
           fail_silently=True
        )