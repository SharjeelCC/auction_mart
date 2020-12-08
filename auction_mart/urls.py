from django.conf.urls import url
from django.contrib import admin

from common.views import AccountLoginView, AccountSignup

urlpatterns = [
    url(r'^login/$', AccountLoginView.as_view(template_name="common/login.html"), name='login'),
    url(r'^signup/$', AccountSignup.as_view(template_name="common/signup.html"),  name='signup'),
    url(r'^admin/', admin.site.urls),
    
]
