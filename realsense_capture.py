import cv2
import pyrealsense2
from realsense_depth import *

point = (400, 300)

def show_distance(event, x, y, args, params):
    global point
    point = (x, y)

# Initialize Camera Intel Realsense
dc = DepthCamera()

# Create mouse event
cv2.namedWindow("Color frame")
cv2.setMouseCallback("Color frame", show_distance)
count = 0

while True:
    ret, depth_frame, color_frame = dc.get_frame()

    # Show distance for a specific pointdetect distance
    # cv2.circle(color_frame, point, 4, (0, 0, 255))
    # distance = depth_frame[point[1], point[0]]

    # cv2.putText(color_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    cv2.imshow("depth frame", depth_frame)
    cv2.imshow("Color frame", color_frame)

    cv2.imwrite('depth/' + str(count) + '.png', depth_frame)
    cv2.imwrite('rgb/' + str(count) + '.png', color_frame)
    count += 1
    key = cv2.waitKey(1)
    if key == 27:
        break