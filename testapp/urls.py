from django.urls import path
from .views import BlogView, BlogDetail, AddPost, PostLike, PostUnLike

urlpatterns = [
    #path('' ,BlogView),
    path('' ,BlogView.as_view(),name='home'),
    #path('blog/<postid>',BlogDetail,name='detail')
    path('blog/<pk>',BlogDetail.as_view(),name='detail'),
    path('additem', AddPost, name='additem'),
    #path('<int:num>',BlogDetail)
    path('like/<postid>', PostLike, name='postlike'),
    path('unlike/<postid>', PostUnLike, name='postunlike')
]

