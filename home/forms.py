from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={
                "type": "name",
                "placeholder": "Your Name...",
                'name': 'name',
                'id': "name",
                "autocomplete": "on",
                "required":""
            }),
            "email": forms.TextInput(attrs={
                "placeholder": "Your E-mail...",
                'name': 'email',
                'id': "email",
                "required":"",
                "type": "text",
                "pattern": "[^ @]*@[^ @]*",
            }),
            'subject': forms.TextInput(attrs={
                "placeholder": "Subject..",
                'name': 'subject',
                'id': "subject",
                "required":"",
                "type": "subject",
                "autocomplete": "on"
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "Your Message...",
                "name": "message",
                "id": "message"
            })
        }

        