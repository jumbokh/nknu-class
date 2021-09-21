### [Notebooks](https://github.com/jumbokh/nknu-class/blob/main/ML/notebooks/Notebooks.md)
### Clustering 分群法、[聚類方法](https://github.com/jumbokh/nknu-class/blob/main/docs/%E8%81%9A%E9%A1%9E%E6%96%B9%E6%B3%95.pdf)
<pre>
目的是將相似的實例聚成一組。分群法很適合用於資料分析、顧客細分、推薦系統、
搜尋引擎、圖像分割、半監督學習、降維，及其他
</pre>
### anomaly detection 異常檢測
<pre>
目的是學習 "正常" 的資料長怎麼樣，接著用它來偵測不正常的實例。
</pre>
### density estimation 密度估計
<pre>
目的是估計產生資料集的隨機程序的機率密度函數(PDF)。
密度估計通常用於異常檢測：在密度很低的區域中的實例很有可能是異常的。
他也很適合用來分析資料與視覺化。
</pre>
### K-Means && K Nearest Neighber
<pre>
KNN就是讓你透過一群已經標記好類別的資料，來針對未分類的資料做分類的工具。

那如果只有一群尚未分類的資料，我們要怎麼將他分類呢？
</pre>
##
<pre>
from sklearn.cluster import KMeans
k = 5
kmeans = KMeans(n_clusters=k)
y_pred = kmeans.fit_predict(X)
</pre>
#### K-Means 運作流程
<pre>
1. 先決定K
2. k就是最後要分成幾群，如果你希望最後資料分成 3群 ，k就是3。
3. 在你的資料中，隨機選擇k個點做為群中心(也可以直接從資料挑)。
4. 把每一筆資料標記上離它最近的群中心
5. 根據同一個標記的所有資料，重新計算出群中心。
6. 如果步驟4算出來的群中心跟原本步驟3不同，則重複步驟3
</pre>
##
<pre>
1. 我們要分成兩群(K=2),所以一開始先挑了兩個點(b)。

2. 將資料標記(著色)成距離最近的群中心(c)。

3. 同一個群中心(顏色)的資料重新計算新的中心位置(d)。

4. 同步驟2，做標記(著色的動作)。

5. 同步驟3，重新計算新的群中心的位置(f)。

6. 再重複步驟2,3 結果群中心位置不變，表示分群完畢。
</pre>
##
#### Q&A
<pre>
K-means簡單快速的方法被廣泛的使用，但是實際運用上還是有一些問題需要被克服。正所謂萬事起頭難，K-means一開始會先要求你提供K，但是k到底要多少才合理？ 
</pre>
#### 參考
* [歐幾里得距離](https://zh.wikipedia.org/wiki/%E6%AC%A7%E5%87%A0%E9%87%8C%E5%BE%97%E8%B7%9D%E7%A6%BB)
* [曼哈頓距離](https://zh.wikipedia.org/wiki/%E6%9B%BC%E5%93%88%E9%A0%93%E8%B7%9D%E9%9B%A2)
* [各種距離](https://www.itread01.com/content/1524567619.html)
* [K-近鄰演算法 KNN](https://pyecontech.com/2020/04/19/knn/) 
* [K-近鄰演算法 KNN範例](https://www.itread01.com/content/1546304971.html)
* [机器学习实战--KNN](https://zhuanlan.zhihu.com/p/114396747)
#### 書籍
* [精通機器學習：使用Scikit-Learn, Keras與TensorFlow 第二版](https://www.books.com.tw/products/0010854043?gclid=Cj0KCQjws4aKBhDPARIsAIWH0JVf3gBKAAnbDrWncGpqfxvLBrJuyEIOVsyu_7_5-pYcb4uRh7ikXhQaAtvpEALw_wcB)
* [非監督式學習：使用Python](https://www.books.com.tw/products/0010852754?loc=P_br_r0vq68ygz_D_2aabd0_B_2)
* [一書貫通：從資料科學橫入人工智慧領域](https://www.books.com.tw/products/0010806798)
* [一行指令學Python：用機器學習掌握人工智慧](https://www.books.com.tw/products/0010872905?loc=M_0009_001)
