#!/usr/bin/env bash
#
# Runs Django tests (https://docs.djangoproject.com/en/1.11/topics/testing/)

# Environment variables may not be loaded under all conditions.
if [ -z "${TWLIGHT_HOME}" ]
then
    source /etc/environment
fi

{
    # print the date for logging purposes
    echo [$(date)]

    # Load virtual environment
    if source ${TWLIGHT_HOME}/bin/virtualenv_activate.sh
    then
        echo "test --noinput"
        DJANGO_SETTINGS_MODULE=TWLight.settings.local python manage.py test --noinput
    else
        exit 1
    fi
} 2>&1 | tee -a ${TWLIGHT_HOME}/TWLight/logs/test.log
