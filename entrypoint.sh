#!/bin/sh

# Wait for the database to be ready
echo "Waiting for the database to be ready..."
while ! nc -z db 5432; do
  sleep 0.1
done

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Create superuser if not already created
if [ -z "$(python manage.py shell -c 'from django.contrib.auth import get_user_model; print(get_user_model().objects.filter(username=\"${DJANGO_SUPERUSER_USERNAME}\").exists())')" ]; then
  echo "Creating superuser..."
  python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
  echo "Superuser created."
else
  echo "Superuser already exists."
fi

# Start the server
exec "$@"
