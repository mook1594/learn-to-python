#### [GO TO BACK](../README.md)

# 11. 장고 폼의 기초

## 11.1 장고 폼을 이용하여 모든 입력 데이터에 대한 유효성 검사하기
- 폼을 이용하여 유효성 검사
``` python
import csv
import StringIO

from django import forms

from .models import Purchase, Seller

class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase

    def clean_seller(self):
        seller = self.cleaned_data['seller']
        try:
            Seller.objects.get(name=seller)
        except Seller.DoesNotExist:
            msg = '{0} does not exist in purchase #{1}.'.format(
                seller,
                self.cleaned_data['purchase_number']
            )
            raise forms.ValidationError(msg)
        return seller
    
    def add_csv_purchases(rows):
        rows = StringIO.StringIO(rows)

        records_added = 0
        errors = []
        # 한 줄당 하나의 dict를 생성. 단 첫 번째 줄은 키 값으로 함
        for row in csv.DictReader(rows, delimiter=','):

            # PurchaseForm에 원본 데이터 추가
            form = PurchaseForm(row)
            # 원본 데이터가 유효한지 검사
            if form.is_valid():
                # 원본 데이터가 유효하므로 해당 레코드 저장
                form.save()
                records_added += 1
            else:
                errors.append(form.errors)
            
        return records_added, errors
```
- ValidationError에 code 파라미터를 전달해줄 것을 추천

## 11.2 HTML 폼에서 POST 메서드 이용하기
``` html
<form action="{% url 'flavor_add' %}" method="POST">
```
- 폼에서 유일하게 POST를 사용하지 않는 경우는 검색 폼. GET을 이용

## 11.3 데이터를 변경하는 HTTP 폼은 언제나 CSRF 보안을 이용해야 한다
- 사이트 간 위조 요청 방지 CSRF(cross-site request forgery protection)
- [장고의 CSRF 문서](https://docs.djangoproject.com/ko/4.0/ref/csrf/)

### Ajax를 통해 데이터 추가하기
- ajax를 사용할 때는 반드시 CSRF 보안을 사용해야 한다.
- 헤더에 X-CSRFToken을 설정

## 11.4 장고의 폼 인스턴스 속성을 추가하는 방법 이해하기
``` python
from django import forms

from .models import Taster

class TasterForm(forms.ModelForm):

    class Meta:
        model = Taster

    def __init__(self, *args, **kwargs):
        # user 속성 폼에 추가하기
        self.user = kwargs.pop('user')
        super(TasterForm, self).__init__(*args, **kwargs)


```
``` python
from django.views.generic import UpdateView

from braces.views import LoginRequireMixin

from .forms import TasterForm
from .models import Taster

class TasterUpdateView(LoginRequiredMixin, UpdateView):
    model = Taster
    form_class = TasterForm
    success_url = '/someplace/'

    def get_form_kwargs(self):
        """ 키워드 인자들로 폼을 추가하는 메서드 """
        # 폼 #kargs를 가져오기
        kwargs = super(TasterUpdateView, self).get_form_kwargs()
        # kwargs의 user_id 업데이트
        kwargs['user'] = self.request.user
        return kwargs
```

## 11.5 폼이 유효성을 검사하는 방법 알아두기 
### form.is_valid() 동작
- form.is_valid()는 form.full_clean() 호출
- form.full_clean()은 각 필드 유효성 검사
    - to_python()을 이용하여 변환 ValidationError 일으킴
    - 커스텀 유효성 검사기 검사 ValidationError
    - 폼에 clean_<field>() 메서드가 있으면 이를 실행
- from.clean()을 실행
- ModelForm 인스턴스의 경우 form.post_clean()이 다음 작업 실행
    - form.is_valid()가 True, False 관계없이 ModelForm의 데이터를 모델 인스턴스로 설정
    - 모델의 clean() 메서드를 호출. ORM 통해 인스턴스를 저장할 때는 모델 clean() 메서드가 호출되지는 않는다.

### 모델폼 데이터는 폼에 먼저 저장된 이후 모델 인스턴스에 저장된다
``` python
# models.py
from django.db import models

class ModelFormFailureHistory(models.Model):
    form_data = models.TextField()
    models_data = models>TextField()
```
``` python
# views.py
import json

from django.contrib import messages
from django.core import serializers
from core.models import ModelFormFailureHistory

class FlavorActionMixin(object):

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(FlavorActionMixin, self).form_valid(form)

    def form_invalid(self, form):
        """실패 내역을 확인하기 위해 유효성 검사에 실패한 폼과 모델을 저장한다"""
        form_data = json.dumps(form.cleaned_data)
        models_data = serializers.serialize('json', [form.instance])[1:-1]
        ModelFormFailureHistory.objects.create(
            form_data=form_data,
            model_data=model_data
        )
        return super(FlavorActionMixin, self).form_invalid(form)
```

## 11.6 Form.add_error()를 이용하여 폼에 에러 추가하기
``` python
from django import froms

class IceCreamReviewForm(forms.Form):
    # tester 폼의 나머지 부분이 이곳에 위치
    ...
    def clean(self):
        cleaned_data = super(TasterForm, self).clean()
        flavor = cleaned_data.get('flavor')
        age = cleaned_data.get('age')

        if flavor == 'coffee' and age < 3:
            # 나중에 보여줄 에러들을 기록
            msg = u'Coffee Ice Cream is not for Babies.'
            self.add_error('flavor', msg)
            self.add_error('age', msg)

        # 항상 처리된 데이터 전체를 반환한다.
        return cleaned_data
```