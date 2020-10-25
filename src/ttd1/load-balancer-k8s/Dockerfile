FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# install netcat
RUN apt-get update && \
    apt-get -y install netcat && \
    apt-get clean

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

# ttd1
#EXPOSE 80

# ttd2
#EXPOSE 5000

# mata-loadbalancer
EXPOSE 80

CMD ["uvicorn", "api_lb:app", "--host", "0.0.0.0", "--port", "80"]
