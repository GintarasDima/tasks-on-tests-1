# С помощью встроенных методов библиотеки numpy найдите дату первого понедельника в 2015 году.

import numpy as np
data = np.datetime64('2015-01-01')
print("Первый понедельник в 2015году: ","\n",np.busday_offset('2015-01-01', 0, roll='forward', weekmask='Mon'))

