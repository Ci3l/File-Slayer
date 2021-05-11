from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import time
class MyHandler(FileSystemEventHandler) :
    def on_modified(self, event) :
        for filename in os.listdir(folder_to_track) :
            list_filename = filename.split('.')
            print('>>',folder_to_track + '/' + filename)
            if list_filename[-1] == 'class':
                file_to_delete = folder_to_track + "/" + filename
                file_to_delete.remove(src)
                print('> deleted')
folder_to_track = "/Users/Utilisateur/Downloads" #for example
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
