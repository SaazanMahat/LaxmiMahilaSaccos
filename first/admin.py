from django.contrib import admin

# Register your models here.
from django.contrib import admin

from first.models import Contact
from first.models import Notice, Slideshow, ScrollNews, Image, PostImage, Video, Report, Form, Statistic, PopUp, Loan, Saving, Other_program

admin.site.register(Contact)
admin.site.register(Notice)
admin.site.register(Slideshow)
admin.site.register(Report)
admin.site.register(Form)
admin.site.register(ScrollNews)
admin.site.register(Video)
admin.site.register(PopUp)
admin.site.register(Statistic)
admin.site.register(Loan)
admin.site.register(Saving)
admin.site.register(Other_program)


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Image)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Image


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
