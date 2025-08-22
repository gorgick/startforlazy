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
