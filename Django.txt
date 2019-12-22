 Django

    1. Create <project folder> and enter the folder
    2. Virtual environment
        a. virtualenv venv
        b. virtualenv venv -p python3
    3. Activate
        a. source venv/bin/activate
    4. Make directory src then enter to  src 
        a. mkdir src 
        b. cd src
    5. Install django and create project
        a. pip install django==1.11.15
        b. pip install pillow psycopg2    (  psycopg2-binary  )
        c. django-admin.py startproject  <project folder name>
    6. Change dir to  <project folder name>
        a. cd <project folder name>
        b. mkdir static media templates
        c. python manage.py runserver




    1. To activate virtualenv
        a. source ../../venv/bin/activate
    2. To open python shell
        a. python manage.py shell
    3. Create a new App
        a. python manage.py startapp <app name>



    1. Create database and user in phppgadmin
        a. sudo su postgres
        b. createdb <dbname>  
        c. createuser shibil -P
            i.  femmepk -> shibil -> 12345
        d. psql
        e. grant all privileges on database femmepk to shibil;
        f. \q
        g. exit
    2. Create super user
        a. python manage.py createsuperuser
            i. shibil -> shibil789
    3. Migration comments
        a. python manage.py makemigrations
        b. python manage.py migrate
        c. python manage.py loaddata initial_data user_groups permissions notification
    4. Delete migration
        a. find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
        b. find . -path "*/migrations/*.pyc"  -delete
    5. Read and write from file
        a. pip freeze > r.txt
        b. pip install -r r.txt
        c. python manage.py loaddata initial_data user_groups permissions notification







Django documentation notes


    1. Models objects return functions
        a. all()
        b. filter() 	
            i. filter value ( instance= , )
        c. exclude()
            i. To avoid some fields
        d. get() 
            i. for one value 
    2. Models objects create functions
        a. create()
    3. Forms for single line
        a. for field in form:
field.id_for_label   ||  field.label  ||  field
endfor
        b. form.as_p
    4. Form validation views.py(function)
    a. if request.method=="POST":
    	name = request.POST.get('name')
    	email = request.POST.get('email')
    	
    	FormClassName.objects.create(
        	name = name,
        	email = email,
    	)
    	return HttpResponse('Form Submitted')
	else:
    		return HttpResponse('Invalid Request')



Django Pagination
    1. pip install django-el-pagination
    2. Register at INSTALLED_APP in setting -
        a. ‘el_pagination ’
    3.  In template
        a. {% load el_pagination_tags %}
        b.  {% paginate 21 instances %}
        c. set loader temp

Auto Complete
    1. From App
        a. urls.py	
            i. from whichapp.views import NameAutocomplete
            ii. urlpatterns = [	url(r'^anyname-autocomplete/$',NameAutocomplete.as_view(),name='urlname_autocomplete',),
        b. views.py
            i. from dal import autocomplete
            ii. class NameAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
    	if not self.request.user.is_authenticated():
        	return whichapp.objects.none()

    	items = whichapp.objects.filter(is_deleted=False)

    	if self.q:
        	query = self.q
        	items = items.filter(Q(name__icontains=query) | Q(phone__icontains=query) | Q(email__icontains=query) | Q(address__icontains=query)
)

    	return items
    2. To App
        a. forms.py
            i.         	'fieldname' : autocomplete.ModelSelect2(url='mainappulrname:urlname_autocomplete ',attrs={'data-placeholder': 'Product','data-minimum-input-length': 0},),

    3. {{ formname.media }}


User Authentication
    1. pip install django-registration-redux
    2. In main setting
        a. register app -  ‘registration’,
        b. LOGIN_URL = '/seturl/url/'
LOGOUT_URL = '/seturl/url/'
LOGIN_REDIRECT_URL = '/'
    3. main url.py
        a. 	url(r'^app/accounts/', include('registration.backends.default.urls')),
    4. 

