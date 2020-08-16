from django.shortcuts import render

def index(request):
	
	if(request.method=='POST'):
		ls=[]
		num1=request.POST.get('number1')
		num2=request.POST.get('number2')
		print (num1)
		print(num2)
		for i in range(int(num1),int(num2)+1 ):
			ls.append(i)
		return render(request, 'app1/homepage.html', context={'ls':ls})
	elif(request.method=='GET'):
		ls=[]
		for j in range(1,21):
			ls.append(j)
		return render(request,'app1/homepage.html',context={'ls':ls})


  
 