from datetime import datetime
from archiveFont import archiveFont

time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
archiveFont(CurrentFont(), time)