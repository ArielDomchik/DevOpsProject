FROM python:alpine

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY app.py check.py templates/ /
EXPOSE 5000

CMD ["python3", "app.py"]

