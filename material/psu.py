import psutil as ps
from prettytable import PrettyTable

table = PrettyTable(['PNAME', 'STATUS'])
for process in ps.pids():
    try:
        p = ps.Process(process)
        if str(p.status()) == str(ps.STATUS_RUNNING):
            table.add_row([
                p.name(),
                p.status()
            ])
    except:
        print("error")

print(table)
