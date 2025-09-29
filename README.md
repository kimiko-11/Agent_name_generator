This project implements an RCNN-based object detection pipeline to identify and localize objects (airplanes in this case) in images. The workflow combines classical computer vision and deep learning techniques.
Data Preparation:

Images of airplanes along with bounding box annotations are loaded.

Positive and negative regions are extracted using Selective Search.

Feature Extraction:

Each proposed region is passed through VGG16, a pretrained convolutional neural network, to generate fixed-size feature vectors.

Classification:

A Support Vector Machine (SVM) or a custom fully connected layer classifies regions as object or background.

Bounding Box Regression (Optional):

Improves accuracy by fine-tuning predicted bounding box coordinates.

Visualization:

Detected objects are displayed with bounding boxes on images.

Key Features:

Uses pretrained deep learning models for feature extraction.

Combines computer vision techniques (Selective Search) with deep learning for object detection.

Can be extended to real-time detection using video or webcam streams.
