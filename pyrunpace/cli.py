#!/usr/bin/env python3
"""Command line interface module."""

import argparse

from pyrunpace import segment


def main() -> None:
    """Entry point for the application script.

    Args:
        input_str: string to reverse
        capitalize: if true, capitalize letters of input_str
    """
    parser = argparse.ArgumentParser(
        description="Running-pace: computes pace and speed given time [and distance].\
            It also provides times for Marathon, Half-Marathon, 10K, 5K distances"
    )

    parser.add_argument(
        "-t",
        "--time",
        required=True,
        type=str,
        help="time in hh:mm:ss or mm:ss or seconds",
        default=None,
    )
    parser.add_argument(
        "-d",
        "--distance",
        required=False,
        type=float,
        help="distance in km (default: 1km)",
        default=1,
    )

    args = parser.parse_args()

    print("============")
    print("Running-pace")
    print("============")

    hours = 0
    minutes = 0
    if args.time.count(":") == 1:
        minutes, seconds = args.time.split(":")
    elif args.time.count(":") == 2:
        hours, minutes, seconds = args.time.split(":")
    else:
        seconds = int(float(args.time))

    seg = segment.Segment(args.distance, int(hours), int(minutes), int(seconds))
    seg.print_info()
