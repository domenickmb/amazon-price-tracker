#!/usr/bin/env python
import sys

import config
import tracker

if __name__ == '__main__':
    if len(sys.argv) != 2:
        tracker.print_help()
    command = sys.argv[1]
    if command == 'initialize':
        config.initialize()
    elif command == 'start':
        tracker.start_tracking()
    else:
        print(f"Error: Unknown command '{sys.argv[1]}'")
        tracker.print_help()
