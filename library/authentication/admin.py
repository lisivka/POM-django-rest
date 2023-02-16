from django.contrib import admin

from .models import CustomUser
from django import forms


class PersonAdminForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

    def clean_first_name(self):
        if self.cleaned_data["first_name"].find("admin") != -1:
            raise forms.ValidationError("Wrong name ")
        return self.cleaned_data["first_name"]


# admin.site.register(CustomUser)
@admin.register(CustomUser)
class AuthorAdmin(admin.ModelAdmin):
    form = PersonAdminForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["first_name"].label = "First Name (Ім'я):"
        form.base_fields["last_name"].label = "Last Name (Фамілія):"
        form.base_fields["middle_name"].label = "Middle Name (По батькові):"
        # form.base_fields["SAVE"].label = "Записати:"

        return form

    def save_model(self, request, obj, form, change):  # save password Hash
        if obj.pk:
            original_obj = CustomUser.objects.get(pk=obj.pk)
            if obj.password != original_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.save()

    list_per_page = 5
    list_max_show_all = 200
    date_hierarchy = "last_login"
    save_as_continue = True

    list_display = ('id', "email",
                    "first_name", "last_name", "is_active",
                    "created_at", "updated_at", "last_login",
                    "role",
                    "is_superuser", 'is_staff',
                    "password",
                    )
    list_editable = (
        "first_name", "last_name",
        "is_active",
    )
    list_display_links = ('id', "email",
                          # "first_name", "last_name",
                          "created_at", "updated_at", "last_login",
                          "role",
                          # "is_active", "is_superuser", 'is_staff',
                          "password",
                          )
    list_filter = ("is_active", "is_superuser", 'is_staff', 'id',
                   "first_name", "last_name",
                   "created_at", "updated_at",
                   "role",

                   )
    search_fields = ("email", "first_name", "last_name",)
    search_help_text = ("search_fields =  email, first_name, last_name")

    # fields = ("last_login", "email",
    #           "first_name", "last_name", "middle_name",
    #           # "created_at", "__updated_at",
    #           ("role",
    #            "is_active", "is_superuser", 'is_staff',
    #            ),
    #           "password",
    #           )
    readonly_fields = ("last_login",)
    fieldsets = (
        ('NOT Change',
         {
             "fields": (readonly_fields,)
         }),
        ('Change',
         {
             "fields": ("email",
                        "first_name", "last_name", "middle_name",
                        # "created_at", "__updated_at",
                        ("role", "is_active", "is_superuser", 'is_staff',),

                        )
         }),
        ('Password',
         {
             "classes": ("collapse",),
             "fields": ("password",)
         }),

    )
