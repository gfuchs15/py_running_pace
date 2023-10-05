#!/usr/bin/env python3
"""small script for testing functionnality."""

# %% pyrunpace needs to be installed using pip, or call from root
import sys
from pyrunpace import cli

# %% usage
# sys.argv = ["example", "--help"]
# cli.main()

# %% Give a time, using default 1km distance
print("Using the CLI")
sys.argv = ["example", "-t", "00:04:17"]
cli.main()


# %% Using the segement module
print("Using the module")
from pyrunpace import segment

seg = segment.Segment(distance=1, hours=0, minutes=4, seconds=17)
seg.print_info()

print(cli.__doc__)
