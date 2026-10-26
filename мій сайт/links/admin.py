from django.contrib import admin

from .models import ProfileLink, SiteProfile


class ProfileLinkInline(admin.TabularInline):
    model = ProfileLink
    extra = 0
    fields = ("title", "url", "sort_order", "is_active")
    ordering = ("sort_order", "id")


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Profile", {"fields": ("display_name", "username", "quote", "avatar_url")}),
    )
    inlines = (ProfileLinkInline,)

    def has_add_permission(self, request):
        return not SiteProfile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
