# %%
import json
from collections import Counter, defaultdict

import numpy
import pandas as pd
from pandas import DataFrame, Series

path = r'C:\Users\oyff\Desktop\pydata\pydata-book\datasets\bitly_usagov\example.txt'
records = [json.loads(line) for line in open(path)]
# records[0]['tz']
timeZones = [rec['tz'] for rec in records if 'tz' in rec]
# timeZones[:10]

# standard py count tz
# def get_count(seq):
#     counts = defaultdict(int)
#     for x in seq:
#         counts[x] += 1
#     return counts

# counts11 = get_count(timeZones)
# counts['America/New_York']
# len(timeZones)
# counts2 = Counter(timeZones)
# counts2.most_common(10)


# use pandas to count tz
frame = DataFrame(records)
frame['tz'][:10]
tzCounts = frame['tz'].value_counts()
tzCounts[:10]

clear_tz = frame['tz'].fillna('Missing')
clear_tz[clear_tz == ''] = 'Unknown'
tzCounts = clear_tz.value_counts()
tzCounts[:10]
tzCounts[:10].plot(kind='barh')

results = Series([x.split()[0] for x in frame.a.dropna()])
results[:5]
results.value_counts()[:10].plot(kind='barh')

# cframe = frame[frame.a.notnull()]
# operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
# operating_system[:5]
# by_tz_os = cframe.groupby(['tz', operating_system])


# %%
