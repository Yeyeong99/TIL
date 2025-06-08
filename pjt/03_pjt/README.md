# 관통 프로젝트: 금융
## 역할 
- 손준호
    - 네비게이션 바 구현
    - 회원가입 구현
    - 로그인 & 로그아웃 구현
    - 관심 종목 저장을 위한 모델 구현
- 이예영
    - 프로필 페이지: 관심 종목 관리 기능 구현
    - 관심 종목 클릭 시 크롤링 진행
    - 디자인 개선

## 페이지 구현
## 관심 종목 관리 기능 구현
```python
# accounts/urls.py    
    path('profile/find_company/<str:company_name>/', views.find_company, name='find_company'),
```
- 위와 같이 path 추가
- 프로필 상에서 상세 종목을 선택했을 때 -> stock_finder(메인페이지)에 company_name이 채워진 상태로 넘겨주기 위한 경로
```python
# accounts/views.py
def find_company(request, company_name):
    context = {
        'company_name': company_name,
    }
    return render(request, 'contentfetch/stock_finder.html', context)
```
- 위와 같이 context를 통해 company_name을 넘겨
```html
<!--contentfetch/templates/contentfetch/stock_finder.html-->
<input
        id="company"
        class="form-control mx-2"
        type="text"
        name="company_name"
        value="{{ company_name|default:'' }}"
        {%
        if
        is_loading
        %}readonly{%
        endif
        %}
      />
```
- 위와 같이 company_name으로 출력

### 프로필 페이지: 관심 종목 클릭 시 크롤링 진행
```python
# contentfetch/views.py
def stock_finder(request):
    driver = None  # WebDriver 초기화
    company_name = ''
    loading_step = ''

    if request.method == "POST":
        company_name = request.POST.get('company_name', '').strip().lower()
        loading_step = request.POST.get('loading_step', '')

    elif request.method == "GET":
        company_name = request.GET.get('company_name', '').strip().lower()

    if company_name:
        try:
            # 1. DB에서 `company_name`으로 부분 검색
            existing_data = StockData.objects.filter(
                company_name__icontains=company_name
            ).first()
```
- 스켈레톤 코드 상에서 `if not name`이라고 되어있던 부분을 위와 같이 수정
    - post일 때와 get일 때 company_name을 가져오는 방식이 구분되기 때문에
    - if - elif로 나누고 가져와진 기업 이름이 있을 때 try - except 구문을 실행하도록 수정

## 마무리
- 실시간으로 공유하며 하지 않고 직렬적으로 업무를 나눠 진행해 레거시 코드를 보수하는 느낌이 있었다.
    - 실제 협업을 할 경우, 꼭 필요한 경험이라는 생각이다.
    - 다른 사람이 작성한 코드를 이해하고, 그 방식에 맞춰 코드를 작성하는 것에 익숙해져야 한다는 생각이 들었다.
- UX/UI를 개선하는 데 있어서 부트스트랩 이용에 더 익숙해질 필요가 있다는 생각이 들었다.
    - 이전에 써봤거나 출력해봤던 화면도 구현 방식을 다시 봤을 때 생소했기 때문에 UI 개선을 위해선 css 사용에 더 익숙해져야 한다는 생각이다.