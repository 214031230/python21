"""CMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from fault_reporting import views
from django.views.static import serve
from django.conf import settings
from fault_reporting import urls as fault_report_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^index/$', views.index),
    url(r'^ooxx/', views.pcgetcaptcha),
    # 课件 ↓
    url(r'^register/$', views.RegisterView.as_view()),
    url(r'^logout/$', views.logout),
    # 故障总结主页面
    url(r'^fault-report/', include(fault_report_urls)),  # 以fault-report开头的所有路由都交给二级路由去处理
    # 给用户上传的那些文件的路径做一个对应关系
    url(r'^media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
]
