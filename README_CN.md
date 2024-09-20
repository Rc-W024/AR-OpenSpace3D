# 虚拟3D模型真实现实技术的应用
[English](README.md) | 中文

![](https://skillicons.dev/icons?i=py)

该项目通过三维建模与编程相结合，以实现虚拟现实（VR）、真实现实（AR）及其相关技术应用。通过3D模型与[OpenSpace3D](https://www.openspace3d.com/)编辑器实现智能交互，允许用户基于VR技术对模型进行相应操作。

软件可通过该链接安装：https://www.openspace3d.com/lang/en/support/download/

## 任务框架
### 监视与跟踪
- 基于标记的识别系统。将代表虚拟信息的物理标记显示在给定的投影平面上。下图显示了在标记坐标系中投影3D对象的所需步骤。

![215047881-25abca24-b2ad-4741-87e7-db91c8adea86](https://user-images.githubusercontent.com/97808991/224477574-ec960685-531f-464b-996f-13b29fe270e3.png)

- 基于图像识别的无标记系统。在这种情况下，标记可以是任何图像（更消耗资源），以查找与参考图像匹配的图案。

### 移动设备传感器定位
GPS用于定位，罗盘用于定向，加速度计用于确定倾角。通过在手机中看到的图像上绘制与当前位置重合的多媒体内容。

## Python & AR
AR的基础是模拟自然视觉过程，这正是摄影测量技术所研究的。利用摄影测量中立体视觉的原理，我们的大脑就能够根据每只眼睛给出的两个二维图像形成一个三维世界。

在计算机视觉中，眼睛被从现实世界中捕捉图像的相机所取代。在捕获过程中，第三维度丢失，生成的图像以像素为单位存储在二维坐标系中。因此，问题就“简化”为寻找“对象”系统（3D）中点的坐标与“图像”系统（2D）中相同点坐标之间的对应关系，从中我们就能知道相机相对于目标系统的位置和方向，因此可将任何3D坐标“投影”到图像系统上。

Python中的OpenCV库可用来了解AR应用程序的基础知识。这是一个非常强大的专用于计算机视觉的库，它允许执行诸如检测图像中的相关特征、相机校准和计算目标点和图像点之间对应关系等任务。

在`liberias`文件夹中上传了一些适用于Python 2.7的库文件，包括matplotlib、numpy和opencv，`scripts`文件夹中包含了一些有关校准、捕获、检测、提取和投影的参考代码。在安装了必要的组件后，可以从以下链接安装最新的库文件。

安装必要的组件后，可通过该链接安装最新的库：https://sourceforge.net/projects/opencvlibrary/files/

## 项目信息
在本项目中，使用了先前已创建好的3D模型（.obj文件），并使用笔记本电脑自带的本地摄像头完成人机交互。使用[`plantilla`](https://github.com/Rc-W024/AR-OpenSpace3D/blob/main/plantilla.pdf)模板作为标记面板，允许模型根据应用程序使用的标签（模型和虚拟按钮）进行排列。面板中模型展示标记尺寸为8x8厘米，控制按钮为3x3厘米。

## 结果
### 模型展示
![image](https://user-images.githubusercontent.com/97808991/215061642-14f7c140-fa34-4f58-b495-91606b00d6c2.png)

### 模型隐藏
![image](https://user-images.githubusercontent.com/97808991/215061984-12b40011-2658-4a98-bdbf-c5d23bfa518d.png)

### 位移（模型与底座分离）
![image](https://user-images.githubusercontent.com/97808991/215062132-c397ba98-797b-4e1e-820e-faac0e996f9a.png)

### 放大
![image](https://user-images.githubusercontent.com/97808991/215062203-fa6c38e0-a3f5-4336-b5a0-84ca86f21a92.png)

### 旋转
![image](https://user-images.githubusercontent.com/97808991/215062299-baf0a216-52c4-4c26-8373-eac74536e3e7.png)

## 演示
https://github.com/Rc-W024/AR-OpenSpace3D/assets/97808991/b0c27dd4-edc8-4af9-b3b7-29226ea4dd65
