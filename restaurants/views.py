from django.shortcuts import render

# Create your views here.
def home(request):
	context = {
	"msg":"hello world"
	}
	return render(request,'home.html',context)