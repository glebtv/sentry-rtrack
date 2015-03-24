Sentry Gitlab
=============

A plugin for Sentry which allow you to create issues in your rtrack repositories from Sentry errors.

This module used the [sentry-github](https://github.com/getsentry/sentry-github) module as a basis for it structure.
This module used the [sentry-gitlab](https://github.com/ajcrowe/sentry-gitlab) module for some ideas

Please note that rtrack is not currently publically available, so this module is probably useless for you.

Install
-------

Clone to repository to your sentry install. 

    git clone https://github.com/glebtv/sentry-rtrack.git

Then run the setup script to install the plugin and it's dependencies.

    python setup.py install

Alternatively you can use `pip`

    pip install -e "git+https://github.com/glebtv/sentry-rtrack.git@v0.1.0#egg=sentry-rtrack"

Restart Sentry and you should see a new plugin under `manage integrations` for your projects.

Configure
---------

Once enabled you can configure your settings on each project.

Bugs & Issues
-------------

If you find something that doesn't work please create an issue or even better fix it and submit a pull request!

Dependencies
------------

* [requests](http://www.python-requests.org)

