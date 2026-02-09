FROM python:3.9-slim
WORKDIR /app
COPY requirments.txt .
RUN pip install -r requirments.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
