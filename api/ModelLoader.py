import joblib
import pandas as pd


class ModelLoader:
    def __init__(self, model_path: str):
        """Initialize the ModelLoader class and load the model and label encoder."""
        self.model_path = model_path
        self.model = None
        self.label_encoder = None
        self.load()

    def load(self):
        """Load the model and label encoder from the specified directory."""
        try:
            self.model = joblib.load(f'{self.model_path}/iris_model.pkl')
            self.label_encoder = joblib.load(f'{self.model_path}/label_encoder.pkl')
            print("Model loaded successfully 👏")
        except FileNotFoundError as e:
            print(f"Error loading files: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def predict(self, new_data: pd.DataFrame):
        """Make predictions on new data."""
        if self.model is None or self.label_encoder is None:
            raise ValueError("Model and label encoder need to be loaded before making predictions.")

        try:
            predictions = self.model.predict(new_data)
            predicted_classes = self.label_encoder.inverse_transform(predictions)
            return predicted_classes
        except Exception as e:
            print(f"An error occurred during prediction: {e}")
            raise
