# Image Classification Pipeline

## Overview
This project aims to build an image classification pipeline using SVM.

## Prerequisites
- Python 3.8 or higher

## Installation
1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Training

To train the model, run the following command:
```bash
python train.py
```
__[Optional]__
If you don't have the dataset to train, run the below command, then the above one
    
```bash
python donwload_img.py
```


## API Endpoints

To start the Fastapi server:

```bash
uvicorn app.main:app --reload
```

1. Get : `localhost:8000/`
   
    Response:
    ```json
    {"message": "Welcome to the SVM Image Classification API"}
    ```

2. Get : `localhost:8000/predict?img_path={path of the image file}`
   
    Response:
    ```json
    {"image_path": "dataset_images\cat\cat_1.jpg", "prediction": "cat", "probability": [0.17703761011165794, 0.293257644060069, 0.2627881483547557, 0.14008333744991586, 0.12683326002360162]}
    ```

## Usage
To run the Fastapi server:
```bash
curl 'localhost:8000/predict?img_path=dataset_images%5Ccat%5Ccat_1.jpg'
```
This will output the predicted class for the given image.

