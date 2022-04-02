FROM python:3.7-slim
WORKDIR /docker_container
ADD . /docker_container
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
# CMD cd webapp/ ; python app.py
CMD ["python","app.py"]