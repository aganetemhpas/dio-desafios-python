# biblioteca de terceiros
# pip install pytz

import datetime
import pytz

# Criando datetime com timezone
d = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))


# Somente com python
d = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3), "BRT"))

# convertendo para outro timezone
d_utc = d.astimezone(datetime.timezone.utc)
print(d_utc)