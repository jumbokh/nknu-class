# Scikit-Image 的範例
# 載入套件
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import data, exposure

# 收集正樣本 (positive set)
# 使用 scikit-learn 的人臉資料集
from sklearn.datasets import fetch_lfw_people
faces = fetch_lfw_people()
positive_patches = faces.images
print(positive_patches.shape) 

# 顯示正樣本部份圖片
fig, ax = plt.subplots(4,6)
for i, axi in enumerate(ax.flat):
    axi.imshow(positive_patches[500 * i], cmap='gray')
    axi.axis('off')

# 收集負樣本 (negative set)
# 使用 Scikit-Image 的非人臉資料
from skimage import data, transform, color

imgs_to_use = ['hubble_deep_field', 'text', 'coins', 'moon',
               'page', 'clock','coffee','chelsea','horse']
images = [color.rgb2gray(getattr(data, name)())
          for name in imgs_to_use]
len(images)

# 將負樣本轉換為不同的尺寸
from sklearn.feature_extraction.image import PatchExtractor

# 轉換為不同的尺寸
def extract_patches(img, N, scale=1.0, patch_size=positive_patches[0].shape):
    extracted_patch_size = tuple((scale * np.array(patch_size)).astype(int))
    # PatchExtractor：產生不同尺寸的圖像
    extractor = PatchExtractor(patch_size=extracted_patch_size,
                               max_patches=N, random_state=0)
    patches = extractor.transform(img[np.newaxis])
    if scale != 1:
        patches = np.array([transform.resize(patch, patch_size)
                            for patch in patches])
    return patches

# 產生 27000 筆圖像
negative_patches = np.vstack([extract_patches(im, 1000, scale)
                              for im in images for scale in [0.5, 1.0, 2.0]])
print(negative_patches.shape) 

# 顯示部份負樣本
fig, ax = plt.subplots(4,6)
for i, axi in enumerate(ax.flat):
    axi.imshow(negative_patches[600 * i], cmap='gray')
    axi.axis('off')

# 合併正樣本與負樣本
from skimage import feature   # To use skimage.feature.hog()
from itertools import chain

X_train = np.array([feature.hog(im)
                    for im in chain(positive_patches,
                                    negative_patches)])
y_train = np.zeros(X_train.shape[0])
y_train[:positive_patches.shape[0]] = 1

# 使用 SVM 作二分類的訓練
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV 

# C為矯正過度擬合強度的倒數，使用 GridSearchCV 尋求最佳參數值
grid = GridSearchCV(LinearSVC(dual=False), {'C': [1.0, 2.0, 4.0, 8.0]},cv=3)
grid.fit(X_train, y_train)
print(grid.best_score_)

# C 最佳參數值
print(grid.best_params_) 

# 依最佳參數值再訓練一次
model = grid.best_estimator_
model.fit(X_train, y_train)

# 取新圖像測試
test_img = data.astronaut()
test_img = color.rgb2gray(test_img)
test_img = transform.rescale(test_img, 0.5)
test_img = test_img[:120, 60:160]


plt.imshow(test_img, cmap='gray')
plt.axis('off');

 #滑動視窗函數
def sliding_window(img, patch_size=positive_patches[0].shape,
                   istep=2, jstep=2, scale=1.0):
    Ni, Nj = (int(scale * s) for s in patch_size)
    for i in range(0, img.shape[0] - Ni, istep):
        for j in range(0, img.shape[1] - Ni, jstep):
            patch = img[i:i + Ni, j:j + Nj]
            if scale != 1:
                patch = transform.resize(patch, patch_size)
            yield (i, j), patch

# 使用滑動視窗計算每一視窗的 Hog
indices, patches = zip(*sliding_window(test_img))
patches_hog = np.array([feature.hog(patch) for patch in patches])

# 辨識每一視窗
labels = model.predict(patches_hog)
labels.sum() # 偵測到的總數

# 將每一個偵測到的視窗顯示出來
fig, ax = plt.subplots()
ax.imshow(test_img, cmap='gray')
ax.axis('off')

# 取得左上角座標
Ni, Nj = positive_patches[0].shape
indices = np.array(indices)

# 顯示
for i, j in indices[labels == 1]:
    ax.add_patch(plt.Rectangle((j, i), Nj, Ni, edgecolor='red',
                               alpha=0.3, lw=2, facecolor='none'))

print(patches_hog.shape)

candidate_patches = patches_hog[labels == 1]
print(candidate_patches.shape)

