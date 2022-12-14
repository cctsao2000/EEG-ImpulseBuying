import glob,os
import csv

# change logfile(.txt) to csv
def log2csv(filename):
    data = []
    with open(filename, 'r') as f:
        logs = f.readlines()
        start = round(float(logs[0].split()[0]))
        for line in logs:
            eventlog = line.split()
            if len(eventlog)>2:
                data.append([round(float(eventlog[0]))-start, eventlog[1], round(float(eventlog[2]))-start, eventlog[3]+'2'])
            else:
                data.append([round(float(eventlog[0]))-start, eventlog[1]])

    with open(f'../log-csv/{filename[:-4]}.csv', 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(['timecode', 'first choice', 'timecode2', 'second choice'])
        for d in data:
            writer.writerow(d)

def main():
    os.chdir('../log-txt')
    for logfile in glob.glob('*.txt'):
        log2csv(logfile)

if __name__ == '__main__':
    main()