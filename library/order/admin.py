from django.contrib import admin
from .models import Order
from django.utils.html import format_html


# admin.site.register(Order)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    def user_details(self, obj):
        return [obj.user.email, str(obj.user.first_name) + " " + str(obj.user.last_name)]

    def book_details(self, obj):
        return [obj.book.name + " - " + str(obj.book.description)]

    def view_user_link(self, obj):
        from django.utils.html import format_html
        user_id = obj.user.id
        user_last_name = obj.user.last_name
        user_first_name = obj.user.first_name
        user_email = obj.user.email
        return format_html(
            f'<a href="/admin/authentication/customuser/{user_id}">{user_id} {user_first_name} {user_last_name} {user_email}</a>')

    def view_book_link(self, obj):
        return format_html(
            f'<a href="/admin/book/book/{obj.book.id}">{obj.book.id} {obj.book.name} </a>')

    list_per_page = 5
    list_max_show_all = 200
    # date_hierarchy = "created_at"
    date_hierarchy = "end_at"
    empty_value_display = '---NOT returned!---'

    list_display = ('id', "view_user_link", "view_book_link", "book_details", "created_at", "plated_end_at", "end_at",)
    list_display_links = ('id', "book_details", "created_at", "plated_end_at", "end_at",)
    list_filter = ("user__email", "created_at", "plated_end_at", "end_at",)
