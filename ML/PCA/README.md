### PCA
#### 維度縮減演算法將高維的資料投影至低維空間，同時透過移除冗餘資訊，儘可能的維持了最多的顯著資訊。
#### PCA 藉由處理特徵間的相關性來達到目的。 如果一個特徵子集內的特徵彼此相關程度很高，PCA 會試著合併
#### 這些高相關的特徵，並且以較少量的線性無關的特徵來表示資料。
#### [GITHUB: Hands-on Unsupervised Learning Using Python](https://github.com/aapatel09/handson-unsupervised-learning)
##### [MNIST 手寫數字資料集](http://yann.lecun.com/exdb/mnist)
    ##### 進行特徵縮放是運用PCA前的必要步驟，但以MNIST資料集來說，特徵值已縮放到0至1的範圍內了，所以可以跳過這個步驟。
### 維度縮減
#### 1. 線性投影
* 主成分分析、奇異值分解、隨機投影
#### 2. 流形學習 (非線性維度縮減)
* isomap、多維度標法 (multidimensional scaling, MDS)、局部線性嵌入 (locally linear embedding, LLE)、
* t-distributed stochastic neighbor embedding (t-SNE)、字典學習、隨機森林嵌入 (random trees embedding)
* 獨立成分分析 (independent component analysis)
##
