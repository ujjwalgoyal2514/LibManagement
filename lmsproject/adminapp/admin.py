from django.contrib import admin
from .models import IssueBook,BookStore,Program,Branch,Year

admin.site.register(BookStore)
admin.site.register(IssueBook)
admin.site.register(Program)
admin.site.register(Branch)
admin.site.register(Year)
# Register your models here.
