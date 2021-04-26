#### [GO TO BACK](../README.md)

# 2. Let's build our back-end web app
```shell
python manage.py startapp stores
```
### model.py
```python
class Pizzeria(models.Model):
    pizzeria_name = models.CharField(max_length=200, blank=False)
    street = models.CharField(max_length=400, blank=True) 
    city = models.CharField(max_length=400, blank=True) 
    state = models.CharField(max_length=2, null=True, blank=True)
    zip_code = models.IntegerField(blank=True, default=0) 
    website = models.URLField(max_length=420, blank=True) 
    phone_number = models.CharField(validators=[RegexValidator(regex=r'^\1?\d{9,10}$')], max_length=10, blank=True)
    description = models.TextField(blank=True) 
    logo_image = models.ImageField(upload_to='pizzariaImages', blank=True, default="pizzariaImages/pizzalogo.png" )
    email = models.EmailField(max_length=245, blank=True) 
    active = models.BooleanField(default=True)

def __str__(self):
    return "{}, {}".format(self.pizzeria_name, self.city)
```
### root/urls.py
```python
urlpatterns = [
    path('', include('stores.urls')),
]
```
### View Lists
##### serializer.py
```python
class PizzeriaListSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Pizzeria 
        fields = [
            'id', 
            'logo_image', 
            'pizzeria_name', 
            'city', 
            'zip_code', 
            'absolute_url'
        ]
```
##### views.py
```python
class PizzeriaListAPIView(generics.ListAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaListSerializer

```
##### stores/urls.py
```python
urlpatterns = [ 
    path('', views.PizzeriaListAPIView.as_view(), name="pizzeria_list"), 
]
```
### View Detail
##### serializer.py
```python
class PizzerialDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'pizzeria_name'
            'street',
            'city',
            'state',
            'zip_code',
            'website',
            'phone_number',
            'description',
            'logo_image',
            'email',
            'active',
        ]
```
##### views.py
```python
class PizzeriaRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer
```
##### stores/urls.py
```python
urlpatterns = [ 
    path('<int:id>/', views.PizzeriaRetrieveAPIView.as_view(), name='pizzeria_detail')
]
```
### Create View
##### serializers.py
- PizzeriaDetailSerializer
##### views.py
```python
class PizzeriaCreateAPIView(generics.CreateAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer
```
##### urls.py
```python
urlpatterns = [
    path('create/', views.PizzeriaCreateAPIView.as_view(), name="pizzeria_create")
]
```
### Update View
##### serializers.py
- PizzeriaDetailSerializer
##### views.py
```python
class PizzeriaRetrieveUpdateAPIView(generics.RetrieveUpdateApiView):
    lookup_field = 'id'
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer
```
##### urls.py
```python
urlpatterns = [
    path('update/<int:id>/', views.PizzeriaRetrieveUpdateAPIView.as_view(), name='pizzeria_update')
]
```
### Delete View
##### views.py
```python
class PizzeriaDestroyAPIView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Pizzeria.objects.all()
```
##### urls.py
```python
urlpatterns = [
    path('delete/<int:id>/', views.PizzeriaDestroyAPIView.as_view(), name="pizzeria_delete")
]
```
