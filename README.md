# light_detect
This code, using openCV ,can **detect the light and draw a rectangle as a ROI**

This code was used for my light image, so that **threshold_value and threshold_method can be changed for your image properly**

**This code will draw TOP5 ROIs based on area** 

# How to run
**Install Python**, 

**Install** Python Library -> **numpy, cv2(opencv-python)**

**Edit the cv2.imread path to your own image**

**Run the Code**

# Method
1. Image Read
2. Image Read another one with Gray
3. Set the threshold_value as you want between 0,255
4. Use **cv2.threshold** with **cv2.THRESH_BINARY**
5. Use **cv2.connectedComponentsWithStats** will give you infos about
   "#" of labels for object, object's number, (object's x, y, width, height, area), and center point of object
7. Use **np.argsort** to Sort based on areas
8. Use that index to gather info about left, right, top, bottom infos
9. Use that info to draw rectangle to your image
10. Use **cv2.imshow** to show your own image with ROIs

# Result
![image](https://github.com/msjung8/light_detect/assets/45056638/15a657d2-8784-4952-8d01-d5f461ffdad9)
![image](https://github.com/msjung8/light_detect/assets/45056638/eaba53e6-6926-4b7b-878e-677134e18b9a)

