from datetime import datetime
from archiveFont import archiveFont

time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
print('Manually archiving font', os.path.basename(CurrentFont().path), '...')
archiveFont(CurrentFont(), time)