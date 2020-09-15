from django.shortcuts import render
from django.conf import settings
import threading
import time

def main_job():
    while True:
        time.sleep(10)
        print("\n\nChecando...\n\n")

# task = threading.Thread(target=main_job)
# task.setDaemon(True)
#task.start()
