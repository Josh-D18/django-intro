from django.shortcuts import render

# Create your views here.

def index(request):
  if request.POST:
    context = {
      'name': request.POST['name'],
      'email': request.POST['email'],
    }
    return render(request, 'thanks.html', context)
  context = {
    'results': [
      {'name': 'Fatima Lopez', 'email': 'f.lopez@email.com'},
      {'name': 'Gary Johnston', 'email': 'g.johnston@email.com'},
      {'name': 'Mari Gotze', 'email': 'mario.gotze23@gmail.com'},
      {'name': 'Gary Johnston', 'email': 'omar.ysuf12@yahoo.com'}
    ]
  }
  return render(request, 'index.html', context)
