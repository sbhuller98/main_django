FROM python:3.8.3


# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /opt/mysite
RUN mkdir -p /opt/mysite/pip_cache
RUN mkdir -p /opt/mysite/sukh_site_v1
COPY requirements.txt start-server.sh /opt/mysite/
COPY .pip_cache /opt/mysite/pip_cache/
COPY sukh_site_v1 /opt/mysite/sukh_site_v1/
WORKDIR /opt/mysite
RUN pip install -r requirements.txt --cache-dir /opt/mysite/pip_cache
RUN chown -R www-data:www-data /opt/mysite

# start server
EXPOSE 8080
STOPSIGNAL SIGTERM
CMD ["/opt/mysite/start-server.sh"]