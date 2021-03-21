import datetime
import argparse

def parse_ical_date(s):
    year = int(s[:4])
    month = int(s[4:6])
    day = int(s[6:8])
    hour = int(s[9:11])
    minute = int(s[11:13])
    second = int(s[13:15])

    # we're ignoring UTC designations, as they seem to be ignored by most calendars?
    return datetime.datetime(year, month, day, hour, minute, second)

def parse_input_date(s):
    s = s.split('-')
    year = int(s[0])
    month = int(s[1])
    day = int(s[2])
    try:
        return datetime.datetime(year, month, day)
    except:
        print("Not a valid date")
        exit()

def clip_ics(input_file, output_file, before_date: datetime.datetime):
    print("Reading ics file...", end="")
    with open(input_file) as f:
        lines = f.readlines()
    print(" done")

    print("Looking through events...")
    first_event = 0
    last_event = 0
    events_before = 0
    for i, l in enumerate(lines):
        if l.strip() == 'BEGIN:VEVENT':
            if not first_event:
                first_event = i
            last_event = i
            events_before += 1
        if l.startswith('DTSTART:'):
            event_start = parse_ical_date(l.split(':')[1])
            if event_start >= before_date:
                break
    print("Found %d events before %s to be clipped" % (events_before, input_date.date().isoformat()))
    
    print("Writing output file...", end="")
    with open(output_file, 'w') as f:
        f.writelines(lines[:first_event])
        f.writelines(lines[last_event:])
    print(" done")


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', dest='input', required=True,
                    help="the path to your input .ics file")
parser.add_argument('-o', '--output', dest='output', default="clipped.ics",
                    help="the path to your desired output file")
parser.add_argument('-d', '--date', dest='date',
                    help="the desired clipping date in the following format: yyyy-mm-dd. If none is provided, current date will be used")

args = vars(parser.parse_args())

input_date = args['date']
if input_date:
    input_date = parse_input_date(input_date)
else:
    input_date = datetime.datetime.now()
            
clip_ics(args['input'], args['output'], input_date)