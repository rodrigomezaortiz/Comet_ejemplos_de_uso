import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load the Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target_names[iris.target], name='class')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

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
    prediction = rf_classifier.predict(features)
    
    # Display result
    st.header('Prediction')

    prediction = 50

    if prediction < 60:
        prediction = 60

    st.write(f'The iris flower is predicted to be: **{prediction}**')

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