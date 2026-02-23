from django.shortcuts import render

# Create your views here.

def login_view(request):
    print(request.method)
    print(request.POST)



    if request.method == 'POST':
        print(request.POST)

        
    return render(request, 'login_app/login.html')
