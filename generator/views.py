from django.shortcuts import render

# Create your views here.
def generators(request):
    return render(request, 'generator/geneators.html')