FROM python:3.6-slim
MAINTAINER lizhuliang<lizhuliang@quancheng-ec.com>

RUN mkdir -p /root/
WORKDIR /root/

COPY requirements.txt deploy.conf gunicorn.conf manage.py /root/
RUN pip install -r requirements.txt

# hack fory pymysql not support Inception
COPY connections.py /usr/local/lib/python3.6/site-packages/pymysql/connections.py

COPY core/ /root/core/
COPY libs/ /root/libs/
COPY settingConf/ /root/settingConf/

RUN mkdir -p /root/log/
RUN mkdir -p /root/exportData/

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
