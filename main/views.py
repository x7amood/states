from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from main.models import State, City
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.views.generic import ListView,DetailView
from django.template import RequestContext
from django

def city_create(request):
	request_context= RequestContext(request)
	context={}
	if request.method == 'POST':
		form = CreateCityForm(request.POST)
		context['form']=form
		if form .is_valid():
			form.save()
			return render_to_response('city_search.html', context,context_instance=request_context)
		else:
			context['valid']=form.errors
			return render_to_response('city_search.html', context,context_instance=request_context)



def city_search(request):
	request_context = RequestContext(request)
	context = {}
	if request.method == 'POST':
		form = CitySearchForm(request.POST)
		context['form']=form
		if form.is_valid():
			name='%s' % form.cleaned_data['name']
			state=form.cleaned_data['state']
			context['city_list']=City.object.filter(name__startswith=name,state__name__startswith=state)
			return render_to_response('city_search.html', context,context_instance=request_context)
		else:
			context['valid']=form.errors
			return render_to_response('city_search.html', context,context_instance=request_context)
	else:
		form=CitySearchForm()
		context['form']= form
		return render_to_response('city_search.html', context,context_instance=request_context)
def template_view(request):

	context = {}
	states = State.objects.all()
	context['states'] = state

	return render(request, 'state_list.html',context)

def get_search(request):

	if request.method == 'GET':
		get_var = request.GET.get('city_name', None)
		print 'GET: %s ' %request.GET
		print 'POST: %s' % request.POST

		text_string = ''


		text_string = 'Search Term: %s <br>' % city_name
		text_string = """

		<form action="/get_search/" method="GET">
		Search Cities:

		<input type='text' name='city_name'>

		<br>

		<input type='submit' value="Submit">

		<br>

		</form?

	"""
class StateListView(ListView):
	model = State
	template_name = "state_list.html"
	context_object_name = 'states'

def state_detail(request, pk):
	state = State.objects.get(pk = pk)
	context['state'] = state_list
	return render(request,'state_detail.html',context)
	return HttpResponse(state)

def state_list(request):
	context = {}
	states = State.objects.all()
	context ['states'] = states

class StateDetailView(DetailView):
	models = State
	template_name = "state_detail.html"
	context_object_name = "state"

class CityEditForm(forms.ModelsForm):
	class Meta:
		model = City
		fields = '__all__'

@login_request
def citydelete(request, pk);
	City.objects.get(pk=pk).delete()

@login_required
def city_edit(request, pk):

    context = {}

    city = City.objects.get(pk=pk)

    form = CityEditForm(request.POST or None, instance=city)

    context['city'] = city
    context['form'] = form

    if form.is_valid():
   	    form.save()
	    return redirect('/state_list/')

	return render_to_response('city_edit.html', context, context_instance=RequestContext(request))




	# states = State.objects.all()

	# state_list = []

	# for state in states:

	# 	state_list.append("<a href='/state_detail/%s'>%s -- %s </a> <br>" % (state.name, state.name, state.statecapital.name))	

	# return HttpResponse(state_list)	

	# csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zip_codes_states.csv")  

