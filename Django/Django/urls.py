"""Django URL Configuration

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
from home import home_page, page_2, page_3, page_4, page_5, heros, page_6, page_7, page_8, page_10, page_11, page_9, segv, process_answer, trap, res_cs, cs
from .answers import result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home_page, name='home'),
    path('page_2', page_2, name='page2'),
    path('page_3', page_3, name='page3'),
    path('page_4', page_4, name='page4'),
    path('page_5', page_5, name='page5'),
    path('page_6', page_6, name='page6'),
    path('page_7', page_7, name='page7'),
    path('page_8', page_8, name='page8'),
    path('page_9', page_9, name='page9'),
    path('page_10', page_10, name='page10'),
    path('page_11', page_11, name='page11'),
    path('heros', heros, name='heros'),
    path('result', result, name='result'),
    path('segv', segv, name='segv'),
    path('trap', trap, name='trap'),
    path('res_cs', res_cs, name='res_cs'),
    path('cs', cs, name='cs'),
    path('process_answer/<int:id>', process_answer, name='process_answer'),
]
