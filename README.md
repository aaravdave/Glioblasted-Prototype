# Glioblasted (Prototype)

## Summary
Glioblasted is a software utilizing image classification to detect glioblastoma, a high-grade, aggressive form of brain and/or spine cancer, given images of H&E stained slides. Glioblasted has an accuracy of 98% and is trained on data from The Cancer Imaging Archive (TCIA)'s University of Pennsylvania Glioblastoma Multiforme (UPENN-GBM) dataset (Link: [UPENN-GBM](https://pathdb.cancerimagingarchive.net/eaglescope/dist/?configurl=%2Fsystem%2Ffiles%2Fcollectionmetadata%2F202401%2Fcohort_builder_01-27-2024.json&filterState=%5B%7B%22id%22%3A%22collection%22%2C%22title%22%3A%22TCIA+Collection%22%2C%22field%22%3A%22collection%22%2C%22operation%22%3A%22eq%22%2C%22values%22%3A%22UPENN-GBM%22%7D%5D). This repository hosts a prototype (v0.1.0α) for instruction on elementary image classification.

## Abstract
This study examined how glioblastoma, a high-grade cancer originating in brain or spine cells, can be detected using machine learning with a 98% accuracy or above to fix the lack of available tools to detect glioblastoma via histological slides. Using data collected from The Cancer Imaging Archive, a Python-based Scikit-learn model was created that could detect between benign and malignant tumors of glioblastoma. However, the accuracy of the model was low. To combat this, more accurate layers were added and various numbers in the model (i.e. epochs) were modified. The majority of the procedure involved the improvement of the input image through the image processing Python module OpenCV's various functions (i.e. thresholds, contours, inverses) in order to achieve the desired accuracy. In the end, an accuracy level of 98% was achieved. The likely reasons for this are the various modifications that were made in newer prototypes. It can be concluded that this tool is a step towards improving the field of glioblastoma-related AI-assisted pathology. Theoretical and practical implications of the results were discussed.

## Paper
*Coming Soon*

## Recognizations
- Best in Category, Robotics and Intelligent Machines, 2024 Georgia Science and Engineering Fair
- Nomination for the 2024 Thermo Fisher Scientific Junior Innovators Challenge, recieved through 2024 Georgia Science and Engineering Fair
- University of Georgia Mathematics Department Special Award, 2024 Georgia Science and Engineering Fair
- 1st Honors (top 10% in fair), 2024 Georgia Science and Engineering Fair
- Best in Fair, 2024 Abraham Baldwin Agricultural College Regional Science and Engineering Fiar

## Technical Specifications
This software was made in Python with primarily the module Scikit-learn.
> To run the software, download all files and run `main.py`.

## License
This software, as with all subsequent versions of the software, is protected by the CC-BY-NC-ND license. In summary, this does not allow commercial usage, distribution, or distribution of modifications of the software. In additon, you are required to credit authorship and state any changes you may have made.
> More information is in the file titled `LICENSE.md`.

## Contacts
For questions concerning the contents of this repository, please contact aaravhdave \[at] gmail \[dot] com.
