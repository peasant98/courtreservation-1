#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "courtreservation.settings")

    from django.core.management import execute_from_command_line
#what is wrong with satish laptop?
    execute_from_command_line(sys.argv)
