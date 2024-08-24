from ninja import NinjaAPI
from rural_producers.api import router as rural_producers_router

api = NinjaAPI()

@api.get('/')
def server_health_check(request):
    return {
        'message': 'online'
    }
    
api.add_router('/rural-producers', rural_producers_router)