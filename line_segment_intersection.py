"""
Computes wheather 2 line segments (defined by a start and end point) are intersecting
Source: https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
"""

# assumes line segments are stored in the format [(x0,y0),(x1,y1)]
def intersects(s0,s1):
	dx0 = s0[1][0]-s0[0][0]
	dx1 = s1[1][0]-s1[0][0]
	dy0 = s0[1][1]-s0[0][1]
	dy1 = s1[1][1]-s1[0][1]
	p0 = dy1*(s1[1][0]-s0[0][0]) - dx1*(s1[1][1]-s0[0][1])
	p1 = dy1*(s1[1][0]-s0[1][0]) - dx1*(s1[1][1]-s0[1][1])
	p2 = dy0*(s0[1][0]-s1[0][0]) - dx0*(s0[1][1]-s1[0][1])
	p3 = dy0*(s0[1][0]-s1[1][0]) - dx0*(s0[1][1]-s1[1][1])
	return (p0*p1<=0) and (p2*p3<=0)
