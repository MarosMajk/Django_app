# Django_app task

### Proces inštálácie

Na začiatok je potrebné si stiahnúť .zip súbor celej aplikácie (clone or download)

Po extrahovaní súboru do priečinku je potrebné si vytvoriť virtual enviroment. A následne nainštalovať všetky potrebné balíčky pip.

```sh
$ python3 -m venv enviroment
$ . enviroment/bin/activate
$ pip install -r requirements.txt
```

Aplikáciu spustíme pomocou python manage.py runserver

```sh
$ cd mysite
$ python manage.py runserver
```

### Balíčky

Pip packpages použité v aplikácií.

| packpage | version |
| ------ | ------ |
| asgiref | 3.2.7|
| Django | 3.0.7|
| pytz| 2020.1 |
| sqlparse |0.3.1|
