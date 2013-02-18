from django.conf.urls import patterns, url
from django.views.generic import ListView


from djangor.models import Entry
from djangor.forms import EntryForm
from djangor.views import AddEntryView


urlpatterns = patterns('',
    # List view for all posts:
    url(r'^$',
        ListView.as_view(
            queryset=Entry.objects.all(),
            context_object_name="entries",
            template_name="djangor/entry_list.html"
        ),
        name="entry_list"),
    url(r'^add/$',
        AddEntryView.as_view(
            model=Entry,
            form_class=EntryForm,
            template_name="djangor/entry_form.html",
            success_url="/",
        ),
        name="add_entry"),
)