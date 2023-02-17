# py_running_pace
Small script that computes pace per km from a time and distance in km.\\
It also gives expected times for common running distances, assuming the average computed pace.

## Usage

```
Running-pace: computes pace and speed given time [and distance]. It also provides times for Marathon, Half-Marathon, 10K, 5K distances.

options:
  -h, --help            show this help message and exit
  -t TIME, --time TIME  time hh:mm:ss or mm:ss or ss
  -d DISTANCE, --distance DISTANCE
```

### Examples
giving time for 1 km (default):
```bash
python .\running-time.py -t 00:04:17
```

or specifying a distance:
```bash
python .\running-time.py -t 00:42:24 -d 10.0 
```
