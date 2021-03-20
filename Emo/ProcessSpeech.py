import ktrain
import tensorflow as tf
from SpeechText import open_mic


trans_table = {
    "Sadness" : b'a',
    "Joy" : b'b',
    "Fear" : b'c',
    "Neutral" : b'd',
    "Anger" : b'e'
}


# have our classifier make a prediction
def predict_emotion():
    predictor = ktrain.load_predictor('C:\\Users\\tyxia\\Documents\\Pomona\\Classes\\2nd\\s2\\electronics128\\PythonCode\\tf_model.h5')
    prediction = predictor.predict(open_mic())
    print(prediction)
    return trans_table[prediction]