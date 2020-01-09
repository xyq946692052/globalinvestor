import os
from celery import Celery
from django.conf import settings


# 获取当前文件夹名，即为该django项目名
project_name = os.path.split(os.path.abspath('.'))[-1]
project_settings = '{}.conf.test'.format(project_name)


# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', project_settings)

# 实例化celery
app = Celery(project_name)

# 使用django的settings文件配置celery
app.config_from_object('django.conf:settings')

# Celery加载所有注册的应用
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

