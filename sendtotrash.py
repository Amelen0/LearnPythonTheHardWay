#! usr/bin/ env python3
#Script to send files to trash

import send2trash
baconfile = open('baconfile','a')
baconfile.write('Hello bacon')
baconfile.close()
send2trash.send2trash('baconfile')
