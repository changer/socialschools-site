#PROJECT_NAME#

#Requirements Installation

Please install the requirements according to your environment from the
requirements directory. It is recommended to use virtualenv. You can create your
virtualenv (assuming that you have virtualenvwrapper installed) by the following
command.

```
mkvirtualenv PROJECT_NAME -r requirements.txt
```

or to update requirements of existing virtualenv,
```
pip install -r requirements.txt
```

#Settings management

You will not be able to run the development server or management commands if the
DJANGO_SETTINGS_MODULE environment variable is not set.
With your virtualenv activated, enter the following commands

```
add2virtualenv .
echo "export DJANGO_SETTINGS_MODULE=PROJECT_NAME.settings.local" >> $VIRTUAL_ENV/bin/postactivate
echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate
```
Reload your virtualenv to activate the new settings