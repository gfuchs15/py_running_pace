#!/usr/bin/env python3
"""small script for testing functionnality."""

# %% pyrunpace needs to be installed using pip, or call from root
import sys
import pyrunpace

# %% usage
sys.argv = ["example", "--help"]
pyrunpace.main()

# %% Give a time, using default 1km distance
sys.argv = ["example", "-t", "00:04:17"]
pyrunpace.main()

# %% Given also a distance
sys.argv = ["example", "-t", "00:04:17"]
pyrunpace.main()
