from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse


# index
def index(request):
    return render(request, 'index.html')


# ajax_posting function
def ajax_posting(request):
    if request.is_ajax():
        first_name = request.POST.get('first_name', None) # getting data from first_name input
        last_name = request.POST.get('last_name', None)  # getting data from last_name input
        print(first_name)
        print(last_name)
        if first_name and last_name: #cheking if first_name and last_name have value
            response = {
                         'msg':'Your form has been submitted successfully' # response message
            }
            return JsonResponse(response) # return response as JSON

