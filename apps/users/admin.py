from django.contrib import admin


from .models import UserProfile

# Register your models here.




class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile,UserProfileAdmin)