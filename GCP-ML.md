## 使用Google Cloud的機器學習服務
### [【懶人包】Google Cloud 基礎教學資源彙集](https://ikala.cloud/google-cloud-products-quick-start/)
### [開始使用 Google Cloud](https://cloud.google.com/docs?authuser=1)
* [Quick start](https://cloud.google.com/storage/docs/quickstart-gsutil?hl=zh-tw)
* [註冊帳號](https://cloud.google.com/)
* [Cloud SDK](https://cloud.google.com/sdk/?&_ga=2.46617319.-1772323265.1635597182#download)
* [SDK 安裝說明](https://cloud.google.com/sdk/docs/install)
* [建立專案: like: [nknu-ai-class]](https://console.cloud.google.com/projectcreate)
* [搜尋: cloud vision api](https://console.cloud.google.com/marketplace/product/google/vision.googleapis.com?q=search&referrer=search&authuser=1&project=nknu-ai-class)
* gcloud init or gcloud auth login
<pre>
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
##
### Create bucket
gsutil mb -b on -l asia-east1 gs://jumbo-gcloud-bucket/
gsutil ls gs://jumbo-gcloud-bucket/
gsutil cp Desktop/kitten.png gs://jumbo-gcloud-bucket/
## setting for rpi
## https://rclone.org/drive/#making-your-own-client-id
</pre>
##
### [Cloud Vision API](https://github.com/jumbokh/gcp_class/tree/master/VISION)
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
