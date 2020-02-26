#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
#sys.path.append("/media/gonzalo/ARCHIVOS/Universidad/Codigo/SignBank/FinSL-signbank")
#sys.path.append("E:/Universidad/Codigo/Web/django_projects/Sign_Bank/FinSL-signbank")

if __name__ == "__main__":
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "signbank.settings.development")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
