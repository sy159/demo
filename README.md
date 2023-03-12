# xxx demo
## 功能简介
- demo 啦啦啦 因为本地是mysql所以直接用的mysql来实现，就没用PostgreSQL

------------
## 环境安装
- #### Python3.9
- #### 安装mysql5.7
------------
## 项目配置
- #### 克隆源码
git clone https://github.com/sy159/demo
- #### 安装依赖
python3 -m pip install -r requirements.txt
- #### 修改dbconfig配置
根据实际情况配置数据库地址及用户名密码等，如果不需要redis作为缓存就注释掉redis配置，使用默认的文件缓存
- #### 修改config文件
根据自己的配置修改config文件
- #### settings配置
根据需求配置settings.py文件


------------
## 命令启动
- #### 创建数据库
python3 manage.py makemigrations

python3 manage.py migrate

如果某个app下的model没有生成，就是用**python3 manage.py makemigrations --empty appname 单独生成**
- #### docker启动
docker build -t xxx:v1 
docker run -d -it --name demo -p 80:8000 xxx:v1  

- #### 创建后台登录的超级用户
python3 manage.py createsuperuser
- #### 项目启动
python3 manage.py runserver 0.0.0.0:8000


------------
## 接口文档地址
http://127.0.0.1:8000/swagger/
