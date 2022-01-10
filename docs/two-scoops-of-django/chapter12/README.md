#### [GO TO BACK](../README.md)

# 12. 폼 패턴들
### 유용한 폼 관련 패키지들
- django-floppyforms: 장고 폼을 html5로 렌더링
- django-crispy-forms
- django-forms-bootstrap: crispy-forms와 충돌 발생할 수도 있음

## 패턴 1: 간단한 모델폼과 기본 유효성 검사기
- ModelForm 기본 유효성 검사기를 있는 그대로 수정 없이 이용

``` python
# views.py
from django.view.generic import CreateView, UpdateView

from braces.views import LoginRequiredMixin

from .models import Flavor

class FlavorCreateView(LoginRequiredMixin, CreateView):
    model = Flavor
    fields = ('title', 'slug', 'scoops_remaining')

class FlavorUpdateView(LoginRequriedMixin, UpdateView):
    model = Flavor
    fields = ('title', 'slug', 'scoops_remaining')
```

## 패턴 2: 모델 폼에서 커스텀 폼 필드 유혀성 검사기 이용하기
``` python
# validators.py
from django.core.exceptions import ValidationError

def validate_tasty(value):
    """단어가 'Tasty'로 시작하지 않으면 ValidationError를 일으킨다."""
    if not value.startswith(u'Tasty'):
        msg = u'Must start with Tasty'
        raise ValidationError(msg)
```

### 여러 모델에 적용하기 위한 방법
``` python
# core/models.py
from django.db import models

from .validators import validate_tasty

class TastyTitleAbstractModel(models.Model):
    title = models.CharField(max_length=255, validators=[validate_tasty])

    class Meta:
        abstract=True
```
``` python
# models.py
from django.core.urlresolvers import reverse
from django.db import models

from core.models import TastyTitleAbstractModel

class Flavor(TastyTitleAbstractModel):
    slug = models.SlugField()
    scoops_remaining = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('flavors:detail', kwargs={'slug': self.slug})
```
- 폼에만 validation 체크를 하고 싶다면?
- 타이틀 말고 다른 필드에 적용하고 싶다면?
- ! 커스텀 폼을 만든다
``` python
from django import forms
from core.validators import validate_tasty
from .models import Flavor

class FlavorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FlavorForm, self).__init__(*args, **kwargs)
        self.fields['title'].validators.append(validate_tasty)
        self.fields['slug'].validators.append(validate_tasty)

    class Meta:
        model = Flavor
```

``` python
# views.py
from django.contrib import messages

class FlavorActionMixin(object):
    model = Flavor
    fields = ('title', 'slug', 'scoops_remaining')

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(FlavorActionMixin, self).form_valid(form)

class FlavorCreateView(LoginRequiredMixin, FlavorActionMixin, CreateView):
    success_msg = 'created'
    # FlavorForm 클래스를 명시적으로 추가
    form_class = FlavorForm

class FlavorUpdateView(LoginRequriedMixin, FlavorActionMixin, UpdateView):
    success_msg = 'updated'
    # FlavorForm 클래스에 명시적 추가
    form_class = FlavorForm

class FlavorDetailView(DetailView):
    model = Flavor
```

## 패턴 3: 유효성 검사의 클린 상태 오버라이딩 하기
- clean() 메서드는 어떤 특별한 필드에 대한 정의도 가지고 있지 않기 때문에 두 개 또는 그 이상 필드들에 대해 서로 간의 유효성을 검사하는 동간이 된다.
- clean 유효성 검사 상태는 영속성 데이터에 대해 유효성을 검사하기 좋은 장소다. 이미 유효성 검사를 일부 마친 데이터에 대해 불필요한 데이터베이스 연동을 줄일 수 있다.

``` python 
# forms.py
from django import forms
from flavors.models import Flavor
class IceCreamOrderForm(forms.Form)
    """일반적으로 forms.ModelForm을 이용하면 된다. 하지만 모든 종류의 폼에서 이와 같은 방식을 적용할 수 있음을 보이기 위해 forms.Form을 이용했다.
    """

    slug = forms.ChoiceField('Flavor')
    toppings = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(IceCreamOrderForm, self).__init__(*args, **kwargs)
        self.fields['slug'].choices = [
            (x.slug, x.title) for x in Flavor.objects.all()
        ]

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if Flavor.objects.get(slug=slug).scoops_remaining <= 0:
            msg = u'Sorry, we are out of that flavor'
            raise forms.ValidationError(msg)
        return slug

    def clean(self):
        cleaned_data = super(IceCreamOrderForm, self).clean()
        slug = cleaned_data.get('slug', '')
        toppings = cleaned_data.get('toppings', '')

        if u'chocolate' in slug.lower() and \
            u'chocolate' in toppings.lower():
            msg = u'Your order has too much chocolate.'
            raise forms.ValidationError(msg)
        return cleaned_data
```

## 패턴 4: 폼 필드 해킹하기(두개의 CBV, 두 개의 폼, 한 개의 모델)
- model에 필수값이 아닌 필드를 Update시에는 필수값으로 지정해야할때 Form 에서 코드를 반복하지말고 아래와 같이 해결하자
``` python
# forms.py
from django import forms

from .models import IceCreamStore

class IcceCreamStoreUpdateForm(forms.ModelForm):
    class Meta:
        model = IceCreamStore
        fields = ('title', 'block_address', 'phone', 'description')

    def __init__(self, *args, **kwargs):
        super(IceCreamStoreUpdateForm, self).__init__(*args, **kwargs)
        self.fields['phone'].requried = True
        self.fields['description'].required = True
```
* [Meta.fields를 이용하되 Meta.exclude는 이용하지 말자](../chapter26/README.md)


## 패턴 5: 재사용 가능한 검색 믹스인 뷰
``` python
# core/views.py
class TitleSearchMixin(object):
    def get_queryset(self):
        queryset = super(TitleSearchMixin, self).get_queryset()

        q = self.request.GET.get('q')
        if q:
            return queryset.filter(title__icontains=q)
        return queryset
```
``` python
# views
class FlavorListView(TitleSearchMixin, ListView):
    model = Flavor

# views
class IceCreamStoreListView(TitleSearchMixin, ListView):
    model = Store
```
``` html
<!-- store_list.html --> 
<form action="" method="GET">
    <input type="text" name="q" />
    <button type="submit">search</button>
</form>

<!-- flavor_list.html --> 
<form action="" method="GET">
    <input type="text" name="q" />
    <button type="submit">search</button>
</form>
```