#Socialschools Site#

#Requirements Installation

Please install the requirements according to your environment from the
requirements directory. It is recommended to use virtualenv. You can create your
virtualenv (assuming that you have virtualenvwrapper installed) by the following
command.

```
mkvirtualenv socialschools_site -r requirements.txt
```

or to update requirements of existing virtualenv,
```bash
pip install -r requirements.txt
```

# Database management

Use the following steps to setup the database and use the database dump where available.

```
$ psql postgres
postgres=# create database socialschools_site;
postgres=# \q

$ psql socialschools_site < ~/socialschools_site.sql
```

#Settings management

You will not be able to run the development server or management commands if the
DJANGO_SETTINGS_MODULE environment variable is not set.
With your virtualenv activated, enter the following commands

```bash
add2virtualenv .
echo "export DJANGO_SETTINGS_MODULE=socialschools_site.settings.local" >> $VIRTUAL_ENV/bin/postactivate
echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate
```
Reload your virtualenv to activate the new settings