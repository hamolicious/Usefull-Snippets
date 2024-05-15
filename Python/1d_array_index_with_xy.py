"""
https://softwareengineering.stackexchange.com/questions/212808/treating-a-1d-data-structure-as-2d-grid

Takes a 2d index (x and y) and returns an index into a 1d array
"""

def xy_to_i(x: int, y: int) -> int:
  return x + width*y;
