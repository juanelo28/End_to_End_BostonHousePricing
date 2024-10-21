FROM python:3.11

# Copy the current directory contents into /app in the container
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install the necessary dependencies
RUN pip install -r requirements.txt

# Make port available to the world outside this container
EXPOSE $PORT

# Define environment variable for gunicorn
#ENV PORT=8000

# Run the application using gunicorn
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
