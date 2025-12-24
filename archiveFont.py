import os
from mojo.UI import Message

def archiveFont(font, time):
    
    if not font:
        Message('No font found', informativeText = 'Please open a font for this action.')
    
    else:
        path = font.path

        if path:
            url = os.path.dirname(path)
    
            if '_Archive' not in url:
                archive = f'{url}/_Archive'
    
                if not os.path.exists(archive):
                	os.makedirs(archive)
    
                name = path.replace(url + '/', '')
    
                newFont = font.copy()
                newFont.save(path = f'{archive}/{time}-{name}', formatVersion = 3)