from django.contrib import admin
from django.contrib.admin import ModelAdmin, SimpleListFilter

from author.models import Author
from .models import Book


class AuthorsFilter(SimpleListFilter):
    title = "Authors"  # a label for our filter
    parameter_name = "authors"  # you can put anything here

    def lookups(self, request, model_admin):
        # This is where you create filter options; we have two:
        res = []
        for author in Author.books.through.objects.all():
            value_to_append = (str(author.author.id),
                               str(author.author.name + " " + author.author.surname))
            print(value_to_append)
            if value_to_append not in res:
                res.append(value_to_append)
        return set(res)

    def queryset(self, request, queryset):
        # This is where you process parameters selected by use via filter options:

        for item in Author.books.through.objects.all():
            if self.value() == str(item.author.id):
                # Get websites that have at least one page.
                return queryset.distinct().filter(authors=self.value())

        if self.value():
            # Get websites that don't have any pages.
            return queryset.distinct().filter(authorsisnull=True)


class BooksInline(admin.TabularInline):
    model = Author.books.through
    extra = 0
    verbose_name = "Author"
    # fields = ("name","surname" )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    def author(self, obj):
        return [f"{author.name} {author.surname}" for author in obj.authors.all()]
        # return [f"[id={author.id}] {author.name} {author.surname}" for author in obj.authors.all()]

    list_per_page = 5
    list_max_show_all = 200

    list_display = ['id', 'name', 'count', 'author', "year", "date_of_issue", 'description', ]
    list_display_links = ['name', 'id', 'count', 'author', "year", "date_of_issue", 'description', ]
    inlines = [BooksInline, ]

    search_help_text = "search_fields = id,   name,   count,  description"
    search_fields = ('id', 'name', 'count', 'description',)
    list_filter = (
        AuthorsFilter, 'name', 'id', 'count', "year", "authors__patronymic", "authors__name", "authors__surname",)
    # list_filter = (AuthorsFilter, 'name', 'id', 'count', "authors__surname",)
    save_as = True
    save_as_continue = True
    actions_on_bottom = True
    # fields = ('name', 'description', "count")
    readonly_fields = ('name', "year")
    fieldsets = (
        ('Not Change',
         {
             'fields': readonly_fields
         }),
        ("Change",
         {
             "classes": ("collapse",),
             'fields': ('description', 'count', "date_of_issue",)
         }),
    )
