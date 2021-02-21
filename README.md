# ICS Clipper
A small python script to remove events from .ics files before a certain date.

## Usage

The following will remove all events before today from an ics file:

```shell
$ git clone https://github.com/realChesta/ics-clipper.git
$ cd ics-clipper
$ python ics_clipper.py -i "yourpath/events.ics"
```

### Options
* `-i, --input [path]` *required* the input .ics file to be read.
* `-o, --output [path]` the path to the desired output .ics file. Default is `"clipped.ics"`.
* `-d, --date [yyyy-mm-dd]` the desired cutoff date in that exact format. If not specified, the current date will be used.