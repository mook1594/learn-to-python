#### [GO TO BACK](../README.md)

# 10. 클래스 기반 뷰의 모범적인 이용

## 10.1 클래스 기반 뷰를 이용할 때의 가이드라인
- 뷰 코드의 양은 적으면 적을 수록 좋다.
- 뷰 안에서 같은 코드를 반복적으로 이용하지 말자.
- 뷰는 프리젠테이션 로직에서 관리하도록 하자. 비즈니스 로직은 모델에서 처리하자. 매우 특별한 경우에는 폼에서 처리하자.
- 뷰는 간단 명료 해야한다.
- 403, 404, 500 에러 핸들링에 클래스 기반 뷰는 이용하지 않는다. 대신 함수 기반 뷰를 이용
- 믹스인은 간단 명료 해야한다.

## 10.2 클래스 기반 뷰와 믹스인 이용하기
- 다중 상속을 해야할 때 믹스인을 사용
- 장고가 제공하는 기본 뷰는 항상 오른쪽으로 진행한다.
- 믹스인은 기본 뷰에서 부터 왼쪽으로 진행한다.
- 믹스인은 파이썬의 기본 객체 타입을 삭속해야만 한다.
- 예
``` python
from django.views.generic import TemplateView

class FreshFruitMixin(object):
    def get_context_data(self, **kwargs):
        context = super(FreshFruitMixin, self).get_context_data(**kwargs)
        context['has_fresh_fruit'] = True
        return context

class FruityFlavorView(FreshFruitMixin, TemplateView):
    template_name = 'fruity_flavor.html'
```

## 10.3 어떤 장고 제네릭 클래스 기반 뷰를 어떤 태스크에 이용할 것인가?
- View: 어디서든 이용 가능한 기본 뷰
- RedirectView: 사용자를 다른 URL로 리다이렉트
- TemplateView: 장고 HTML 템플릿을 보여줄 때
- ListView: 객체 목록
- DetailView: 객체를 보여줄 때
- FormView: 폼 전송
- CreateView: 객체를 만들때
- UpdateView: 객체를 업데이트 할 때
- DeleteView: 객체를 삭제 할 때
- GenericDateView: 시간 순서로 객체를 나열해서 보여줄 때

## 10.4 장고 클래스 기반 뷰에 대한 일반적인 팁
### 인증된 사용자에게만 장고 클래스 기분 뷰/제네릭 클래스 기반 뷰 접근 가능하게 하기
``` python
# views.py
from django.views.generic import DetailView

from vraces.views import LoginRequiredMixin

from .models import Flavor

class FlavorDetailView(LoginRequiredMixin, DetailView):
    model = Flavor
```
- LoginRequiredMixin은 가장 왼쪽에 위치한다.
- 베이스 뷰 클래스는 항상 가장 오른쪽에 위치 한다.

### 뷰에서 유효한 폼을 이용하여 커스텀 액션 구현하기
``` python
from django.views.generic import CreateView

from braces.views import LoginRequiredMixin

from .models import Flavor

class FlavorCreateView(LoginRequiredMixin, CreateView):
    model = Flavor
    fields = ('title', 'slug', 'scoops_remaining')

    def from_valid(self, form):
        return super(FlavorCreateView, self).formvalid(form)

```

### 뷰에서 부적합한 폼을 이용하여 커스텀 액션 구현하기
``` python
from django.views.generic import CreateView

from braces.views import LoginRequiredMixin

from .models import Flavor

class FlavorCreateView(LoginRequiredMixin, CreateView):
    model = Flavor

    def from_invalid(self, form):
        # 커스텀 로직이 이곳에 위치
        return super(FlavorCreateView, self).form_invalid(form)

```

### 뷰 객체 이용하기
``` python
from django.utils.functional import cached_property
from django.views.generic import UpdateView, TemplateView

from braces.views import LoginRequiredMixin

from .models import Flavor
from .tasks import update_users_who_favorited

class FavoriteMixin(object):

    @cached_property
    def likes_and_favorites(self):
        """ likes와 favorites의 딕셔너리를 반환"""
        likes = self.object.likes()
        favorites = self.object.favorites()
        return {
            "likes": likes,
            "favorites": favorites,
            "favorites_count": favorites.count(),
        }

class FlavorUpdateView(LoginRequriedMixin, FavoriteMixin, UpdateView):
    model = Flavor
    fields = ('title', 'slug', 'scoops_remaining')

    def form_valid(self, form):
        update_users_who_favorited(
            instance=self.object,
            favorites=self.likes_and_favorites['favorites']
        )
        return super(FlavorCreateView, self).form_valid(form)

class FlavorDetailView(LoginRequiredMixin, FavoriteMixin, TemplateView):
    model = Flavor
```

``` html
{# flavors/base.html #}
{% extends 'base.html' %}
{% block likes_and_favorites %}
<ul>
    <li>Likes: {{ view.likes_and_favorites.likes }}</li>
    <li>Favorites: {{ view.likes_and_favorites.favorites_count }}</li>
</ul>
{% endblock likes_and_favorites %}
```

## 10.5 제네릭 클래스 기반 뷰와 폼 사용하기
``` python
# models.py
from django.core.urlresolvers import reverse
from django.db import models

STATUS = (
    (0, 'zero'),
    (1, 'one'),
)

class Flavor(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    scoops_remaining = models.IntegerField(default=0, choices=STATUS)

    def get_absolute_url(self):
        return reverse('flavors:detail', kwargs={'slug': self.slug})

```

### 뷰 + 모델폼 예제
``` python
# views.py
class FlavorCreateView(LoginRequiredMixin, CreateView):
    model = Flavor
    fields = ('title', 'slug', 'scoops_remaining')

class FlavorUpdateView(LoginRequriedMixin, UpdateView):
    model = Flavor
    fields = ('title', 'slug', 'scoops_remaining')

class FlavorDetailView(DetailView):
    model = Flavor
```
- 믹스인을 사용하게 되면
``` python
# views.py
class FlavorActionMixin(object):
    fields = ('title', 'slug', 'scoops_remaining')

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(FlavorActionMixin, self).form_valid(form)

class FlavorCreateView(LoginRequiredMixin, FlavorActionMixin, CreateView):
    model = Flavor
    success_msg = 'Flavor created!'

class FlavorUpdateView(loginRequiredMixin, FlavorActionMixin, UJpdateView):
    model = Flavor
    success_msg = 'Flavor updated!'

class FlavorDetailView(DetailView):
    model Flavor

```

### 뷰 + 폼 예제
``` python
# views.py
class FlavorListView(ListView):
    model = Flavor

    def get_queryset(self):
        # 부모 get_queryset으로 부터 쿼리세트를 패치
        queryset = super(FlavorListView, self).get_queryset()

        # q GET 파라미터 받기
        q = self.request.GET.get('q')
        if q:
            # 필터된 쿼리세트 반환
            return queryset.filter(title__icontains=q)
        # 기본 쿼리세트 반환
        return queryset
```

## 10.6 django.views.generic.View 이용하기
``` python
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django. views.generic import View

from braces.views import LoginRequiredMixin

from .forms import FlavorForm
from .models import Flavor

class FlavorView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # Flavor 객체의 디스플레이를 처리
        flavor = get_object_or_404(Flavor, slug=kwargs=['slug'])
        return render(request, 'flavors/flavor_detail.html', {'flavor': flavor})

    def post(self, request, *args, **kwargs):
        # Flavor 객체의 업데이트를 처리
        flavor = get_object_or_404(Flavor, slug=kwargs['slug'])
        form = FlavorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('flavors:detail', flavor.slug)

class PDFFlavorView(LoginRequiredMixin, View):
    # 종류 할당
    flavor = get_object_or_404(Flavor, slug=kwargs['slug'])

    # 응답 생성
    response = HttpResponse(content_type='application/pdf')

    # PDF 스트림 생성 후 응답에 할당
    response = make_flavor_pdf(response, flavor)

    return response
```
