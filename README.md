## opencv edge detection

**NOTE**: `opencv` : 3.0.0

Methods used
- canny edge detection 
- laplace and sobel

## Setting up the Dev Env

Refer [https://github.com/prodicus/opencv3-ansible-vagrant-playbook](https://github.com/prodicus/opencv3-ansible-vagrant-playbook) for getting a working OpenCV 3.0.0 up and running on your box

## Running it

**Example run**

```bash
$ git clone https://github.com/prodicus/opencv_edge_detection 
$ cd opencv_edge_detection && workon cv
(cv) $ python canny_edge.py --image test_input/hostel_notice.jpg
```

## Canny Edge

<p align="center">
    <b>Sample input</b>
</p>

![Alt](https://github.com/prodicus/opencv_edge_detection/raw/master/test_input/win_frnds_blue.jpg)


<p align="center">
    <b>Sample output</b>
</p>

![Alt](https://github.com/prodicus/opencv_edge_detection/raw/master/test_output/canny_edge/win_frnds_blue.jpg)

## Laplace and Sobel

<p align="center">
    <b>Sample input</b>
</p>

![Alt](https://github.com/prodicus/opencv_edge_detection/raw/master/test_input/win_frnds_blue.jpg)


<p align="center">
    <b>Sample output</b>
</p>

![Alt](https://github.com/prodicus/opencv_edge_detection/raw/master/test_output/laplace_and_sobel/sobel_xy_combined.jpg)



# License

GPLv3
