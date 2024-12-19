# pull python base image
FROM python:3.10-slim

# add requirements file & trained model
ADD requirements.txt .

# update pip
RUN pip install --upgrade pip

# install dependencies
RUN pip install -r requirements.txt

# add application file
ADD app/* app/.
ADD app/model/* app/model/.

# expose port where your application will be running
EXPOSE 7860

# start application
CMD ["python", "app/main.py"]
