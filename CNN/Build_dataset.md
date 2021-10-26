## Build image dataset
* **建立資料集目錄**
### 例:
###   dataset
###     Jackie_Wu
###     JJ_Lin
* **網路搜尋影像檔**
    * 建立 Azure image Service [快速入門：使用 Bing 影像搜尋 REST API 和 Python 來搜尋影像](https://docs.microsoft.com/zh-tw/azure/cognitive-services/bing-image-search/quickstarts/python)
    * 取得: key, end point
         * python bing_search.py --query "吳宗憲" --output dataset/Jackie_Wu
         * python bing_search.py --query "林俊傑" --output dataset/JJ_Lin
    * 檢視影像檔, 刪除太多人或非人像、本人等
* **建立特徵檔**
    * python encode_faces.py --dataset dataset --encodings encodings.pickle
* **測試**
    * python recognize_faces_image.py --encodings encodings.pickle --image examples/example_01.png
### 參考
* [快速入門：使用 Bing 影像搜尋用戶端程式庫](https://docs.microsoft.com/zh-tw/azure/cognitive-services/bing-image-search/quickstarts/client-libraries?tabs=visualstudio&pivots=programming-language-csharp)
* [search sample code I](https://github.com/nikitaa30/Face-Recognition)
* [search sample code II](https://github.com/Azure-Samples/cognitive-services-python-sdk-samples/tree/master/samples/search)
* [Face recognition with OpenCV, Python, and deep learning](https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/)
* [How to (quickly) build a deep learning image dataset](https://www.pyimagesearch.com/2018/04/09/how-to-quickly-build-a-deep-learning-image-dataset/)
