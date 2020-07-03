from django.urls import path,include,re_path
from posts import views as posts_views




urlpatterns = [


    path("Uploadpic",posts_views.Uploadpic),
    re_path("addcomment",posts_views.addcomment,name="addcomment"),
    re_path("delete_post",posts_views.delete_post,name="delete_post"),
	path("Ratings/<int:postid>",posts_views.Ratings,name="Ratings"),
	path("Comments/<int:postid>",posts_views.Comments,name="Comments"),



]