from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'', include('accounts.urls')),
    url(r'', include('disciplines.urls')),
    url(r'', include('groups.urls')),
    url(r'', include('files.urls')),
    url(r'', include('modules.urls')),
    url(r'', include('questions.urls')),
    url(r'', include('grades.urls')),
    url(r'', include('peer_review.urls')),
    url(r'', include('practical_test.urls')),
    url(r'', include('exercises.urls')),
    url(r'', include('irat.urls')),
    url(r'', include('grat.urls')),
    url(r'', include('rank.urls')),
    url(r'', include('dashboard.urls'))
]

# While in development mode we will use relative URL for static and average
# files. In production mode we will no longer need this folder as we will store
# everything on a server
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
