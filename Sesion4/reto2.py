import datetime
from datetime import timedelta

today = datetime.datetime.now()

print(today)

print('Dentro de 300 días será: ',(today+timedelta(days=300)).strftime('%A %d %B %Y'))