# Install OpenCV on Raspberry
https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/
https://www.pyimagesearch.com/opencv-tutorials-resources-guides/


####### TEST WITH DARKNET (Raspberry) #######

# Install Darknet
https://pjreddie.com/darknet/install/

# Install OpenCV
https://www.alatortsev.com/2018/04/27/installing-opencv-on-raspberry-pi-3-b/

# Activar Environment
$ source ~/.profile

# Cambiar Enviroment
$ workon cv 

# Test Yolo
https://pjreddie.com/darknet/yolo/

# Mejor tutorial
https://github.com/leehaesung/YOLO-Powered_Robot_Vision

# Probar la libreria
[Funciona pero no dibuja los cuadros de deteccion]
./darknet detect cfg/yolov1.cfg yolo.weights data/dog.jpg

[Bus error]
./darknet detect cfg/yolov3-tiny.cfg yolov3.weights data/dog.jpg
ref: [puede ser un tema del SD card] https://raspberrypi.stackexchange.com/questions/19634/frequent-bus-error-and-input-output-error-problem


####### TEST WITH OPEN CV (Raspberry) #######

# Index projects
https://www.pyimagesearch.com/practical-python-opencv/?src=pi-opencv-install

# Setup de la camara 
https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

# Errores comunes
https://www.pyimagesearch.com/2016/08/29/common-errors-using-the-raspberry-pi-camera-module/

# Funciono
$ python real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel


####### TEST WITH OPEN CV (Raspberry) #######
### Articulo de pyimagesearch (sin probar)
https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/

# Reading barcodes with Python and OpenMV
https://www.pyimagesearch.com/2018/03/19/reading-barcodes-with-python-and-openmv/

# Deep learning and Google Images for training data
https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/

# OpenCV OCR and text recognition with Tesseract
https://www.pyimagesearch.com/2018/09/17/opencv-ocr-and-text-recognition-with-tesseract/

# OpenCV Object Tracking
https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/
$ python opencv_object_tracking.py --video dashcam_boston.mp4 --tracker csrt

# Tracking multiple objects with OpenCV
https://www.pyimagesearch.com/2018/08/06/tracking-multiple-objects-with-opencv/

# Fire detection
https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html

# Fire detection in video
https://vgg.fiit.stuba.sk/2015-02/2755/

# Face recognition with OpenCV, Python, and deep learning
https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/

# Object Tracking using OpenCV (C++/Python) (Muy buena documentacion)
https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/

# OpenCV Saliency Detection: Otra opcion para seguimiento
https://www.pyimagesearch.com/2018/07/16/opencv-saliency-detection/#comment-471161

#################### TS #################### 
-----------------------------------
raspberry yolo Segmentation fault

https://github.com/DT42/BerryNet
-----------------------------------
libQtGui.so.4: cannot open shared object file
ref [funciono]: https://www.reddit.com/r/linux4noobs/comments/5058s8/help_libqtguiso4_cannot_open_shared_object_file/
sudo apt-get install libqtgui4
-----------------------------------
libQtTest.so.4: cannot open shared object file:
ref [funciono]: https://raspberrypi.stackexchange.com/questions/83648/how-can-i-use-opencv-with-python-3-on-a-raspberry-pi
sudo apt install libqt4-test
-----------------------------------
Error retrieving accessibility bus address: org.freedesktop.DBus.Error.ServiceUnknown: The name org.a11y.Bus was not provided by any .service files
https://lb.raspberrypi.org/forums/viewtopic.php?t=196070
sudo apt-get install at-spi2-core
-----------------------------------
from imutils.video import VideoStream ImportError: No module named 'imutils'
https://github.com/jrosebr1/imutils/issues/39
$ workon your_env_name
$ pip install imutils
-----------------------------------
raise PiCameraMMALError(status, prefix)
picamera.exc.PiCameraMMALError: Failed to enable connection: Out of resources

-----------------------------------

AttributeError: module 'cv2.cv2' has no attribute 'TrackerCSRT_create'
https://stackoverflow.com/questions/44633378/attributeerror-module-cv2-cv2-has-no-attribute-createlbphfacerecognizer
https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/

-----------------------------------
-----------------------------------
-----------------------------------
#################### TS
```sh
# Enable Environment
source ~/.profile
# Change Enviroment
workon cv 
# Enable openCV
sudo ln -s /usr/local/python/cv2 cv2
```

## Camera is enable

```sh
raspistill -v -o test.jpg
```

```sh
sudo find . -name test_video.py
cd ~/opencv/pi-object-detection
python test_video.py
```
