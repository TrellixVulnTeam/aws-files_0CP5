from django.contrib import admin
from . models import User, Article
from django import forms
from django.db import models
#from data_migrate.widgets import RichTextEditorWidget

# class ArticleInline(admin.TabularInline):
#      model = Article
#      extra = 3

# @admin.register(Article)
# class ArticleUser(admin.ModelAdmin):
#     raw_id_fields = ('user', )
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe


# class UserAdmin(admin.ModelAdmin):
#     readonly_fields = ('full_name_details', )

#     def full_name_details(self, instance):
#         return instance.full_name

#     full_name_details.short_description = 'full_name_details'

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'full_name']
    date_hierarchy = 'date_of_birth'
    empty_value_display = '-empty-'
admin.site.register(User, UserAdmin)

def make_action(modeladmin, request, queryset):
    queryset.update(status='p')

make_action.short_description = 'update_action'

class ArticleUser(admin.ModelAdmin):
    list_display = ['title', 'body', 'status']
    actions = [make_action]

admin.site.register(Article, ArticleUser)
# class UserAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Name', {'fields': ['full_name']})
#     ]
#     inlines = [ArticleInline]

# admin.site.register(User, UserAdmin)






# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_select_related = ('user', )

"""
class UserForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = ['date_of_birth']
"""
# from django.contrib.admin import FieldListFilter

# @admin.register(User)
# class AdminUser(admin.ModelAdmin):
#     search_fields = ['first_name', 'last_name']
#     empty_value_display = 'unknown'
#     list_display = ('first_name', 'last_name', 'date_of_birth')
#     list_display_links = ('last_name', )
#     list_editable = ('first_name',)
#     list_filter = (('first_name', admin.BooleanFieldListFilter), 'last_name')
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(author=request.user)
    # # list_display = ('username',)

    # def username(self, obj):
    #     return ("%s %s " % (obj.first_name, obj.last_name)).upper()
    #list_display = ('first_name', 'date_of_birth', 'full_name')
    # formfield_overrides = {
    #     models.TextField: {'widget': RichTextEditorWidget},
    # }
    #form = UserForm
    #date_hierarchy = 'pub_date'
    #fields = (('full_name', 'date_of_birth'), 'last_name')
    #exclude = ('full_name',)

#admin.site.register(User, AdminUser)


"""
class Person(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()

    def decade_born_in(self):
        return self.birthday.strftime('%Y')[:3] + "0's"
    decade_born_in.short_description = 'Birth decade'

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'decade_born_in')

"""


# from django.utils.html import format_html
# from django.db.models import Value
# from django.db.models.functions import Concat

# class Person(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     color_code = models.CharField(max_length=6)

    # def my_property(self):
    #     return self.first_name + ' ' + self.last_name
    # my_property.short_description = "Full name of the person"

    #full_name = property(my_property)
    
    # def colored_name(self):
    #     return format_html(
    #         '<span style="color: #{};">{} {}</span>',
    #         self.color_code,
    #         self.first_name,
    #         self.last_name,
    #     )
    
    # def colored_name(self):
    #     return ("%s " % self.color_code)
    #colored_name.admin_order_field = Concat('first_name', Value(' '), 'last_name')

# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('colored_name', )
#admin.site.register(Person, PersonAdmin)
