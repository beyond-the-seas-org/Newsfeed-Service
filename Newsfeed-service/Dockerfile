# Use an official Python runtime as a parent image
FROM python:3.11.4-alpine

# Set the working directory within the container named "app"
WORKDIR /app

# Copy the requirements file into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

# Define the command to run your application within the container
CMD ["flask", "run"] 