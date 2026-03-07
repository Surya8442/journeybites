FROM python:3.9-slim

# set working directory
WORKDIR /app

# copy requirements
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy project files
COPY . .

# expose port
EXPOSE 5000

# run application
CMD ["python","app.py"]
