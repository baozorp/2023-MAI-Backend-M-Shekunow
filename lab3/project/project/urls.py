# project/project/urls.py
from django.urls import path, re_path
from django.contrib import admin
urlpatterns = [
   path('', index, name='index'),
   re_path(r'^$', 'chats.views.index',
                  name='index'),
   path('chats/', include('chats.urls')),
   path('admin/', admin.site.urls),
]

# project/project/urls.py
from chats.views import chat_list
urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('category/<int:pk>/',
         'chat_category',
         name='chat_category'),
    path('<chat_id>/', 'chat_detail', name='chat_detail'),
]
