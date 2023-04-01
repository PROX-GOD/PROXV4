import os, platform

os.system('git pull')

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    import OK64

elif bit == '32bit':

    import OK
