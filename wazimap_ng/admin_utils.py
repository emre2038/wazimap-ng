import json

from django.forms.widgets import Widget
from django.contrib import admin

def customTitledFilter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper
    
def description(description, func):
    func.short_description = description
    return func


class SortableWidget(Widget):
    template_name = 'widgets/SortableWidget.html'

    class Media:
        css = {'all': ("/static/css/jquery-ui.min.css", "/static/css/sortable-widget.css",)}
        js = ("/static/js/jquery-ui.min.js", "/static/js/sortable-widget.js",)

    def get_context(self, name, value, attrs=None):
        values_list = []
        values = json.loads(value)

        return {'widget': {
            'name': name,
            'values': values
        }}

