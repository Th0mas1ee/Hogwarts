import logging

root_log = logging.getLogger(__name__)
for h in root_log.handlers[:]:
    root_log.removeHandler(h)
    h.close()

logging.basicConfig(level=logging.INFO,
                    format='%(asctime).19s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='report.log',
                    filemode='a')