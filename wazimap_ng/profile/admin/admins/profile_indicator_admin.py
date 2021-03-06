from django.contrib.gis import admin
from django.contrib.postgres import fields
from adminsortable2.admin import SortableAdminMixin

from ... import models
from ..forms import ProfileIndicatorAdminForm

from wazimap_ng.general.widgets import customTitledFilter, description, SortableWidget
from wazimap_ng.datasets.models import Indicator, Dataset
from wazimap_ng.general.admin.admin_base import BaseAdminModel

@admin.register(models.ProfileIndicator)
class ProfileIndicatorAdmin(SortableAdminMixin, BaseAdminModel):
    list_filter = (
        ('profile__name', customTitledFilter('Profile')),
        ('subcategory__category__name', customTitledFilter('Category')),
        "subcategory",
    )

    list_display = (
        "profile",
        "label", 
        description("Indicator", lambda x: x.indicator.name), 
        description("Category", lambda x: x.subcategory.category.name),
        "subcategory",
        "order",
    )

    fieldsets = (
        ("Database fields (can't change after being created)", {
            'fields': ('profile', 'indicator')
        }),
        ("Profile fields", {
          'fields': ('label', 'subcategory', 'description', 'choropleth_method')
        }),
        ("Subindicators", {
          'fields': ('subindicators',)
        })
    )

    form = ProfileIndicatorAdminForm

    formfield_overrides = {
        fields.JSONField: {"widget": SortableWidget},
    }
    help_texts = ["choropleth_method", ]

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ("profile",) + self.readonly_fields
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        if not change:
            obj.subindicators = obj.indicator.subindicators
        super().save_model(request, obj, form, change)