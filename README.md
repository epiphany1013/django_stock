# 주식 정보 표시 웹 애플리케이션

📌 개요

이 프로젝트는 Django를 사용하여 개발된 주식 정보 표시 웹 애플리케이션입니다. 
사용자는 특정 회사의 주식을 입력하여 실시간 주식 데이터를 조회할 수 있습니다.


📌 기능
- 사용자가 회사 입력시, 해당 회사의 52주간 최고 가격, 최저 가격, 최신 가격을 알려줍니다.


📌 작동 환경 (개발 환경)

- python 3.8.9
- django 4.2




📌 설치 및 실행방법

- 프로젝트를 클론
```
git clone https://github.com/epiphany1013/django_stock.git
```

- 필요한 패키지를 설치

```python
pip install -r requirements.txt
```

- api_key.py 파일에 발급받은 token을 입력 (https://iexcloud.io/)
```python
key = "YOUR_TOKEN"
```

- Django 서버를 시작

```python
python manage.py runserver
```
