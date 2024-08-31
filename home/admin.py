from django.contrib import admin
from . models import Feedback
from django.utils.html import format_html
from .models import Complain
# from . models import BusinessPage
admin.site.site_header = "Swipe2Clean Admin's"
# admin.site.register(Feedback)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id','userr','uemail','ucomment')

@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    list_display = ('id','okmail','addr','comment','num','cause_image')

    def cause_image(slef, obj):
        return format_html('<img src="{0}" width="auto" height="150px">'.format(obj.image.url))

