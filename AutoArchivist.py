# set as startup script to automatically archive font files to an '_Archive folder'

import os
from datetime import datetime
from mojo.subscriber import Subscriber
from archiveFont import archiveFont

class AutoArchivist(Subscriber):
    
    def autoArchive(self, font):
        # print(font)
        url = os.path.dirname(font.path)

        if '_Archive' not in url:
            archive = f'{url}/_Archive'    

            if not any(datetime.now().strftime('%Y-%m-%d') in file for file in os.listdir(archive)):
                print('AutoArchivist is saving font', os.path.basename(font.path), '...')
                time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                archiveFont(font, time)
            else:
                # print('File does exist.')
                pass
    
    def fontDocumentDidOpen(self, info):
        self.autoArchive(info['font'])
        
AutoArchivist()