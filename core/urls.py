from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n'))
]


urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),

    path('', include('base.urls', namespace='base')),
    path('course/', include('courses.urls', namespace='course')),
    path('category/', include('categories.urls', namespace='category')),
    path('account/', include('accounts.urls', namespace='account')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('quiz/', include('quiz.urls', namespace='quiz')),
    path('admissions/', include('admissions.urls', namespace='admissions')),
    path('scientific-researches/', include('researches.urls', namespace='researches')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)