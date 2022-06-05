from django.contrib import admin
from web.models import Profile , Analysis ,AnaysisStatus

# Register your models here.
class AnalysisAdmin(admin.ModelAdmin):
    list_display = ("data","status","created_at","user")

  
    @admin.display(empty_value="????")
    def data(self,obj):
        return obj.data

    @admin.display()
    def status(self,obj):
        
        return obj.status

    @admin.display(empty_value="????")
    def created_at(self,obj):
        return obj.created_at

    @admin.display(empty_value="????")
    def user(self,obj):
        return obj.user

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('due_date',"user","premium")

    
    @admin.display(empty_value="????")
    def user(self,obj):
        return obj.user

    @admin.display(empty_value="????")
    def premium(self,obj):
        return obj.premium

    @admin.display(empty_value="????")
    def due_date(self,obj):
        return obj.due_date

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Analysis,AnalysisAdmin)