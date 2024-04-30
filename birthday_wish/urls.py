from django.contrib import admin
from django.urls import path, include

admin.site.site_title = "Birthday Wish Admin Site"
admin.site.site_header = "Birthday Wish Administration"
admin.site.index_title = "Birthday Wish Administration"

urlpatterns = [
    path("admin/", admin.site.urls),
    path('users/', include('users.urls'))
]
