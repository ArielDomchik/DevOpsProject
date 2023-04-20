FROM python:alpine

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt 
RUN mkdir -p /logs && mkdir -p /templates
COPY app.py requirements.txt /
COPY index.html /templates
EXPOSE 5000

CMD ["python3", "app.py"]

