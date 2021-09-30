FROM python:3.8.8

RUN echo "hello"

WORKDIR /home/

RUN git clone https://github.com/lee-JunR/Fems_api

WORKDIR /home/Fems_api/

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 5050

CMD ["python", "manage.py", "runserver", "0.0.0.0:5050"]
