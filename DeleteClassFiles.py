import os
from os import listdir
from os.path import isfile, join
#folder_to_track = input('folder to track :')
folder_to_track = r'\Users\Utilisateur\Documents'
folder_to_track.replace('\\',"/")

files = [f for f in listdir(folder_to_track) if isfile(join(folder_to_track, f))]
directories = [ name for name in os.listdir(folder_to_track) if os.path.isdir(os.path.join(folder_to_track, name)) ]
if '.tmp.drivedownload' in directories :
    directories.remove('.tmp.drivedownload')
if 'Mes vidéos' in directories :
    directories.remove('Mes vidéos')
if 'Ma musique' in directories :
    directories.remove('Ma musique')
if 'Mes images' in directories :
    directories.remove('Mes images')
i = len(directories) - 1
while i >= 0  :
    directories[i] = folder_to_track + '/' + directories[i]
    i = i - 1
for filename in files :
    list_filename = filename.split('.')
    if list_filename[-1] == 'class':
        print('>>',folder_to_track + '/' + filename)
        file_to_delete = folder_to_track + "/" + filename
        os.remove(file_to_delete)
        print('> deleted')
directoriesToCheck = []
i = 0
while len(directories) > 0 :
    files = [f for f in listdir(directories[i]) if isfile(join(directories[i], f))]
    directoriesInDirectories = [ name for name in os.listdir(directories[i]) if os.path.isdir(os.path.join(directories[i], name)) ]
    if len(directoriesInDirectories) > 0 :
        j = 0
        while j < len(directoriesInDirectories)  :
            directoriesToCheck.append(directories[i] + '/' + directoriesInDirectories[j])
            j = j + 1
    for filename in files :
        list_filename = filename.split('.')
        if list_filename[-1] == 'class':
            print('>>',directories[i] + '/' + filename)
            file_to_delete = directories[i] + "/" + filename
            os.remove(file_to_delete)
            print('> deleted')
    del directories[i]
    if len(directories) == 0 :
        directories = directoriesToCheck
        directoriesToCheck = []
