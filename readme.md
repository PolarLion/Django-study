WSGIScriptAlias /polarlion  /path/to/Django-study/mysite/mysite/wsgi.py
WSGIPythonPath /path/to/Django-study/mysite/
Alias /static/ /path/to/Django-study/mysite/static/
<Directory /path/to/Django-study/mysite/static>
#Order deny,allow                                                                                                                                                                      
Options Indexes FollowSymLinks
AllowOverride All 
Require all granted
Allow from all
</Directory>
<Directory /path/to/Django-study/mysite/mysite>
<Files wsgi.py>
Require all granted
</Files>
</Directory>
