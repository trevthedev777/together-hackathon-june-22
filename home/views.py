''' View to render the home page '''

from django.shortcuts import render


def index(request):
    ''' Display the home page '''
    template = 'home/index.html'
    return render(request, template)
