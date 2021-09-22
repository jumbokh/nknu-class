### PCA
#### 維度縮減演算法將高維的資料投影至低維空間，同時透過移除冗餘資訊，儘可能的維持了最多的顯著資訊。
* #### PCA 藉由處理特徵間的相關性來達到目的。 如果一個特徵子集內的特徵彼此相關程度很高，PCA 會試著合併
* #### 這些高相關的特徵，並且以較少量的線性無關的特徵來表示資料。
* #### PCA 通常會丟掉一些在原先特徵集內可取得的資訊，通常是拋棄較沒有價值的元素，只留下重要的。
* #### 利用PCA精簡過的特徵集進行訓練的模型精卻度不如使用完整特徵集進行訓練的模型精確度。
* 考慮MNIST圖像，圖像外圍的像素幾乎是白的，所以你可以將訓練集的這些像素完全移除，且不會損失太多資訊。
* PCA可找出訓練組中變異數最大的軸，然後它也可以找出與第一軸正交的第二軸，它佔了剩餘變異度的多數。
* 你該如何找到訓練組的主成分?
    * 用標準的矩陣分解技術 -- 奇異值分解 (Singular Value Decomposition, SVD)
    * 如果降維是為了做資料的視覺化，此時你要將維數降為2或3
    * PCA壓縮:
<pre>
# MNIST 784 -> 154
pca = PCA(n_components = 154)
X_reduced = pca.fit_transform(X_train)
# 恢復784維
X_recovered = pca.inverse_transform(X_reduced)
</pre>
* 選擇成分的數量
<pre>
pca = PCA().fit(digits.data)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance');
</pre>
![曲線](https://github.com/jumbokh/nknu-class/blob/main/ML/PCA/pca.png)
### 維度縮減
#### 1. 線性投影
* 主成分分析、奇異值分解、隨機投影
#### 2. 流形學習 (非線性維度縮減)
* isomap、多維度標法 (multidimensional scaling, MDS)、局部線性嵌入 (locally linear embedding, LLE)、
* t-distributed stochastic neighbor embedding (t-SNE)、字典學習、隨機森林嵌入 (random trees embedding)
* 獨立成分分析 (independent component analysis)
##
#### [GITHUB: Hands-on Unsupervised Learning Using Python](https://github.com/aapatel09/handson-unsupervised-learning)
#### [Github: Handson-ml2](https://github.com/ageron/handson-ml2)
#### [Github: Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook)
##### [MNIST 手寫數字資料集](http://yann.lecun.com/exdb/mnist)
###### 進行特徵縮放是運用PCA前的必要步驟，但以MNIST資料集來說，特徵值已縮放到0至1的範圍內了，所以可以跳過這個步驟。
* [PCA using Python (scikit-learn)](https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60)
##
#### Notebooks
* [python data science handbook: PCA](https://github.com/jumbokh/nknu-class/blob/main/ML/PCA/PCA_1.ipynb)
* [PCA: DatingWeb](https://github.com/jumbokh/nknu-class/blob/main/ML/PCA/PCA_DatedWeb.ipynb)
* [PCA & KNN-1: Dating Web](https://github.com/jumbokh/nknu-class/blob/main/ML/PCA/classified_DatingWeb_1.ipynb)
* [PCA,Select K Best](https://github.com/jumbokh/nknu-class/blob/main/ML/PCA/classified_DatingWeb_2.ipynb)
* [Hand Write digits](https://github.com/jumbokh/nknu-class/blob/main/ML/PCA/05_09_Principal_Component_Analysis.ipynb)
* [Iris KNN,PCA and Select K Best](https://github.com/jumbokh/nknu-class/blob/main/ML/PCA/4_2_KNN%2C_PCA_and_SelectKBest.ipynb)
* [PCA: anomaly detection](https://github.com/jumbokh/nknu-class/blob/main/ML/PCA/04_anomaly_detection.ipynb)
* [03_dimensionality_reduction](https://github.com/jumbokh/nknu-class/blob/main/ML/PCA/03_dimensionality_reduction.ipynb)
* [08_dimensionality_reduction](https://github.com/jumbokh/nknu-class/blob/main/ML/PCA/08_dimensionality_reduction.ipynb)
