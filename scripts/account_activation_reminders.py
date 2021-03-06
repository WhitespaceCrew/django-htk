import time

import script_config
from script_config import job_runner
from script_config import slog

from django.conf import settings

from htk.apps.accounts.emails import AccountActivationReminderEmails
from htk.constants.time import *

DAEMON_MODE = True
#DAEMON_MODE = False

def main():
    def workhorse():
        AccountActivationReminderEmails().send_emails()

    while True:
        job_runner(workhorse)

        if settings.TEST:
            # just make sure that it runs
            break

        if not DAEMON_MODE:
            # just run once, don't keep looping
            break

        slog('Done sending reminder emails, sleeping...')
        time.sleep(TIMEOUT_1_HOUR)

if __name__ == '__main__':
    job_runner(main)
