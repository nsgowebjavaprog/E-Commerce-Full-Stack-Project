from django.http import JsonResponse

def home(request):
    data = {
        'message': 'welcome to the learning with project'
    }
    return JsonResponse(data)