from django.contrib import admin
from django.urls import path, re_path
from tree_menu_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name='index'),
    re_path(r'^(?P<path>.*)$', index, name='index'),
]
