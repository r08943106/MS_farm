import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
import time
import win32gui


def screenshot_window():
    window_title="MapleStory"
    hwnd = win32gui.FindWindow(None, window_title)
    x, y, x1, y1 = win32gui.GetClientRect(hwnd)
    x, y = win32gui.ClientToScreen(hwnd, (x, y))
    x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
    return pyautogui.screenshot(region=(x, y, x1, y1))
    
def WindowBound():
    window_title="MapleStory"
    hwnd = win32gui.FindWindow(None, window_title)
    x, y, x1, y1 = win32gui.GetClientRect(hwnd)
    x, y = win32gui.ClientToScreen(hwnd, (x, y))
    return x,y,x1, y1


def multi_template_matching(img, template, threshold, method=cv.TM_CCOEFF_NORMED):

    # Apply template Matching
    res = cv.matchTemplate(img,template,method)
    loc = np.where(res >= threshold)
    return loc

def draw_box(img,loc,h,w,c):

    num_det = len(loc[0])
    x2 = loc[1] + np.repeat(w,num_det) 
    y2 = loc[0] + np.repeat(h,num_det)
    boxes = np.column_stack((loc[1],loc[0], x2, y2))
    #print(loc[1],loc[0])
    
    for box in boxes:
        cv.rectangle(img,(box[0],box[1]), (box[2],box[3]), c , 2)

    return img

def Distance(x,y,x1,y2):
    return abs(x-x1)+abs(y-y2)

def closest_object(me, objects):
    if len(objects)==0:
        return [[-1],[-1]]
    my_x, my_y = me[0], me[1]
    min_obj = [[objects[0][0]],[objects[1][0]]]
    min_value = Distance(my_x, my_y,objects[0][0],objects[1][0])
    for i in range(len(objects[0])):
        distance = Distance(my_x, my_y,objects[0][i],objects[1][i])
        if distance<min_value:
            min_obj = [[objects[0][i]],[objects[1][i]]]
            min_value = distance
    return np.array(min_obj)



