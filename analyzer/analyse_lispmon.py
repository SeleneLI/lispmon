__author__ = 'yueli'


from config.config import *

# Build the 'year', 'month' and 'day'
year_list = [str(year) for year in range(2010, 2017)]
month_list = []
for month in range(1, 13):
    month_list.append(str('%02d'%month))
day_list = []
for day in range(1, 32):
    day_list.append(str('%02d'%day))

eid_num_list = []

# Open a file to store the eid number
try:
    os.stat(LISPMON_TRACES)
except:
    os.makedirs(LISPMON_TRACES)

print os.path.join(LISPMON_TRACES, 'eid_number.csv')

with open(os.path.join(LISPMON_TRACES, 'eid_number.csv'), 'wb') as eid_num_file:
    spamwriter = csv.writer(eid_num_file, dialect='excel', delimiter=';')
    spamwriter.writerow(['Date', 'EID number', 'EID prefix'])

    for year in year_list:
        for month in month_list:
            for day in day_list:
                target_url = 'http://lispmon.net/mappings/EID4_mappings_{0}{1}{2}.txt'.format(year,month,day)
                print target_url
                eid_prefix_list = []

                try:
                    response = urllib2.urlopen(target_url)
                    html = response.read()
                    eid_counter= 0
                    for line in html.split('\n'):
                        # Remove the sentence beginning with '#', '&' and '>', as well as the empty line
                        if line.startswith('#') or line.startswith('&') or line.startswith('>') or line == '':
                            continue
                        # The returned legency/EID prefix
                        elif len(line.split(',')) > 1:
                            if line.split(',')[1] == '1':
                                # eid_counter += 1
                                eid_prefix_list.append(line.split(',')[0])

                    eid_counter = len(list(set(eid_prefix_list)))
                    eid_num_list.append(eid_counter)
                    print '{0}-{1}-{2}:'.format(year,month,day), eid_counter

                    row = ['{0}-{1}-{2}'.format(year,month,day), eid_counter]
                    row.extend(list(set(eid_prefix_list)))
                    spamwriter.writerow(row)

                except urllib2.HTTPError:
                    print 'HTTP Error 404: Not Found'

    print 'eid_num_list =', eid_num_list