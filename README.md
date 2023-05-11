# Application of Virtual 3D Model AR Technology

This project combines three-dimensional modeling and programming knowledge to enable VR, AR, and related technologies. Its purpose is to combine the modeled 3D model with the [OpenSpace3D](https://www.openspace3d.com/) editor to realize intelligent interaction, allowing the user to perform corresponding operations on the model based on VR technology.

该项目通过3D建模和编程相结合，以实现VR、AR及其相关技术应用。通过3D模型与[OpenSpace3D](https://www.openspace3d.com/)编辑器实现智能交互，允许用户基于VR技术对模型进行相应操作。

You can install the software from the following address: https://www.openspace3d.com/lang/en/support/download/

## Workflow

### Monitoring and tracking

- Marker-based recognition. Displays physical markers representing virtual information on a given projection plane. The figure below shows the steps required to project a 3D object in a mark coordinate system.
<br />基于标记的识别系统。将代表虚拟信息的物理标记显示在给定的投影平面上。下图显示了在标记坐标系中投影3D对象的所需步骤。

![215047881-25abca24-b2ad-4741-87e7-db91c8adea86](https://user-images.githubusercontent.com/97808991/224477574-ec960685-531f-464b-996f-13b29fe270e3.png)

- A marker-free system based on image recognition. In this case, the marker will be any image (it's more resource intensive) to find patterns that match the reference image.
<br />基于图像识别的无标记系统。在这种情况下，标记可以是任何图像（更消耗资源），以查找与参考图像匹配的图案。

### Location based on mobile device sensors

GPS for position, compass for orientation and accelerometer for inclination. By drawing multimedia content coincident with the current location on the image seen in the mobile phone.

GPS用于定位，罗盘用于定向，加速度计用于定倾角。通过在手机中看到的图像上绘制与当前位置重合的多媒体内容。

## Python & AR

The basis of AR is to simulate the natural visual process, which is exactly what photogrammetry does. Using the principles of stereo vision in photogrammetry, our brains are able to form a three-dimensional world from two two-dimensional images given by each eye.

AR的基础是模拟自然视觉过程，这正是摄影测量技术所研究的。利用摄影测量中立体视觉的原理，我们的大脑就能够根据每只眼睛给出的两个二维图像形成一个三维世界。

In computer vision (CV), eyes are replaced by cameras that capture images from the real world. During capture, the third dimension is lost and the resulting image is stored in a two-dimensional coordinate system in pixels. Therefore, the problem is "simplified" to find the correspondence between the coordinates of a point in the "object" system (3D) and the coordinates of the same point in the "image" system (2D), from which we can know the position of the camera relative to the target system and orientation, so any 3D coordinate can be "projected" onto the image system.

在计算机视觉中，眼睛被从现实世界中捕捉图像的相机所取代。在捕获过程中，第三维度丢失，生成的图像以像素为单位存储在二维坐标系中。因此，问题就“简化”为寻找“对象”系统（3D）中点的坐标与“图像”系统（2D）中相同点坐标之间的对应关系，从中我们就能知道相机相对于目标系统的位置和方向，因此可将任何3D坐标“投影”到图像系统上。

The OpenCV library in Python can be used to learn the basics of AR applications. This is a very powerful library dedicated to computer vision that allows performing tasks such as detecting relevant features in images, camera calibration and computing correspondences between object points and image points.

Python中的OpenCV库可用来了解AR应用程序的基础知识。这是一个非常强大的专用于计算机视觉的库，它允许执行诸如检测图像中的相关特征、相机校准和计算目标点和图像点之间对应关系等任务。

Some library files for Python 2.7 are uploaded in the `liberias` folder, including matplotlib, numpy and opencv. The `scripts` folder contains some calibration, capture, detection, extraction and projection function codes for reference. 

在`liberias`文件夹中上传了一些适用于Python 2.7的库文件，包括matplotlib、numpy和opencv，`scripts`文件夹中包含了一些有关校准、捕获、检测、提取和投影的参考代码。在安装了必要的组件后，可以从以下链接安装最新的库文件。

After installing the necessary components, the latest library can be installed from: https://sourceforge.net/projects/opencvlibrary/files/

## Project Info...

In this project, the previously created 3D model (.obj) is used, and the local camera of the laptop is used to complete the human-computer interaction. Regarding the marks, a [`plantilla`](https://github.com/Rc-W024/AR-OpenSpace3D/blob/main/plantilla.pdf) template is used, allowing the model to be arranged according to the marks (model and virtual buttons) used by the application. The model mark is 8x8 cm, and the button mark is 3x3 cm.

在本项目中，使用了先前已创建好的3D模型（.obj文件），并使用笔记本电脑自带的本地摄像头完成人机交互。使用[`plantilla`](https://github.com/Rc-W024/AR-OpenSpace3D/blob/main/plantilla.pdf)模板作为标记面板，允许模型根据应用程序使用的标签（模型和虚拟按钮）进行排列。面板中模型展示标记尺寸为8x8厘米，控制按钮为3x3厘米。

## Results

### Exportation 展示模型

![image](https://user-images.githubusercontent.com/97808991/215061642-14f7c140-fa34-4f58-b495-91606b00d6c2.png)

### Hiding 隐藏模型

![image](https://user-images.githubusercontent.com/97808991/215061984-12b40011-2658-4a98-bdbf-c5d23bfa518d.png)

### Displacement 位移（模型与底座分离）

![image](https://user-images.githubusercontent.com/97808991/215062132-c397ba98-797b-4e1e-820e-faac0e996f9a.png)

### Zoom 放大模型

![image](https://user-images.githubusercontent.com/97808991/215062203-fa6c38e0-a3f5-4336-b5a0-84ca86f21a92.png)

### Rotation 模型旋转

![image](https://user-images.githubusercontent.com/97808991/215062299-baf0a216-52c4-4c26-8373-eac74536e3e7.png)

演示视频请移步：The DEMO VIDEO can be viewed in [`AR-Demo.mp4`](https://github.com/Rc-W024/AR-OpenSpace3D/blob/main/AR-Demo.mp4).
