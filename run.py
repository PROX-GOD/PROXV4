import os, platform

os.system('git pull')

 

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from OK64 import approval

    approval()

elif bit == '32bit':

    from OK import approval

    approval()
