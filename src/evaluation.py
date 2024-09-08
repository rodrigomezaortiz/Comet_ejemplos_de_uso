import joblib
import pandas as pd

def predict(features):
    """
    Usa los modelos entrenados para predecir

    Args:
        features (list): DataFrame de entrada con las columnas
            del Iris dataset.

    Returns:
        float: Predicción del modelo
    """

    # Scaled
    df = pd.DataFrame(features, columns=['sepal_length','sepal_width','petal_length','petal_width'])
    scaler = joblib.load("../model/scaler.joblib")
    x = scaler.transform(df)

    # Model
    df = pd.DataFrame(x, columns=['sepal_length','sepal_width','petal_length','petal_width'])
    model = joblib.load("../model/best_model.joblib")
    return model.predict(df)
