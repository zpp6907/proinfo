FROM python:3.8

MAINTAINER Aaron

#设置环境变量
ENV PYTHONUNBUFFERED 1
COPY pip.conf /root/.pip/pip.conf

#在容器内/var/www/html/下创建 PetHomeServer 文件夹
RUN mkdir -p /var/www/html/con_dev

#设置容器内工作目录
WORKDIR /var/www/html/con_dev

#将当前目录文件加入到容器工作目录中(.表示当前宿主机目录)
ADD . /var/www/html/con_dev

#利用pip安装依赖
RUN pip install -r requirement.txt