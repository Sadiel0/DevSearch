from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
projectsList = [
    {
        'id':'1', 
        'title':'Manifest',
        'description':'Meditate and Find your inner self'
    }, 
    {
        'id':'2', 
        'title':'Python App',
        'description':'Cool stuff made with python'
    },
     {
        'id':'3', 
        'title':'Backend for a big website',
        'description':'Backend for the top 5 company'
    },
]
def projects(request):

    page =  'Projects'
    number = 10 
    context = {'page': page, 'number': number, 'projects':projectsList}
    return render(request, 'projects/projects.html',context)

def project(request,pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})   