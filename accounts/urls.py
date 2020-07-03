from django.urls import path,include,re_path
from accounts import views as accounts_views




urlpatterns = [
    path("Logout",accounts_views.Logout),
    path('Home',accounts_views.home, name='Home'),
    
    path("Search",accounts_views.search,name="Search"),



    path("PicQuaR",accounts_views.PicQuaR,name="PicQuaR"),
    path("Rankings",accounts_views.Rankings,name="Rankings"),

    path("update_profile_pic",accounts_views.update_profile_pic,name="update_profile_pic"),


    
    path("u/<str:username>/",accounts_views.profile,name="profile"),
]