# Application of Virtual 3D Model AR Technology
English | [中文](README_CN.md)

This project combines three-dimensional (3D) modeling and programming knowledge to enable Virtual Reality (VR), Augmented Reality (AR), and related technologies. Its purpose is to combine the modeled 3D model with the [OpenSpace3D](https://www.openspace3d.com/) editor to realize intelligent interaction, allowing the user to perform corresponding operations on the model based on VR technology.

The software can be installed from the following address: https://www.openspace3d.com/lang/en/support/download/

## Workflow
### Monitoring and tracking
- Marker-based recognition. Displays physical markers representing virtual information on a given projection plane. The figure below shows the steps required to project a 3D object in a mark coordinate system.

![215047881-25abca24-b2ad-4741-87e7-db91c8adea86](https://user-images.githubusercontent.com/97808991/224477574-ec960685-531f-464b-996f-13b29fe270e3.png)

- A marker-free system based on image recognition. In this case, the marker will be any image (it's more resource intensive) to find patterns that match the reference image.

### Location based on mobile device sensors
GPS for position, compass for orientation and accelerometer for inclination. By drawing multimedia content coincident with the current location on the image seen in the mobile phone.

## Python & AR
The basis of AR is to simulate the natural visual process, which is exactly what photogrammetry does. Using the principles of stereo vision in photogrammetry, our brains are able to form a three-dimensional world from two two-dimensional images given by each eye.

In computer vision (CV), eyes are replaced by cameras that capture images from the real world. During capture, the third dimension is lost and the resulting image is stored in a two-dimensional coordinate system in pixels. Therefore, the problem is "simplified" to find the correspondence between the coordinates of a point in the "object" system (3D) and the coordinates of the same point in the "image" system (2D), from which we can know the position of the camera relative to the target system and orientation, so any 3D coordinate can be "projected" onto the image system.

The OpenCV library in Python can be used to learn the basics of AR applications. This is a very powerful library dedicated to computer vision that allows performing tasks such as detecting relevant features in images, camera calibration and computing correspondences between object points and image points.

Some library files for Python 2.7 are uploaded in the `liberias` folder, including matplotlib, numpy and opencv. The `scripts` folder contains some calibration, capture, detection, extraction and projection function codes for reference. 

After installing the necessary components, the latest library can be installed from: https://sourceforge.net/projects/opencvlibrary/files/

## Project Info
In this project, the previously created 3D model (.obj) is used, and the local camera of the laptop is used to complete the human-computer interaction. Regarding the marks, a [`plantilla`](https://github.com/Rc-W024/AR-OpenSpace3D/blob/main/plantilla.pdf) template is used, allowing the model to be arranged according to the marks (model and virtual buttons) used by the application. The model mark is 8x8 cm, and the button mark is 3x3 cm.

## Results
### Exportation
![image](https://user-images.githubusercontent.com/97808991/215061642-14f7c140-fa34-4f58-b495-91606b00d6c2.png)

### Hiding
![image](https://user-images.githubusercontent.com/97808991/215061984-12b40011-2658-4a98-bdbf-c5d23bfa518d.png)

### Displacement
![image](https://user-images.githubusercontent.com/97808991/215062132-c397ba98-797b-4e1e-820e-faac0e996f9a.png)

### Zoom
![image](https://user-images.githubusercontent.com/97808991/215062203-fa6c38e0-a3f5-4336-b5a0-84ca86f21a92.png)

### Rotation
![image](https://user-images.githubusercontent.com/97808991/215062299-baf0a216-52c4-4c26-8373-eac74536e3e7.png)

The DEMO VIDEO can be viewed in [`AR-Demo.mp4`](https://github.com/Rc-W024/AR-OpenSpace3D/blob/main/AR-Demo.mp4).
