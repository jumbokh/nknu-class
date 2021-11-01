## 使用Google Cloud的機器學習服務
### 參考
* [【懶人包】Google Cloud 基礎教學資源彙集](https://ikala.cloud/google-cloud-products-quick-start/)
* [快速啟用 Cloud AutoML Vision](https://ikala.cloud/cloud-automl-vision-quick-start/)
* [使用GCP部署機器學習API](https://ithelp.ithome.com.tw/articles/10252383)
* [開始使用 Google Cloud](https://cloud.google.com/docs?authuser=1)
* [VISION python code](https://cloud.google.com/vision/automl/object-detection/docs/samples/automl-vision-object-detection-predict?authuser=1#automl_vision_object_detection_predict-python)
* [Getting Start with Keras on GCP](https://github.com/jumbokh/nknu-class/blob/main/notebooks/getting_started_keras.ipynb)
* [啟用API: AI Platform Training & Prediction API](https://console.cloud.google.com/marketplace/product/google/ml.googleapis.com?authuser=1&project=ailatform-keras-jumbo)
* [AI Platform Training & Prediction API](https://console.cloud.google.com/marketplace/product/google/ml.googleapis.com?authuser=1&project=ailatform-keras-jumbo)
* [How to access files from Google Cloud Storage in Colab Notebooks](https://medium.com/analytics-vidhya/how-to-access-files-from-google-cloud-storage-in-colab-notebooks-8edaf9e6c020)
### Example Program
* [5.2 - Using convnets with small datasets](https://github.com/jumbokh/nknu-class/blob/main/CNN/notebooks/5.2-using-convnets-with-small-datasets.ipynb)
* [Colab: gcp and Cats vs Dog Small Data Set](https://github.com/jumbokh/nknu-class/blob/main/notebooks/Cats_Dogs_GCP.ipynb)
* [Colab: gcp Storage File OP](https://github.com/jumbokh/nknu-class/blob/main/notebooks/gcloud_fileop.ipynb)
* [Getting started: Training and prediction with Keras in AI Platform](https://github.com/jumbokh/nknu-class/blob/main/notebooks/PetImages_keras.ipynb)
### 開始使用 Google Cloud Platform
* [Quick start](https://cloud.google.com/storage/docs/quickstart-gsutil?hl=zh-tw)
* [註冊帳號](https://cloud.google.com/)
* [Cloud SDK](https://cloud.google.com/sdk/?&_ga=2.46617319.-1772323265.1635597182#download)
* [Installing Cloud SDK](https://cloud.google.com/sdk/docs/install#deb)
* [SDK 安裝說明](https://cloud.google.com/sdk/docs/install)
* [建立專案: like: [nknu-ai-class]](https://console.cloud.google.com/projectcreate)
* [搜尋: cloud vision api](https://console.cloud.google.com/marketplace/product/google/vision.googleapis.com?q=search&referrer=search&authuser=1&project=nknu-ai-class)
* gcloud init or gcloud auth login
<pre>
E:\GCP>gcloud auth login
E:\GCP>gcloud config set project nknu-ai-class
E:\GCP>gcloud compute regions list
API [compute.googleapis.com] not enabled on project [41275790770]. Would you like to enable and retry (this will take a
few minutes)? (y/N)?  y

Enabling service [compute.googleapis.com] on project [41275790770]...
</pre>
* [主機佈署](https://robarter.pixnet.net/blog/post/223284367-%5Bgcp%5Dgoogle%E9%9B%B2%E7%AB%AF%E6%9E%B6%E7%AB%99%282.1%29---%E9%81%B8%E6%93%87%E5%90%88%E9%81%A9%E7%9A%84%E9%83%A8%E5%B1%AC%E4%BD%8D%E7%BD%AE)
<pre>
# 設定 region & timezone
gcloud compute project-info add-metadata --metadata google-compute-default-region=asia-east1,google-compute-default-zone=asia-east1
</pre>
## [使用 Google Storage](https://cloud.google.com/storage/docs/quickstart-gsutil?hl=zh-tw)
<pre>
# 注意: 資料集要放在 us-central1 的主機上(僅 Vision Auto ML)，不然要設定成跨區域
# Create bucket
gsutil mb -b on -l us-central1 gs://jumbo-gcloud-bucket/
gsutil ls gs://jumbo-gcloud-bucket/
gsutil cp Desktop/kitten.png gs://jumbo-gcloud-bucket/
## setting for rpi
## https://rclone.org/drive/#making-your-own-client-id
</pre>
##
<pre>
gsutil ls -r gs://willchad_vcm/WillChad > file_list.cv
# edit file_list.csv
</pre>
### [Lab for Cloud Vision API](https://github.com/jumbokh/gcp_class/tree/master/VISION)
### Create image dataset
<pre>
jumbokh@cloudshell:~ (nknu-ai-class)$ gsutil ls gs://jumbo_vision_bucket
gs://jumbo_vision_bucket/ChuNewSong/
jumbokh@cloudshell:~ (nknu-ai-class)$ gsutil ls gs://jumbo_vision_bucket/ChuNewSong
gs://jumbo_vision_bucket/ChuNewSong/Chu/
gs://jumbo_vision_bucket/ChuNewSong/New/
gs://jumbo_vision_bucket/ChuNewSong/Song/
jumbokh@cloudshell:~ (nknu-ai-class)$ gsutil ls gs://jumbo_vision_bucket/ChuNewSong/Chu > a1
jumbokh@cloudshell:~ (nknu-ai-class)$ gsutil ls gs://jumbo_vision_bucket/ChuNewSong/New > a2
jumbokh@cloudshell:~ (nknu-ai-class)$ gsutil ls gs://jumbo_vision_bucket/ChuNewSong/Song > a3
jumbokh@cloudshell:~ (nknu-ai-class)$ cat a1 a2 a3 > files.list
jumbokh@cloudshell:~ (nknu-ai-class)$ less files.list
jumbokh@cloudshell:~ (nknu-ai-class)$ gsutil cp files.list gs://jumbo_vision_bucket/ChuNewSong
Copying file://files.list [Content-Type=application/octet-stream]...
/ [1 files][  8.9 KiB/  8.9 KiB]
Operation completed over 1 objects/8.9 KiB.
jumbokh@cloudshell:~ (nknu-ai-class)$
</pre>
* ![create dataset](https://github.com/jumbokh/nknu-class/blob/main/docs/vision_dataset.JPG)
* ![vision train](https://github.com/jumbokh/nknu-class/blob/main/docs/vision_train.JPG)
* ![Vision Auto ML Train Result](https://github.com/jumbokh/nknu-class/blob/main/docs/result.JPG)
* ![Model predict](https://github.com/jumbokh/nknu-class/blob/main/docs/predict.JPG)
* ![Model](https://github.com/jumbokh/nknu-class/blob/main/docs/model.JPG)
