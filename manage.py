#!/usr/bin/env python
import os
import sys

from tracker.boot import fix_path
fix_path()

GAE_SANDBOX_ARG_PREFIX = '--gae_'

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tracker.settings")

    from djangae.core.management import execute_from_command_line

    # argv, sandbox_args = [], {}
    # for arg in sys.argv:
    #     if arg.startswith(GAE_SANDBOX_ARG_PREFIX):
    #         value = None
    #         if '=' in arg:
    #             key, value = arg.split('=')
    #         else:
    #             key = arg
    #         sandbox_args[key.replace(GAE_SANDBOX_ARG_PREFIX, '')] = value
    #     else:
    #         argv.append(arg)

    # execute_from_command_line(argv, **sandbox_args)
    execute_from_command_line(sys.argv)
