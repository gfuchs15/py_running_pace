# py_running_pace
Small script that computes pace per km from a time and distance in km.\\
It also gives expected times for common running distances, assuming the average computed pace.

## Installation (optional)

Build the wheel and then install it with pip:
```bash
python setup.py bdist_wheel
pip instal ./dist/*.whl
```

## Usage

```
Running-pace: computes pace and speed given time [and distance]. It also provides times for Marathon, Half-Marathon, 10K, 5K distances.

options:
  -h, --help            show this help message and exit
  -t TIME, --time TIME  time in hh:mm:ss or mm:ss or seconds
  -d DISTANCE, --distance DISTANCE
                        distance in km (default: 1km)
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
