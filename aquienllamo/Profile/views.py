from django.shortcuts import render
from login.forms import ServiceForm
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from Service.models import UserAQL,Service,Category
from django.http import HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.template import RequestContext, loader



class Registrarse(FormView):
	template_name = 'registrarProveedor.html'
	form_class = ServiceForm
	success_url = reverse_lazy('registrarse')
# Create your views here.

def Profile(request):
	if request.user.is_authenticated():
		return render(request,"principal.html")
	return HttpResponseRedirect("/login")


def RegisterProveedor(request):
	return render(request,"registrarProveedor.html")


def register(request):
	if request.method== "POST":
		form = ServiceForm(request.POST,request.FILES)
		if form.is_valid:
			NameService= form['NameService'].value()
			if NameService:
				cat=form['Category'].value()
				category=Category.objects.get(Name=cat)
				DescriptionService=form['DescriptionService'].value()
				if DescriptionService:
					Phone=form['Phone'].value()
					if Phone:
						if Phone.isdigit():
							EmailField=form['Email'].value()
							Adress=form['Adress'].value()
							Image=form['Image'].value()
							userAQL=UserAQL.objects.get(User=request.user)
							service=Service(NameService=NameService,Category=category,DescriptionService=DescriptionService,Phone=Phone,Email=EmailField,Adress=Adress,Image=Image,User=userAQL)
							service.save()
							NameService=''
							DescriptionService=''
							Phone=''
							return render_to_response('principal.html', {'message2': "GRACIAS POR REGISTRAR SU SERVICIO", 'form' : form}, context_instance=RequestContext(request))	
								
						else:
							string="ESTE ES UN CAMPO NUMERICO"
							return render_to_response('RegistrarProveedor.html', {'message4': string, 'form' : form}, context_instance=RequestContext(request))

					else:
						string="ESTE ES UN CAMPO OBLIGATORIO"
						return render_to_response('RegistrarProveedor.html', {'message4': string, 'form' : form}, context_instance=RequestContext(request))	

				else:
					string="ESTE ES UN CAMPO OBLIGATORIO"
					return render_to_response('RegistrarProveedor.html', {'message3': string, 'form' : form}, context_instance=RequestContext(request))
					
			else:
				string= "ESTE ES UN CAMPO OBLIGATORIO"
				return render_to_response('RegistrarProveedor.html', {'message1': string, 'form' : form}, context_instance=RequestContext(request)) 



	return render(request,"registrarse.html")



