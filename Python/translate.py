"""
Takes in a value and maps it from a range to another range, for example:

6 came from a range between 1, 500 but you want it to be 0, 100
new_val = translate(6, 1, 500, 0, 100)

CREDITS: https://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another Adam Luchjenbroers
"""

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)
