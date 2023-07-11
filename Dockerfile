FROM python:3
WORKDIR /app
ADD wsgi.py .

RUN python -m pip install --upgrade pip
RUN pip install flask
EXPOSE 5000

CMD ["python", "wsgi.py"]