from django.views.generic import TemplateView,FormView,ListView,CreateView 
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy, reverse 
from .models import Usuario
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render,render_to_response,redirect, RequestContext
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.template import RequestContext as RC
from django.contrib.auth.models import User
from Service.models import UserAQL


class Registrarse(FormView):
	template_name = 'registrarse.html'
	form_class = UserForm
	success_url = reverse_lazy('registrarse')

	def form_valid(self, form):
		uss = form.cleaned_data['username']
		uss2= user.objects.filter(username= uss)
		

		user = form.save() # aca tengo los datos del formulario # ACA GUARDO EL FORM Y COMO LO QUE VIENE YA ES UN USUARIO LO GUARDO EN UN USER 
		usuario = User() # aca inicializo una variable tipo usuario para cargarla con el form.
		Usuario.User = user  # ACA YA EMPIEZO A LLENAR LA TABLA PERFIL ONDA QUE LLENO LAS DOS TABLAS JUNTAS .
		Usuario.FirstName = form.cleaned_data['nombre']
		Usuario.LastName = form.cleaned_data['apellido']
		Usuario.Email = form.cleaned_data['email']
		Usuario.save()
		return HttpResponseRedirect('/categories')	


	# Create your views here.

class  Principal (TemplateView ): 
    template_name =  'principal.html'
def salir(request):
	logout(request)
	return HttpResponseRedirect("/login")
def enter(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/profile")
	if request.method== "POST":
	    username = request.POST['User']
	    password = request.POST['Pass']
	    user = authenticate(username=username, password=password)
	    if user is not None:
	        if user.is_active:
	            login(request, user)
	            return HttpResponseRedirect("/profile")
	        else:
	        	return render_to_response("login1.html",{'message':'usuario o contrasenia invalida'},context_instance = RC( request, {} ),)    	
	    else:
	        return render_to_response("login1.html",{'message':'ERROR Usuario o contrasenia invalida'},context_instance = RC( request, {} ),)
	else:
		return render(request,"login1.html")



def register(request, *args, **kwargs):
	if request.method== "POST":
		form = UserForm(request.POST,request.FILES)
		if form.is_valid:
			username = form['UserName'].value()
			if username:
				uss2= User.objects.filter(username= username)
				if uss2:
					string = " NOMBRE DE USUARIO EXISTENTE"
					uss2=''
					return render_to_response('registrarse.html', {'message': string, 'form' : form}, context_instance=RequestContext(request))
				else:
					password = form['Pass'].value()
					email = form['Email'].value()
					if email:
						mail=User.objects.filter(email=email)
						if mail:
							string = "EL EMAIL YA ESTA REGISTRADO"
							mail=''
							return render_to_response('registrarse.html', {'message3': string, 'form' : form}, context_instance=RequestContext(request))
						else:	
							fname = form['FirstName'].value()
							if fname:
								lname = form['LastName'].value()
								if lname:
									dni = form['DNI'].value()
									if dni:
										
										image = form['Image'].value()
										user = User.objects.create_user(username=username,email=email,password=password)
										user.is_staff = True
										userAQL = UserAQL(User=user,FirstName=fname,LastName=lname,DNI=dni,Image=image)
					 					user.save()
					 					userAQL.save()
										string =''	
								 		fname= ''	
										lname=''
										email=''
										uss2=''
										mail=''
										username=''
										#return HttpResponseRedirect("/login", {'message': "Gracias por Registrarse, Ya puede iniciar Sesion"})
										return render_to_response('login1.html', {'message2': "Gracias por Registrarse, Ya puede iniciar Sesion", 'form' : form}, context_instance=RequestContext(request))
										

									else:
										string="ESTE CAMPO ES OBLIGATORIO"
										dni=''
										return render_to_response('registrarse.html', {'message6': string, 'form' : form}, context_instance=RequestContext(request))


								else:
									string= "ESTE CAMPO ES OBLIGATORIO "
									lname=''
									return render_to_response('registrarse.html', {'message4': string, 'form' : form}, context_instance=RequestContext(request))


							else:
								string ="ESTE CAMPO ES OBLIGATORIO "
								fname=''
								return render_to_response('registrarse.html', {'message5': string, 'form' : form}, context_instance=RequestContext(request))
						


					else:
						string= "ESTE ES UN CAMPO OBLIGATORIO"
						email=''
						return render_to_response('registrarse.html', {'message3': string, 'form' : form}, context_instance=RequestContext(request))
			else:
				string= "ESTE ES UN CAMPO OBLIGATORIO"
				username=''
				return render_to_response('registrarse.html', {'message': string, 'form' : form}, context_instance=RequestContext(request))

					
						
				
		return render_to_response("registrarse.html",{'message7':'Campos Invalidos', 'form' : form},context_instance = RC( request, {} ),)		
	return render(request,"registrarse.html")


def Comment(request,Name,NameService):
	if request.method == 'GET':
		if request.user.is_authenticated():
			userAQL = UserAQL.objects.filter(User=request.user)
			print(userAQL)
			service = Service.objects.filter(NameService=NameService)
			opinion = request.GET['Comment']
			Comment = Comment(User=userAQL,Service=service,opinion=opinion)
			Comment.save()
			return HttpResponse('/Categories/'+Name+'/'+NameService+'/')




