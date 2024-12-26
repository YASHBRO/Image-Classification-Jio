import joblib
import cv2


class ModelPredictor:
    def __init__(self, model_path: str):
        self.model = joblib.load(model_path)

    def predict(self, img_path: str):
        image = cv2.imread(img_path, cv2.IMREAD_COLOR)
        image = cv2.resize(image, (64, 64))
        image_flat = image.flatten().reshape(1, -1)
        prediction = self.model.predict(image_flat)[0]
        probability = self.model.predict_proba(image_flat)[0]
        return {
            "image_path": img_path,
            "prediction": str(prediction),
            "probability": probability.tolist(),
        }


if __name__ == "__main__":
    predictor = ModelPredictor("model\\svm_model.pkl")
    result = predictor.predict("dataset_images\\cat\\cat_1.jpg")
    print(result)
