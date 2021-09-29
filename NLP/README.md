### NLP : Natural Language Process
* Dataset:
    * [kindle_rating.csv](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/kindle_rating.csv)
    * [tripadvisor.xlsx](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/tripadvisor.xlsx)
    * [Jena climate dataset](https://drive.google.com/file/d/1s6rQQzMrbCTx8YY2Z5MnAEfnHyRA4qYa/view?usp=sharing)
    * [dict.txt.big](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/dict.txt.big)
    * [stop.txt](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/stop.text)
    * [news.txt](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/news.txt)
### NLTK
* [NLTK Book: CH1.1](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/python_NLTK_Ch1_1.ipynb)
* [11-1 BOW](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/11_01_BOW.ipynb)
* [11-2 TF-IDF](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/11_02_TFIDF.ipynb)
* [11-3_字詞前置處理](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/11_03_%E5%AD%97%E8%A9%9E%E5%89%8D%E7%BD%AE%E8%99%95%E7%90%86.ipynb)
* [11-07 以jieba套件進行中文分詞](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/11_07_%E4%B8%AD%E6%96%87_NLP.ipynb)
* [CH16 NLP](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/Ch16_NLP.ipynb)
* [CH17 NLP -- Amazon](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/Ch17_NLP_Amazon.ipynb)
* [CH18 NLP -- Chinese](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/CH18_NLP_Chinese.ipynb)
* [中文文字雲](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/WordCloud_%E4%B8%AD%E6%96%87.ipynb)
### RNN LSTM
* [女神書第六章範例](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/Ch06-RNN-TF1.ipynb)
* [女神書第七章範例 LSTM -- MNIST](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/07_lstm-TF1.ipynb)
* [RNN](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/04-1.%20RNN.ipynb)
* [RNN -- IMDB](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/04_1_%E7%94%A8RNN%E5%81%9A%E6%83%85%E6%84%8F%E5%88%86%E6%9E%90.ipynb)
* [CH6 RNN & LSTM -- IMDB TF2](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/DL_TF2-Ch06-Workshop-RNN_and_LSTM-IMDB_Dataset.ipynb.ipynb)
* [sequence data -- CNN & RNN](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/15_processing_sequences_using_rnns_and_cnns.ipynb)
* [NLP -- RNN & Attentions](https://github.com/jumbokh/nknu-class/blob/main/NLP/notebooks/16_nlp_with_rnns_and_attention.ipynb)
* [kaggle: bitcoin](https://www.kaggle.com/mczielinski/bitcoin-historical-data/version/16) 
##
### 參考
* [CNN & RNN](https://github.com/jumbokh/intro-computers/blob/master/CNN-RNN.md)
* [swesome RNN](https://github.com/kjw0612/awesome-rnn)
* [Text Classification with CNN and RNN](https://github.com/gaussic/text-classification-cnn-rnn)
* [Predict stock market prices using RNN](https://github.com/lilianweng/stock-rnn)
* [chatbot-rnn](https://github.com/pender/chatbot-rnn)
* [jieba-tw](https://github.com/APCLab/jieba-tw)
* [仿宋體字形](https://github.com/micmro/Stylify-Me/blob/master/.fonts/SimSun.ttf)
* [中文斷詞與文字雲教學](http://120.108.221.55/profchwu/dctai/%E6%95%99%E6%9D%90/%E6%96%B7%E8%A9%9E%E8%88%87%E6%96%87%E5%AD%97%E9%9B%B2/%E6%96%B7%E8%A9%9E%E8%88%87%E6%96%87%E5%AD%97%E9%9B%B2%E6%95%99%E5%AD%B8.pdf)
### Book
* [用python進行自然語言處理](https://www.nltk.org/book/)
* [博客來 -- Natural Language Processing with Python](https://www.books.com.tw/products/F011662715)
### jieba
# jieba-tw

結巴(jieba)斷詞台灣繁體 特化版本


## 原理

採用和原始jieba相同的演算法，替換其詞庫及HMM機率表製做出針對台灣繁體的jieba斷詞器


## 安裝

```sh
pip install git+https://github.com/APCLab/jieba-tw.git
```

## 使用

本專案特化部分如下

```python
import jieba

jieba.case_sensitive = True # 可控制對於詞彙中的英文部分是否為case sensitive, 預設False
```

## 斷詞

```python
import jieba

#如果您的電腦同時要使用兩個版本的jieba，請自訂cache檔名，避免兩個cache互相蓋住對方
#jieba.dt.cache_file = 'jieba.cache.new'

seg_list = jieba.cut("新竹的交通大學在新竹的大學路上")
print(" / ".join(seg_list))
# 新竹 / 的 / 交通 / 大學 / 在 / 新竹 / 的 / 大學路 / 上 /

```

其餘操作請參考[結巴官方文件]

[結巴官方文件]: https://github.com/fxsjy/jieba
