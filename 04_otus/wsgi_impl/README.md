# Homework 04: Simple WSGI web framework

Allow you to make small WSGI apps in a simple manner.


# How to Install

Install python's uwsgi server:
```
pip install uwsgi
```

# Running

```
cd wsgi_impl
uwsgi --http :9090 --wsgi-file app.py
```

Connect via browser to http://127.0.0.1/some_urls