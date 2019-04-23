from datetime import datetime
import sys


def log(str_log=""):
    print "| %s | %s |" % (datetime.now(), str_log)
    sys.stdout.flush()
