from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Kineto_Kisom, Profile
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class Kineto_KisomAdmin(ImportExportModelAdmin):
    pass

# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)
# admin.site.unregister(TokenProxy)
admin.site.register(User, CustomUserAdmin)


admin.site.register(Kineto_Kisom, Kineto_KisomAdmin, list_display = ('artistname','trackname','net_royalty_total'))