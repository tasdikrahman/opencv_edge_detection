## opencv edge detection

**NOTE**: `opencv` : 3.0.0

Methods used
- Canny edge detection
- Laplace and Sobel

Relevant links
- [mzucker's noteshrink](https://mzucker.github.io/2016/09/20/noteshrink.html)
- [mzucker's page-dewarping](https://mzucker.github.io/2016/08/15/page-dewarping.html)
- [Python miniconda on heroku](https://github.com/heroku-examples/python-miniconda)
- [Dewarping by Leptonica](http://www.leptonica.com/dewarping.html)
- [Science Direct article](http://www.sciencedirect.com/science/article/pii/S187705091000373X)
- [CiteseerX's article](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.81.1467)
- [Udacity CV tutorials](https://www.youtube.com/playlist?list=PLAwxTw4SYaPnbDacyrK_kB_RUkuxQBlCm)
- [Abid Rahman K's edge detection blog](http://opencvpython.blogspot.com/2012/06/image-derivatives-sobel-and-scharr.html)
- [AI-shack's Laplacian and Sobel article](http://aishack.in/tutorials/sobel-laplacian-edge-detectors/)
- [Edge-detection techniques on Stackoverflow](http://stackoverflow.com/questions/4483502/edge-detection-techniques)
- [List of CV applications](https://github.com/adius/awesome-scanning)
- [Abid Rahman K's Canny blog](https://github.com/abidrahmank/OpenCV2-Python-Tutorials/blob/master/source/py_tutorials/py_imgproc/py_canny/py_canny.rst)
- [OpenCV gradients docs](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_gradients/py_gradients.html#gradients)
- [Canny by Adrian Rosebrock on PyImageSearch](http://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/)
- [Line and Edge detection by Robin David](http://www.robindavid.fr/opencv-tutorial/chapter5-line-edge-and-contours-detection.html)
- [Edge-detection explanation docs](https://webdocs.cs.ualberta.ca/~nray1/CMPUT615_2010/Introduction/Edges.pdf)
- [CS Arizona's Image Analysis](http://vision.cs.arizona.edu/nvs/research/image_analysis/edge.html)
- [CS Arizona's Canny docs](http://vision.cs.arizona.edu/nvs/courses/ece532/cannydoc/html/index.html)
- [Austin G Walters Edge-detection explanation](http://austingwalters.com/edge-detection-in-computer-vision/)
- [Tool to extract news articles from newspaper and give the context about the news](https://github.com/vipul-sharma20/sharingan/)

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

<table>
  <tr>
    <td><img src="https://github.com/prodicus/opencv_edge_detection/raw/master/test_input/win_frnds_blue_640x480.jpg" alt="Screenshot"></td>
    <td><img src="https://github.com/prodicus/opencv_edge_detection/raw/master/test_output/canny_edge/win_frnds_blue.jpg" alt="Screenshot"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/prodicus/opencv_edge_detection/raw/master/test_input/win_frnds_dark_640x480.jpg" alt="Screenshot"></td>
    <td><img src="https://github.com/prodicus/opencv_edge_detection/raw/master/test_output/canny_edge/win_frnds_dark.jpg" alt="Screenshot"></td>
  </tr>
    <tr>
    <td><img src="https://github.com/prodicus/opencv_edge_detection/raw/master/test_input/hostel_notice_640x480.jpg" alt="Screenshot"></td>
    <td><img src="https://github.com/prodicus/opencv_edge_detection/raw/master/test_output/canny_edge/hostel_notice.jpg" alt="Screenshot"></td>
  </tr>
</table>

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
