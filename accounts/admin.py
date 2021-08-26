from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Kineto_Kisom, Profile, RBT_MAR, AltaFonte_MAR
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

class Kineto_KisomDataAdmin(ImportExportModelAdmin):
    pass
class RBT_MARDataAdmin(ImportExportModelAdmin):
    pass
class AltaFonte_MARDataAdmin(ImportExportModelAdmin):
    pass
# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)


admin.site.register(Kineto_Kisom, Kineto_KisomDataAdmin, list_display = ('ARTIST_NAME','CONTENT_NAME','NET_ROYALTY_TOTAL'))
admin.site.register(RBT_MAR, RBT_MARDataAdmin, list_display = ('ARTIST_NAME','CONTENT_NAME','REV_X_2'))
admin.site.register(AltaFonte_MAR, AltaFonte_MARDataAdmin, list_display = ('SERVICE_ID','COUNTRY','ARTIST_DISPLAY','TRACK_TITLE','NET'))