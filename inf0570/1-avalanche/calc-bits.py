#!/usr/bin/env python3
import sys


def calculate_rate(bits1, bits2):
    if len(bits1) != 128 or len(bits2) != 128:
        print("error: invalid lengths")
        exit(1)
    matches = 128
    for idx in range(128):
        matches = matches - 1 if bits1[idx] == bits2[idx] else matches
    return matches / 128


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"usage: {sys.argv[0]} BITS_STREAM1 BIT_STREAM2")
        exit(1)

    bits1 = sys.argv[1]
    bits2 = sys.argv[2]
    rate = calculate_rate(bits1, bits2)
    print(rate)
