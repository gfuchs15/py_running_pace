# pyrunpace

Small package/script that computes pace per km from a time and distance in km.\

It also gives expected times for common running distances, assuming the average computed pace.

## Package installation (recommended)

Install the package with pip:
```bash
python -m pip install .
```

## Usage

Using directly the (installed or located in path) module:
```bash
python -m pyrunrace --help
```
or using the installed command line executable:
```bash
pyrunrace[.exe] --help
```

```bash
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
python -m pyrunpace -t 00:04:17
```

or specifying a distance:
```bash
python -m pyrunpace -t 00:42:24 -d 10.0 
```
