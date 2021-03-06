#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

if __name__ == "__main__":
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "signbank.settings.testing")

    from django.core.management import call_command
    from django.conf import settings

    applen = len('signbank.apps.')

    apps_for_testing = [app[applen:] for app in settings.INSTALLED_APPS
                        if app.startswith("signbank.apps")]

    call_command("test", *apps_for_testing)
