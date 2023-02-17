#!/usr/bin/env python3


import argparse
import segment


if __name__ == "__main__":
    """main function"""
    parser = argparse.ArgumentParser(
        description="Running-time: give pace and speed from a time and a distance\
                    - and the times for M, HM, 10K, 5K distances."
    )

    parser.add_argument(
        "-t",
        "--time",
        required=True,
        type=str,
        help="time hh:mm:ss or mm:ss or ss",
        default=None,
    )
    parser.add_argument(
        "-d",
        "--distance",
        required=False,
        type=float,
        help="distance in km",
        default=1,
    )

    args = parser.parse_args()

    print("Running-pace for python")
    print("=======================")

    total_time = args.time
    hours = 0
    minutes = 0
    if total_time.count(":") == 2:
        hours, minutes, seconds = total_time.split(":")
    elif total_time.count(":") == 1:
        minutes, seconds = total_time.split(":")
    else:
        seconds = total_time

    s = segment.Segment(args.distance, int(hours), int(minutes), int(seconds))
    s.printInfo()
