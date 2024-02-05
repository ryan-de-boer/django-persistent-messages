from django.conf.urls import url
from persistent_messages.views import message_detail, message_mark_read, message_mark_all_read

urlpatterns = [
    url('detail/<int:message_id>/', message_detail, name='message_detail'),
    url(r'^mark_read/(?P<message_id>\d+)/$', message_mark_read, name='message_mark_read'),
    url('mark_read/all/', message_mark_all_read, name='message_mark_all_read'),
]