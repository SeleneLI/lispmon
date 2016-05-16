__author__ = 'yueli'

from config.config import *

target_url = 'http://lispmon.net/mappings/EID4_mappings_20120920.txt'
response = urllib2.urlopen(target_url)
html = response.read()
# print html

# Open a file to store the eid number
try:
    os.stat(LISPMON_TRACES)
except:
    os.makedirs(LISPMON_TRACES)

print os.path.join(LISPMON_TRACES, 'eid_number.csv')

with open(os.path.join(LISPMON_TRACES, 'eid_number_sinal.csv'), 'wb') as eid_num_file:
    spamwriter = csv.writer(eid_num_file, dialect='excel', delimiter=';')
    spamwriter.writerow(['Date', 'EID number', 'EID prefix'])

    eid_counter = 0
    eid_num_list = []
    eid_prefix_list = []
    for line in html.split('\n'):
        if line.startswith('#') or line.startswith('&') or line.startswith('>') or line == '':
            continue
        elif len(line.split(',')) > 1:
            if line.split(',')[1] == '1':
                # eid_counter += 1
                eid_prefix_list.append(line.split(',')[0])

    eid_num_list.append(eid_counter)

    print list(set(eid_prefix_list))
    eid_counter = len(list(set(eid_prefix_list)))
    print eid_counter

    row = ['2012-09-20', eid_counter]
    row.extend(list(set(eid_prefix_list)))
    spamwriter.writerow(row)

    print eid_counter