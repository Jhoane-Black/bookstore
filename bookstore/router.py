from webapp.views import AuthorViewset, BookViewset, ClientViewset, GenereViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('author',AuthorViewset)
router.register('book',BookViewset)
router.register('client',ClientViewset)
router.register('genere',GenereViewset)