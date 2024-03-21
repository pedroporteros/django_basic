from django.urls import path
from meetings import views

from meetings.views import CommentFormView

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('rooms', views.rooms_list, name="rooms"),
    path('new', views.new, name="new"),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('create', views.new, name="create"),
    path('comment', CommentFormView.as_view(), name='comment')
]
