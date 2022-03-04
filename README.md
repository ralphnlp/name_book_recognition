## Introduction
- Template matching is an important topic in the field of Artificial Intelligence (AI) as it is one of the approaches to the basic problem of image processing which is locating the region of interest. It finds where a certain object is in the given image. It has a wide array of applications such as object detection, tracking, surveillance, medical imaging, and image stitching, etc. Reference at  <a href="https://medium.datadriveninvestor.com/template-based-versus-feature-based-template-matching-e6e77b2a3b3a">here</a>.
- The objective of this task is to use feature matching to recognize name of known books that appear in any given image. 
<p align="center">
    <img src="/source_imgs/demo.png">

## Methodology
- The first, using local feature extractor (SIFT) to extract features of known books (template images). And then, with any image is fed to the system, also is called source image, will be extracted local features by similar extractor. Finally, matching features of soucre image to features of each template image, the machine can recognize the name of any book in any given image.
- Run demo: <b>python main.py source_imgs/demo.png</b>
