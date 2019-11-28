###第1行和第2行是标准注释，第1行注释可以让这个文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；###

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import collections    #collections是Python内建的一个集合模块，提供了许多有用的集合类。
import SimpleITK as sitk
import pdb            #pdb为Python程序定义了一个交互式源代码调试器

from scipy.ndimage.interpolation import zoom
#scipy.ndimage提供了一些基础的多维图像处理功能,Interpolation：图像的插值、旋转以及仿射变换，zoom表示缩放
#图像插值是在基于模型框架下，从低分辨率图像生成高分辨率图像的过程，用以恢复图像中所丢失的信息。

from keras.applications.xception import Xception
#Keras的应用模块Application提供了带有预训练权重的Keras模型，这些模型可以用来进行预测、特征提取和微调
#Xception（极致的 Inception）：先进行普通卷积操作，再对1×1 1×1 1×1卷积后的每个channel分别进行3×3 3×3 3×3卷积操作，最后将结果concat

from keras.preprocessing import image
from keras.applications.xception import preprocess_input

model = Xception(weights='imagenet', include_top=False)
#Xception V1 模型, 权重由ImageNet训练而言
#在ImageNet上,该模型取得了验证集top1 0.790和top5 0.945的正确率
#include_top：是否保留顶层的3个全连接网络 ； weights：None代表随机初始化，即不加载预训练权重。'imagenet'代表加载预训练权重

def boundingBox(A, use2D=False):
    # get the coordinates of delineated region from the mask A.
    #从掩模A中获取已划分区域的坐标（矩形块）
    B = np.argwhere(A)   #查找非零数组元素的索引，按元素分组（取非零元素坐标）
    if use2D == True:
        (ystart, xstart), (ystop, xstop) = B.min(axis=0), B.max(axis=0) + 1
        return (ystart, xstart), (ystop, xstop)
    else:
        (zstart, ystart, xstart), (zstop, ystop, xstop) = B.min(axis=0), B.max(axis=0) + 1
        return (zstart, ystart, xstart), (zstop, ystop, xstop)
#如果将三维数组的每一个二维看做一个平面（plane，X[0, :, :], X[1, :, :], X[2, :, :]），三维数组即是这些二维平面层叠（stacked）出来的结果。则（axis=0）表示全部平面上的对应位置，（axis=1），每一个平面的每一列，（axis=2），每一个平面的每一行

def deep_features(imageFilepath, maskFilepath):
    # read Nrrd format images and Nifti format segmentation files 读取Nrrd格式图像和Nifti格式分割文件
    nrrd = sitk.ReadImage(imageFilepath)
    nrrd_array = sitk.GetArrayFromImage(nrrd)  # z, y, x
    # GetArrayFromImage()可用于将SimpleITK对象转换为ndarray，输出形状为：(Depth, Height, Width)横断面，冠状面，矢状面

    # read mask  mask掩膜是用于部分或完全隐藏对象或元素的部分的图形操作，使遮罩内的图像不变化，在图像处理中常用来提取ROI区域
    nii = sitk.ReadImage(maskFilepath)
    nii_array = sitk.GetArrayFromImage(nii)  # z, y, x
    # calculate the coordinates  计算坐标
    (zstart, ystart, xstart), (zstop, ystop, xstop) = boundingBox(nii_array, use2D=False)
    # get the ROI   #获得感兴趣区域
    img0 = nrrd_array[zstart - 1:zstop + 1, ystart:ystop, xstart:xstop]
    uniSize = 224.
    img1 = zoom(img0, zoom=[1, uniSize / img0.shape[1], uniSize / img0.shape[2]], order=3)
    #zoom() 将图片每一维以相应系数缩小
    #input:输入数组img0
    #zoom：浮动或顺序，可选：沿轴的缩放系数。如果为浮动，则每个轴的缩放比例相同。如果是序列，则缩放应为每个轴包含一个值。
    #img0.shape[1] 表示读取img0第二维（也就是y）对应的长度
    #order：样条插值的顺序（默认为3）。顺序必须在0-5的范围内。
    img2 = img1.transpose((2, 1, 0))  #transpose用于对高维数组进行转置 转置时候需要一个由轴编号组成的元组
    img = np.array(img2, dtype=np.float)
 

    # preprocess inputs  #预处理输入
    x = np.expand_dims(iimg, axis=0)   #np.expand_dims:用于扩展数组的形状 表示在iimg的0维添加数据
    #https://blog.csdn.net/qq_43243022/article/details/85683288
    x = preprocess_input(x)    #keras中 preprocess_input() 函数完成数据预处理的工作（#去均值中心化），提高算法的运行效果
    #使用z-score标准化（0-1标准化）经过处理的数据的均值为0，标准差为1
    """
    def preprocess_input(x, data_format=None, mode='caffe'):
       Preprocesses a tensor or Numpy array encoding a batch of images.
        # Arguments
            x: Input Numpy or symbolic tensor, 3D or 4D.
            data_format: Data format of the image tensor/array.
            mode: One of "caffe", "tf".
                - caffe: will convert the images from RGB to BGR,
                    then will zero-center each color channel with
                    respect to the ImageNet dataset,
                    without scaling.
                - tf: will scale pixels between -1 and 1,
                    sample-wise.
        # Returns
            Preprocessed tensor or Numpy array.
        # Raises
            ValueError: In case of unknown `data_format` argument.
    """
    # get deep learning features  #获得深度学习功能
    features = model.predict(x)   #返回一个预测值
    feature_map = features[0].transpose((2, 1, 0)) #feature_map特征图谱
    fearures = np.max(feature_map, -1)
    fearures = np.max(fearures, -1)

    dfs = collections.OrderedDict()  #OrderedDict():实现字典的固定排序,是字典的子类
    #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
    for ind_, f_ in enumerate(fearures):
        dfs[str(ind_)] = f_
    return feature_map, dfs
 

#当我们在命令行运行这个模块文件时，Python解释器把一个特殊变量__name__置为__main__
#而如果在其他地方导入该导入模块时，if判断将失败，
#因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__ == '__main__':
    # read Nrrd format images and Nifti format segmentation files
    # dfs: deep learning features
    imageFilepath = 'path of image/*.nrrd'
    maskFilepath = 'path of mask /*.nii.gz'
    feature_map, dfs = deep_features(imageFilepath, maskFilepath)