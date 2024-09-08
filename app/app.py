import streamlit as st
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
    scaler = joblib.load("./model/scaler.joblib")
    x = scaler.transform(df)

    # Model
    df = pd.DataFrame(x, columns=['sepal_length','sepal_width','petal_length','petal_width'])
    model = joblib.load("./model/best_model.joblib")
    return model.predict(df)

clases = ["Setosa", "Versicolor", "Virginica"]

# Streamlit app
st.title('Iris Flower Classification')

# Input fields
st.header('Enter Iris Features')
sepal_length = st.number_input('Sepal Length (cm)', min_value=0.0, max_value=10.0, value=5.0, step=0.1)
sepal_width = st.number_input('Sepal Width (cm)', min_value=0.0, max_value=10.0, value=3.5, step=0.1)
petal_length = st.number_input('Petal Length (cm)', min_value=0.0, max_value=10.0, value=1.5, step=0.1)
petal_width = st.number_input('Petal Width (cm)', min_value=0.0, max_value=10.0, value=0.2, step=0.1)

# Prediction button
if st.button('Predict Iris Class'):
    # Make prediction
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = predict(features)

    # Display result
    st.header('Prediction')
    st.write()
    st.write(f'The iris flower is predicted to be: **{clases[int(prediction)]}**')

# Add some information about the dataset
st.sidebar.header('About')
st.sidebar.write('''
This app uses the Iris dataset to classify iris flowers into three species:
- Setosa
- Versicolor
- Virginica

The classification is based on four features:
1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

The model used is a Random Forest Classifier.
''')
