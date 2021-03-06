from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, edit_profile
from accounts import url_reset

urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^signup/$', registration, name='signup'),
    url(r'^profile/$', user_profile, name='profile'),
    url(r'^edit_profile/$', edit_profile, name='edit_profile'),
    url(r'^password-reset/', include(url_reset))
    ]