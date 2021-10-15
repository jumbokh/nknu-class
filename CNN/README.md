### CNN 練習
### NoteBooks 
#### DL_Book [github: DL_Book](https://github.com/mc6666/DL_Book)
* [書籍範例及資料下載](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/BookData_DM2145.ipynb)
* [雲端硬碟掛載](https://github.com/jumbokh/nknu-class/blob/main/notebook/CloudData.ipynb)
* [使用 cuDNN驅動執行+GPU](https://github.com/jumbokh/nknu-class/blob/main/CNN/notebooks/WithDriver.ipynb)
### 第七章 Pre-trained Model
* [Keras Application](https://keras.io/zh/applications/) [,English](https://keras.io/api/applications/)
    * [code: 07.01 Keras Applications](https://github.com/jumbokh/nknu-class/blob/main/CNN/notebooks/07_01_Keras_applications.ipynb)
* [numpy :: calculate the cosine distance between the features](https://www.codestudyblog.com/cnb2001/0119184904.html)
    * [code: 07.02 圖形相似度比較](https://github.com/jumbokh/nknu-class/blob/main/CNN/notebooks/07_02_%E5%9C%96%E5%83%8F%E7%9B%B8%E4%BC%BC%E5%BA%A6%E6%AF%94%E8%BC%83.ipynb)
* [使用 ResNet152V2 Model，辨識花朵資料集, 07.03](https://github.com/jumbokh/nknu-class/blob/main/CNN/notebooks/07_03_Flower_ResNet.ipynb)
* [Batch Normalization](http://violin-tao.blogspot.com/2018/02/ml-batch-normalization.html)
* [Covariate Shift](https://ithelp.ithome.com.tw/articles/10241052)
* [On The Perils of Batch Norm](https://www.alexirpan.com/2017/04/26/perils-batch-norm.html)
##
## III 進階的影像應用
* 物件偵測(Object Detection)
* 語義分割(Semantic Segmentation)
* 人臉辨識(Facial Recognition)
* 風格轉換(Style Transfer)
* 光學文字辨識(OCR)
### 第八章 物件偵測 (Object Detection)
* 對圖片滑動視窗並做影像金字塔
    * [8.01](https://github.com/jumbokh/nknu-class/blob/main/CNN/notebooks/08_01_Sliding_Window_And_Image_Pyramid.ipynb)
    * [Sliding Windows for Object Detection with Python and OpenCV](https://www.pyimagesearch.com/2015/03/23/sliding-windows-for-object-detection-with-python-and-opencv/)
    * [py](https://github.com/jumbokh/nknu-class/blob/main/CNN/notebooks/08_01_Sliding_Window.py)
* HOG Face Detection
    * [8.02](https://github.com/jumbokh/nknu-class/blob/main/CNN/notebooks/08_02_HOG_Face_Detection.ipynb)
    * [Non-Maximum Suppression for Object Detection in Python](https://www.pyimagesearch.com/2014/11/17/non-maximum-suppression-object-detection-python/)
    * [8.2-1 py](https://github.com/jumbokh/nknu-class/blob/main/CNN/notebooks/08_02_HOG-Face-Detection-1.py)
    * [8.2-2 py](https://github.com/jumbokh/nknu-class/blob/main/CNN/notebooks/08_02_HOG-Face-Detection-2.py)
* Object Detection
    * [8.03](https://github.com/jumbokh/nknu-class/blob/main/CNN/notebooks/08_03_Object_Detection.ipynb)
    * [08.03 py](https://github.com/jumbokh/nknu-class/blob/main/CNN/notebooks/08_03_object_detection.py)
    * [Turning any CNN image classifier into an object detector with Keras, TensorFlow, and OpenCV](https://www.pyimagesearch.com/2020/06/22/turning-any-cnn-image-classifier-into-an-object-detector-with-keras-tensorflow-and-opencv/)
    * <img src="https://github.com/jumbokh/nknu-class/blob/main/CNN/notebooks/before_NMS.JPG" width="100" height="100">
    * <img src="https://github.com/jumbokh/nknu-class/blob/main/CNN/notebooks/after_NMS.JPG" width="100" height="100">
* 8-4 R-CNN 物件偵測 Regions with CNN, Ross B. Girshick, 2014 (Rich feature hierarchies for accurate object detection and semantic segmentation)
    * [Starter: Airplanes Dataset for R-CNN 67f31bc9-1](https://www.kaggle.com/kerneler/starter-airplanes-dataset-for-r-cnn-67f31bc9-1)
    * [Step-By-Step Implementation of R-CNN from scratch in python](https://github.com/1297rohit/RCNN)
    * [Intersection over Union (IoU) for object detection](https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)
    * [8.04 R-CNN 偵測空照圖中的飛機(記憶體不足，無法在colab執行)](https://github.com/jumbokh/nknu-class/blob/main/CNN/RCNN/08_04_RCNN.ipynb)
* 架構如下:
    * 1. 讀取要辨識的圖片。
    * 2. 使用區域推薦(Region Proposal)演算法，找到2000個候選視窗。(Selective Search)
    * 3. 使用CNN萃取特徵。
    * 4. 使用SVM辨識。
* [Getting Started with Detectron2](https://detectron2.readthedocs.io/en/latest/tutorials/getting_started.html)
    * [detectron2 Tutorial](https://github.com/jumbokh/nknu-class/blob/main/CNN/Detectron2/Detectron2_Tutorial.ipynb)
* 8-5 YOLO 演算法、8-6 YOLO 環境建置
    * [YOLO 官網](https://pjreddie.com/)
    * YOLO CFG: [yolov3.cfg](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
* 8-7 以 Tensorflow 實作 YOLO 模型
    * [將YOLO權重檔轉為Keras格式檔(.h5)](https://github.com/jumbokh/nknu-class/blob/main/CNN/YOLO/08_05_YOLO_Keras_Conversion.ipynb)

### 參考
* [JFIF 說明](https://cloud.tencent.com/developer/article/1427939)
* [shap Test](https://github.com/jumbokh/nknu-class/blob/main/CNN/notebooks/Shap_Test.ipynb)
* [AI MONGO](https://drive.google.com/drive/folders/1Yg2qKv9A4CmZhVfyjQZZJdPHGK_yQ9Vv?usp=sharing)
