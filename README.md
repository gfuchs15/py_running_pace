# py_running_pace
Small script giving pace-per-km a speed in km-per-hour from a time and a distance in km.
It also ouputs expected times for usual running distances assuming average computed pace.

## Usage

```
Running-pace: computes pace andnd speed given time [and distance], also as times for Marathon, Half-Marathon, 10K, 5K distances.

options:
  -h, --help            show this help message and exit
  -t TIME, --time TIME  time hh:mm:ss or mm:ss or ss
  -d DISTANCE, --distance DISTANCE
```

### Examples
giving time for 1 km:
```bash
python .\running-time.py -t 00:04:17
```

or specifying a distance:
```bash
python .\running-time.py -t 00:42:24 -d 10.0 
```
