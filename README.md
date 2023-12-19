# GymGuide-Machine Learning

<p align="justify"> This repository contains a collection of resources used during the capstone project for Bangkit Machine Learning. The project focuses on building machine learning models for our application. For our machine learning needs, we have built image classifier models for Gym Equipment. </p>

<p align="center">
  <img src="https://github.com/GymGuide/GymGuide-ML/assets/90093341/3cf4f9e9-e234-45b1-ba6d-8fbfc9ac37e1" width=30% height=30% >
</p>

## Architecture

<p align="justify"> The model employs Convolutional Neural Network (CNN) technology, a powerful approach in machine learning. This architecture enables the model to effectively process and recognize patterns in input data, making it well-suited for tasks such as image classification. </p>

<p align="center">
  <img src="https://github.com/GymGuide/GymGuide-ML/assets/90093341/3c08db26-082e-4c62-915b-97030be583c1" width=30% height=30% >
</p>

## Datasets

Raw Dataset :
[GymBro Computer Vision Project Dataset](https://universe.roboflow.com/rizzlabzz/gymbro)
Cleaned Dataset :
[Gym Equipment - Cleaned](https://drive.google.com/file/d/181DEbZBhq0XO3QJfPuYNRxGqnqr7oP-9/view?usp=sharing)

## Models

### Model Overview

The model architecture consists of the following layers:
- Convolutional layer with 64 filters and a ReLU activation function.
- Max pooling layer with a 2x2 pool size.
- Flatten layer to convert the 2D feature maps into a 1D feature vector.
- Dense layer with the number of units equal to the number of classes, using softmax activation.

### Data Processing

<p align="justify"> The dataset we used consists of the <b>Gym Equipment</b> model are images belonging to 23 different classes of Gym Equipment, including abdominal machine, arm curl, arm extension, back extension, back row machine, bench press, cable lat pulldown, chest fly, chest press, dip chin assist, hip abduction adduction, incline bench, lat pulldown, leg extension, leg press, lying down leg curl, overhead shoulder press, pulley machine, seated cable row, seated leg curl, smith machine, squat rack, torso rotation machine. </p>

<p align="justify"> Data augmentation techniques are applied to increase the diversity and size of the dataset. The <b>ImageDataGenerator</b> class from TensorFlow is used for rescale, rotation range, zoom range, horizontal flip, fill mode, width shift range, height shift range, shear range, channel shift range and brightness range. </p>

### Model Training

<p align="justify"> The model is then trained using the augmented dataset. <b>Gym Equipment</b> model training is performed for 10 epochs with a batch size of 8 without Callback. </p>

### Model Evaluation

<p align="justify"> The trained model is evaluated using the Test dataset. The evaluation provides the loss and accuracy scores of the model on the Test dataset. Additionally, a sample of images from the test dataset is used to demonstrate the model's predictions. The predicted class and confidence score are displayed for each image. </p>

### Model Saving and Conversion

<p align="justify"> The trained model is saved in the HDF5 format as <b>model.h5</b> for future use. To integrate the model with Android applications, the model is converted to the TensorFlow Lite (TFLite) format using the TFLite Converter. The TFLite model is saved as <b>model.tflite</b> for deployment on resource-constrained devices. </p>

<p align="justify"> In addition to the TFLite model, a metadata file <b>metadata.txt</b> is provided. The metadata file contains information about the model, such as input and output tensor names, input and output types, and model descriptions. It serves as a reference for integrating the TFLite model into applications. </p>

<p align="justify"> Also, creating an API using Flask to serve the <b>model.h5</b> file and deploying it on Google Cloud Run within the Google Cloud Platform (GCP). </p>

## Requirements

To run the notebook and utilize the model, the following dependencies are required:
- Tensorflow
- Keras
- Matplotlib
- NumPy
- PIL
- os

## Contributing

<p align="justify"> Contributions to this project are welcome. If you have any ideas, suggestions, or improvements, please submit a pull request. Make sure to follow the existing coding style and guidelines. </p>

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute the code as per the license terms.

## Contact

For any inquiries or feedback, please contact the project team.
