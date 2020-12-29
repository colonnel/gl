FROM python:3.8.7-slim
RUN pip install psutil
WORKDIR /usr/src/app
COPY . .
CMD ["cpu_mem_info.py"]
ENTRYPOINT ["python3"]