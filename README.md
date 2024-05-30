# Glioblasted (Prototype)

## Summary
Glioblasted is a machine learning model to detect glioblastoma, a high-grade, aggressive form of brain and/or spine cancer. Glioblasted has an accuracy of 98% and is trained off of the UPENN TCIA dataset. Given is a Glioblasted prototype from earlier development (v0.1.0α).

## Abstract
This study examined how glioblastoma, a high-grade cancer originating in brain or spine cells, can be detected using machine learning with a 98% accuracy or above to fix the lack of available tools to detect glioblastoma via histological slides. Using data collected from The Cancer Imaging Archive, a Python-based Scikit-learn model was created that could detect between benign and malignant tumors of glioblastoma. However, the accuracy of the model was low. To combat this, more accurate layers were added and various numbers in the model (i.e. epochs) were modified. The majority of the procedure involved the improvement of the input image through the image processing Python module OpenCV's various functions (i.e. thresholds, contours, inverses) in order to achieve the desired accuracy. In the end, an accuracy level of 98% was achieved. The likely reasons for this are the various modifications that were made in newer prototypes. It can be concluded that this tool is a step towards improving the field of glioblastoma-related AI-assisted pathology. Theoretical and practical implications of the results were discussed.

## Details
This software was made in Python with primarily the module Scikit-learn.
> To run the software, download all files and run `main.py`.

## License
This software, as with all subsequent versions of the software, is protected by the CC-BY-NC-ND license. In summary, this does not allow commercial usage, distribution, or distribution of modifications of the software. In additon, you are required to credit authorship and state any changes you may have made.
> More information is in the file titled `LICENSE.md`.
