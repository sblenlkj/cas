from tg_client import Our_tg_client
import logging
import sys

def get_logger(level:int=logging.WARNING):
    root = logging.getLogger()
    root.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    return root

log = get_logger()

cl = Our_tg_client()
cl.set()
cl.run()