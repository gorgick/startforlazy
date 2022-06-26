Project

1. That's site resume, I show here my skills in back and front: python, Django, docker, docker-compose, html, css

2. I wrote it on Windows 7, so I use to python 3.8, and choose libraries for my OS

3. If you are using Windows 7 - in docker, for Alpine Linux:
RUN apk --update add
RUN apk --update add gcc build-base freetype-dev libpng-dev openblas-dev
maybe thats won't be enough

Also you should know your own IP:
>docker-machine ip default

When you build and run docker-compose:
>docker-compose exec web python manage.py migrate --noinput
>docker-compose exec web python manage.py createsuperuser

About site:

1. Create a model of Couses, Authentication, Authorization, order of courses, sending mails with registration,
personal area, send like or dislike to course(only one time for each person), send a comment,
show a percent of "+" reviews and comments under courses

2. Simple API

Сайт

1. Это сайт резюме, показывающий определенные знания в бэкенде: джанго, синтаксис, docker - docker-compose;
и понимание фронтенда: html, css, использование bootstrap, crispy-forms

2. Написан на ос - Windows 7, версии языка, docker и др - связаны с ос

3. Для подключения на Windows 7, в докер, если используете контейнеризацию alpine дистрибутивом -
RUN apk --update add
RUN apk --update add gcc build-base freetype-dev libpng-dev openblas-dev
возможно это не полный список

Так же - вам надо будет знать свой IP адрес для корректной работы:
>docker-machine ip default

О сайте

1. Создание моделей курсов, Авторизация, Аутонтификация, заказ курсов, пересылка почты при регистрации,
личный кабинет, лайк и дизлайк курсу(один раз, каждому курсу, определенному человеку), вывод % положительных отзывов курса,
оставление комментариев под курсом
2. Простое api

