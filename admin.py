from django.contrib import admin

from {{ app_name }} import models


class ModelAdmin(admin.ModelAdmin):
    model = models.Model

    list_display = ("something",)

    def something(self, post):
        return post.something()
