from django import forms

from djangor.models import Entry


class EntryForm(forms.ModelForm):
    """allow entry of title and text for a post

    because required fields are missing from this form (author, pub_date),
    we will need to save the form without committing the object and then 
    set those values manually
    """

    class Meta:
        model = Entry
        fields = ('title', 'text', )
