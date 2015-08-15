#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/Ginseng-Test/GinsengFlask/")

from GinsengFlask import app as application
application.secret_key = '12341234'
