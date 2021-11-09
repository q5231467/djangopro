django-admin startproject mypro
python manage.py runserver 0.0.0.0:8000

pip install django
pip install pymysql

python manger.py makemigrations
相当于 在该app下建立 migrations目录，并记录下你所有的关于modes.py的改动，比如0001_initial.py， 但是这个改动还没有作用到数据库文件

python manage.py migrate
 将该models.py改动 作用到数据库文件，说明 /blog/article数据库文件已经被改变了，生成表格或者操作了数据

 python manage.py sqlmigrate app_name 0001
 这个命令用于查看 生成的 sql语句， 这个命令相当于之前 django 版本中的 sqlall
cmd 中显示