将下列内容保存到 wsgi.conf 文件，并将文件放在 apache 配置文件目录下 （/path/to/httpd/conf.d）

"
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
</Directory>"
