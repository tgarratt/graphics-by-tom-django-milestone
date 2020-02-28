from django.conf.urls import url, include
from accounts.views import get_sign_in, get_sign_out, get_register
from accounts import url_reset

urlpatterns = [
    url(r'^sign_out$', get_sign_out, name='sign_out'),
    url(r'^login/$', get_sign_in, name='sign_in'),
    url(r'^register/$', get_register, name='register'),
    url(r'^password_reset/', include(url_reset)),
]