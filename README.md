## 一、项目运行环境
64bit linux或window
<br>python 3.6
<br>mysql 5.6
<br>django 2.0

## 二、python2、python3共存：
<br>0、安装编译依赖包：yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel gcc zlib zlib-devel libffi-devel
<br>1、下载编译安装包：wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tar.xz
<br>2、#解压： tar -xvJf  Python-3.7.1.tar.xz
<br>3、切换进入：cd Python-3.7.1
<br>4、编译安装： ./configure prefix=/usr/local/python3  ， sudo make, sudo make install
<br>5、创建python3软连接: ln -s /usr/local/python3/bin/python3.7 /usr/bin/python3
<br>6、pip3: ln -s /usr/local/bin/python3/bin/pip3  /usr/bin/pip3
<br>7、升级pip3:python3 -m pip install --upgrade pip或者pip3 install --upgrade pip
<br>8、解决pip install慢的问题： vi ~/.pip/pip.conf，添加以下内容
```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

## 三、安装虚拟模块
<br>1、[root@localhost ~]# pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple virtualenv,创建virtualenv软连接：ln -s /usr/local/python3/bin/virtualenv /usr/bin/virtualenv(如果pip3 安装报ssl错误，则删除之前解压的python，重新编译)
<br>2、安装virtualenvwrapper:
    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple virtualenvwrapper
<br>3、我们可以在/etc/profile中设置开机自启动，这样的话会影响系统所有用户，也可以在用户家目录下~/.bash_profile针对某个用户进行设置。
这里我们针对root用户进行设置。[root@localhost ~]# vim ~/.bash_profile
<br>4、添加配置：

```
export WORKON_HOME=~/Envs  #设置virtaulenv的统一管理目录
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages' ##添加virtualenvwrapper的参数，生成干净隔绝的
环境
export VIRTUALENVWRAPPER_PYTHON=/usr/local/python3/bin/python3.7 #指定python解释器
source /usr/local/python3/bin/virtualenvwrapper.sh #执行virtualenvwrapper安装脚本
```

读取文件，使得生效，此时已经可以使用virtalenvwrapper
<br>5、使文件立即生效：[root@localhost ~]# source  ~/.bash_profile


## 安装xadmin2.0
1、下载zip包，https://github.com/sshwsfc/xadmin/tree/django2
2、安装 pip install xadmin-django2
3、或者pip install git+git://github.com/sshwsfc/xadmin.git@django2

## 项目运行步骤：

<br>   4、git clone https://github.com/xyq946692052/globalinvestor
<br>  5、mkvirtualenv -p python安装路径/python.exe global-investor
<br>  6、workon global-investor, pip install -r requirements.txt
<br>7、python manager.py --settings=globalinvestor.conf.test