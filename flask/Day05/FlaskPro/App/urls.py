from App.exts import api
from App.views import *

api.add_resource(Home, '/')
api.add_resource(PersonsResource, '/haha/')
api.add_resource(Person2Resource, '/haha2/', endpoint='id')
api.add_resource(Person3Resource, '/haha3/')
api.add_resource(Person4Resource, '/haha4/')