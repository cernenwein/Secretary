FROM python:3.11-slim

WORKDIR /app
COPY calendar_service.py /app/calendar_service.py

RUN pip install google-api-python-client google-auth google-auth-oauthlib flask

EXPOSE 8080
CMD ["python3", "calendar_service.py"]
