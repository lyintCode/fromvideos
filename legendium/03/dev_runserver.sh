#!/bin/bash

# Заменить project на название вашего проекта
DJANGO_SETTINGS_MODULE="project.settings.dev" ./.venv/bin/python manage.py runserver
