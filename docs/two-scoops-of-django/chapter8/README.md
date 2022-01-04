#### [GO TO BACK](../README.md)

# 8. 함수 기반 뷰와 클래스 기반 뷰

## 8.1 함수 기반 뷰와 클래스 기반 뷰를 각각 언제 이용할 것인가?
### 어떤 뷰를 선택할까
- 범용적인 클래스 기반 뷰들의 구조 중 하나가 이미 머리에 떠올랐는가?
- 속성(attribute) 오버라이딩만으로 클래스 기반 뷰가 가능하겠는가?
- 다른 뷰를 생성하기 위해 서브클래스를 만들어야 하는가?
- 클래스 기반 뷰로 구현하기 위해 장고 소스 코드까지 들여다볼 정도로 난해한가?
- 클래스 기반 뷰로 처리할 경우 극단적으로 복잡해 지겠는가? (뷰가 한개 이상의 폼을 처리해야하는가?)

## 8.2 URLConf로 부터 뷰 로직을 분리하기
- 뷰 모듈은 뷰 로직을 포함해야한다
- URL 모듈은 URL 로직을 포함해야 한다.
- 안좋은 예제를 보자
``` python
from django.conf.urls import url
from django.views.generic import DetailView

from tasting.models import Tasting

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Tasting, template_name='tastings/detail.html'), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', DetailView.as_view(model=Tasting, template_name='tastings/results.html', name='results')))
]
```

- 뷰와 url 모델 사이에 상호 느슨한 결합(loose coupling) 대신 단단하게 종속적인 결합(tight coupling)이 되어 있다. (뷰 재사용이 어려움)
- 클래스 기반 뷰들 사이에서 같거나 비슷한 인자들이 계속 이용되면 반복되는 작업을 하지 말라는 철학에 위배
- url 확장성이 파괴됨

## 8.3 URLConf에서 느슨한 결합 유지하기
``` python
# views.py
from django.views.generic import ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse

from .models import Tasting

class TasteListView(ListView):
    model = Tasting

class TasteDetailView(DetailView):
    model = Tasting

class TasteResultsView(TasteDetailView):
    template_name = 'tastings/results.html'

class TasteUpdateView(UpdateView):
    model = Tasting

    def get_success_url(self):
        return reverse('tastings:detail', kwargs={'pk': self.object.pk})
```
``` python
# urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.TasteListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.TasteDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<pk>\d+)/results/$',
        view=views.TasteResultsView.as_view(),
        name='results'
    ),
    url(
        regex=r'^(?P<pk>\d+)/update/$',
        view=views.TasteUpdate.as_view(),
        name='update'
    )
]
```
### 위 방법이 더 좋은 이유
- 반복되는 작업 하지 않기: 뷰들 사이에서 인자나 속성이 중복 사용되지 않는다.
- 느슨한 결합: URLConf에 모델과 템플릿 이름을 전부 제거
- URLConf는 한번에 한가지 업무 처리
- 클래스 기반이라는 장점을 살리게 됨
- 무한한 유연성: 뷰 모델에서 표준화된 정의를 구현

### 클래스 기반의 뷰를 사용하지 않는다면
- __file__ 속성을 이용하여 디렉터리 워킹과 정규표현식을 혼합하여 자동으로 URLConf를 생성하는 정교한 트릭을 이용한 URLConf 확장

## 8.4 URL 이름공간 이용하기
``` python
# urls.py
urlpatterns += [
    url(r'^tastings/', include('tastings.urls', namespace='tastings')),
]
```
``` python
# views.py
class TasteUpdateView(UpdateView):
    model = Tasting

    def get_success_url(self):
        return reverse('tastings:detail',
            kwargs={'pk':self.object.pk})
```
``` html
# html template
{% extends 'base.html' %}

{% block title %}Tastings{% endblock title %}

{% block content %}
<ul>
    {% for tate in tastings %}
        <li>
            <a href="{% url 'tastings:detail' taste.pk %}">{{ taste.title }}</a>
            <small>
                (<a href="{% url 'tastings:update' taste.pk %}">update</a>)
            </small>
        </li>
    {% endfor %}
</ul>
{% endblock content %}
```

### URL 이름을 짧고, 명확하고, 반복되는 작업을 피해서 작성하는 방법
- tasting_detail, tastings_results 보단 detail, results

### 서드 파티 라이브러리와 상호 운영성을 높이기
- namespace를 활용하여 적용

### 검색, 업그레이드, 리팩터링을 쉽게

### 더 많은 앱과 템플릿 리버스 트릭을 허용

## 8.5 URLConf에서 뷰를 문자열로 지목하지 말자
- 나쁜 예
``` python
# urls.py
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # 뷰를 문자열로 정의
    url(r'^$', 'polls.view.index', name='index')
)
```
- 좋은 예
``` python
# urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    # 뷰를 명시적으로 정의
    url(r'^$', views.index, name='index'),
]
```

## locals()를 뷰 콘텍스트에 이용하지 말자
- 나쁜 패턴
``` python
def ice_cream_store_display(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    date = timezone.now()
    return render(request, 'melted_ice_cream_report.html', locals())
```
- 명시적으로 사용하자
``` python
def ice_cream_store_display(request, store_id):
    return render(request, 'melted_ice_cream_report.html', dict{
        'store': get_object_or_404(Store, id=store_id),
        'now': timezone.now()
    })
```