"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from student_management_system import settings
from student_management_app import views, hodviews

urlpatterns = [
    path('demo',views.showDemoPage),
    path('',views.LoginPage),
    path('admin/', admin.site.urls),
    path('get_user_details',views.GetUserDetails),
    path('logout',views.logout_user),
    path('doLogin', views.doLogin),
    path('admin_home', hodviews.admin_home),
    path('add_staff', hodviews.add_staff),
    path('add_staff_save', hodviews.add_staff_save),
    path('add_course', hodviews.add_course),
    path('add_course_save', hodviews.add_course_save),
    path('add_student', hodviews.add_student),
    path('add_student_save', hodviews.add_student_save),
    path('add_subject', hodviews.add_subject),
    path('add_subject_save', hodviews.add_subject_save),
    path('manager_staff', hodviews.manager_staff),
    path('manager_student', hodviews.manager_student),
    path('manager_course', hodviews.manager_course),
    path('manager_subject', hodviews.manager_subject),
    path('edit_staff/<str:staff_id>', hodviews.edit_staff),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
