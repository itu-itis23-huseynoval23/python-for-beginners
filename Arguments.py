# Accepting Arguments
print("hello")

import sys
name = sys.argv[1]
print("Hello " +name)

import argparse

parser = argparse.ArgumentParser(
    description = "This program prints the name of my dogs"
)