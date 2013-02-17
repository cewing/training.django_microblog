from django.conf.urls import patterns, url
from django.views.generic import ListView


from djangor.models import Entry


urlpatterns = patterns('',
    # List view for all posts:
    url(r'^$',
        ListView.as_view(
            queryset=Entry.objects.all(),
            context_object_name="entries",
            template_name="djangor/entry_list.html"
        ),
        name="entry_list")
)