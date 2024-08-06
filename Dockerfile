# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Update pip to the latest version
RUN python -m pip install --upgrade pip

# Install dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /code/

# Copy the entrypoint script into the container
COPY entrypoint.sh /code/

# Make the entrypoint script executable
RUN chmod +x /code/entrypoint.sh

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Set the entrypoint for the container
ENTRYPOINT ["/code/entrypoint.sh"]

# Command to start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
