from django.contrib import admin
from .models import Listing # Listing come from models.py class name

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor' )
    # click on title and id(we can add anything) to navigate from dataBase to website 
    list_display_links = ('id', 'title')
    # add filter by realtor name 
    list_filter = ('realtor',)
    # add checkbox functionality 
    list_editable = ('is_published', )
    # search box
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')

    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
