" Platzigram URL module "
#from django.urls import path
#from platzigram import views as local_views
#from posts import views as posts_views
#from django.contrib import admin
#from django.conf.urls.static import static
#from django.urls import path,include
#from django.conf import settings
#from users import views as users_views


#path('', posts_views.list_posts, name='feed'),
    #path('posts/new/', posts_views.create_post, name='create_post'),

    #path('users/login/', users_views.login_view, name='login'),
    #path('users/logout/', users_views.logout_view, name='logout'),
    #path('users/signup/', users_views.signup, name='signup'),
    #path('users/me/profile/', users_views.update_profile, name='update_profile')

"""Platzigram URLs module."""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('users/', include(('users.urls', 'users'), namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)