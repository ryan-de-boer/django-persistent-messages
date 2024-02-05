from django.urls import path, re_path
from persistent_messages.views import message_detail, message_mark_read, message_mark_all_read

urlpatterns = [
    path('detail/<int:message_id>/', message_detail, name='message_detail'),
    re_path(r'^mark_read/(?P<message_id>\d+)/$', message_mark_read, name='message_mark_read'),
    path('mark_read/all/', message_mark_all_read, name='message_mark_all_read'),
]