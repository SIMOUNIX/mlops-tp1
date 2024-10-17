import joblib

def load_model():
    model = joblib.load('regression.joblib')
    return model

def model_predict(size, nb_rooms, garden):
    model = load_model()
    prediction = model.predict([[size, nb_rooms, garden]])
    return prediction[0]