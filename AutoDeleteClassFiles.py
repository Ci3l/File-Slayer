from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import time
class MyHandler(FileSystemEventHandler) :
    def on_modified(self, event) :
        for filename in os.listdir(folder_to_track) :
            list_filename = filename.split('.')
            if list_filename[-1] == 'class':
                print('>>',folder_to_track + '/' + filename)
                file_to_delete = folder_to_track + "/" + filename
                os.remove(file_to_delete)
                print('> deleted')
folder_to_track = input('folder to track :')
folder_to_track.replace('\\',"/")
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
try :
    while True :
        time.sleep(10)
except KeyboardInterrupt :
    observer.stop()
observer.join()
