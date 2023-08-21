from rest_framework import routers

from thoughts.views import NoteViewSet, CommentViewSet, ProfileViewSet
#router for notes managing
notes_router = routers.DefaultRouter()
notes_router.register(r'notes', NoteViewSet, basename='note')
#router for comments managing
comments_router = routers.DefaultRouter()
comments_router.register(r'comments', CommentViewSet, basename='comment')
#router for profiles(read only yet)
profiles_router = routers.DefaultRouter()
profiles_router.register(r'profiles', ProfileViewSet, basename='profile')
