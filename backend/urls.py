from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from django.shortcuts import redirect

def default_language_redirect(request):
    return redirect('index', language='uz')

urlpatterns = [
    path('', default_language_redirect),
    path("info/", views.info, name="info"),
    #path("qabul_xodim/", views.qabul_xodim, name="qabul_xodim"),
    path("qabul/document-<int:id>", views.qabul_document, name="qabul_document"),
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('success/', views.success, name='success'),
    path('error/', views.error, name='error'),
    path("<str:language>/coming_soon", views.coming_soon, name="coming_soon"),
    path("<str:language>/news-<int:page>", views.news, name="news"),
    path("<str:language>/employee-<int:id>/", views.employee_page, name="employee"),
    path("<str:language>/news/", views.news, name="news"),
    path("<str:language>/contact/", views.contact, name="contact"),
    path("<str:language>/", views.index, name="index"),
    path("<str:language>/news/<int:news_id>", views.news_detail, name="news_detail"),
    path("<str:language>/about/", views.about, name="about"),
    path("<str:language>/meyoriy_hujjatlar/", views.meyoriy_hujjatlar, name="meyoriy_hujjatlar"),
    path("<str:language>/umumiy_malumot/", views.umumiy_malumot, name="umumiy_malumot"),

    path("<str:language>/tuzilma/", views.tuzilma, name="tuzilma"),
    path("<str:language>/tuzilma/<str:tag>", views.tuzilma_teg, name="tuzilma_teg"),
    path("<str:language>/rektorat/", views.rektorat, name="rektorat"),
    path("<str:language>/ilmiy_hayot/ilmiy_faoliyat/", views.ilmiy_faoliyat, name="ilmiy_faoliyat"),
    path("<str:language>/ilmiy_hayot/konferensiya/", views.konferensiya, name="konferensiya"),
    path("<str:language>/ilmiy_hayot/ilmiy_tex_kengash/", views.ilmiy_tex_kengash, name="ilmiy_tex_kengash"),
    path("<str:language>/qabul/", views.qabul, name="qabul"),
    
]


# Настройте обработку статических файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
