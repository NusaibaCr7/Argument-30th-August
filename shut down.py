import os
shutdown = input("Do you wish to shut down your computer?(yes/no): ")
if shutdown == 'no':
    exit()
else:
    os.system("shutdown /s /t 1")   