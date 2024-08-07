# DICOM Project

A Django application that provides an API for uploading and storing DICOM files along with their associated metadata. This project utilizes Django REST Framework for building RESTful APIs and pydicom for extracting metadata from DICOM files.


## Features

- **Upload DICOM files** with associated metadata.
- **Extract metadata** such as Patient ID, Modality, Series Instance UID, and Study Instance UID from uploaded DICOM files.
- **Validate uploaded files** to ensure they are in the DICOM format.
- **Admin interface** for managing uploaded DICOM files.

## Technologies Used

- **Django**
- **Django REST Framework**
- **pydicom**
- **PostgreSQL**
- **Python 3.x**
- **Docker**
- **Docker Compose**

## Installation

### Using Docker

1. **Clone the repository:**

   ```bash
   git clone https://github.com/amiradmin/dicom_project.git
1. **Navigate to the project directory:**

  ```bash
    cd dicom_project
```
3. **Environment Variables**
```env

POSTGRES_DB=yourdbname
POSTGRES_USER=yourdbuser
POSTGRES_PASSWORD=yourdbpassword
DATABASE_URL=postgres://yourdbuser:yourdbpassword@db:5432/yourdbname
SECRET_KEY=your-secret-key
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@gmail.com
DJANGO_SUPERUSER_PASSWORD=your_superuser_password
DEBUG=1
Docker Deployment
The application includes an entrypoint script that handles database migrations and superuser creation automatically. To build and start the containers, run:
```




5. **Access the application:**
```
Open your browser and navigate to http://127.0.0.1:8000 to access the API.
Usage
Accessing the Admin Interface
Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials defined in your environment variables.
```
5. **API Endpoints**
```env Upload DICOM File
Endpoint: /api/dicom/upload/
Method: POST
Request:
file: The DICOM file to upload.
doctype: The type of document.
Response:
On success, returns the serialized data of the uploaded file.
On error, returns validation errors.
```
6. **Authentication**
- The API uses JWT (JSON Web Tokens) for authentication.
```env
POST /api/token/: Obtain JWT token.
POST /api/token/refresh/: Refresh JWT token.
Data Validation and Error Handling
Data Validation: Ensured through Django and DRF serializers (e.g., ensuring unique identifiers).
Error Handling: Standardized error responses with appropriate HTTP status codes.
Setup and Deployment
Prerequisites
Docker
Docker Compose
Environment Variables
Create a .env file in the root directory with the following content:
```
4. **Build and start the containers:**
- Run the following command to build the Docker images and start the application:
```bash
docker-compose up --build
```
- The entrypoint script will wait for the database to be ready, run migrations, and create a superuser if it doesn't already exist.