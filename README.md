# FILE SLAYER

### Description
Here's a little python program that deletes the annoying CLASS files when you're coding in JAVA, or any other type of file. It's deleting the files which are in the folder you specify and those in the folders of your folder.  

### Use project

The project only uses the time and os packages.
```
import os
import time
from os import listdir
from os.path import isfile, join
```
To Launch the project just go to the folder where 'FileSlayer.py' is stored and execute the command line below (in a command prompt window)
```
python FileSlayer.py
```
Now you just got to enter the folder address as specified below and, separated by coma, the type of file that you want to delete (by default it's CLASS)
```
\Users\Utilisateur\Downloads,pdf
```
Don't mind about the 'Utilisateur' it's because I'm French.

If you need it here's the syntax of the main function :
```
FileSlayer(folder to track, file type)
```
or
```
FileSlayer(folder to track)
```

If you have any problem or questions you can contact me by [mail](poire.erwan2005@gmail.com).
