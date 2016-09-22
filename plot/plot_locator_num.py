__author__ = 'yueli'

from config.config import *
import datetime

# To get current date
now = datetime.datetime.now()

# Open a file to store the eid number
try:
    os.stat(os.path.join(LISPMON_FIGURES_AND_TABLES, "{0}_{1}_{2}".format(now.year, now.month, now.day)))
except:
    os.makedirs(os.path.join(LISPMON_FIGURES_AND_TABLES, "{0}_{1}_{2}".format(now.year, now.month, now.day)))

# Read the eid_num_list from locator_number.csv
rloc_num_list = []
with open(os.path.join(LISPMON_TRACES, "{0}_{1}_{2}".format(now.year, now.month, now.day), 'locator_number.csv')) as f_handler:
    next(f_handler)
    for line in f_handler:
        lines = line.split(";")
        rloc_num_list.append(lines[1])

x = range(0, len(rloc_num_list))
print "Length of X-axis:", len(x)
print "Length of Y-axis:", len(rloc_num_list)


mpl.rcParams['text.usetex'] = True
mpl.rcParams.update({'figure.autolayout': True})
plt.plot(x, rloc_num_list)
plt.xlabel(r"\textrm{2012/01/07--2016/09/21}", font)
plt.ylabel(r"\textrm{RLOC number}", font)
plt.xlim(min(x),max(x))
plt.xticks(fontsize=30, fontname="Times New Roman")
plt.yticks(fontsize=30, fontname="Times New Roman")

plt.savefig(os.path.join(LISPMON_FIGURES_AND_TABLES, "{0}_{1}_{2}".format(now.year, now.month, now.day), 'rloc_number.eps'), dpi=300, transparent=True)
plt.show()