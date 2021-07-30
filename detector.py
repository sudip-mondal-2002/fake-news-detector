import numpy as np
import os
import sys
import pickle

import tensorflow
from tensorflow.keras.layers import Embedding,LSTM,Dense,Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
import tensorflow.keras as keras

def detect(text="", DUMP="./Machine-Learning/embeddings/"):
    vectorizer_disk = pickle.load(open(os.path.join(DUMP, "vectorizer.pkl"), "rb"))
    embedding_matrix = pickle.load(open(os.path.join(DUMP, "embedding.pkl"), "rb"))

    vectorizer = TextVectorization.from_config(vectorizer_disk['config'])
    vectorizer.adapt(tensorflow.data.Dataset.from_tensor_slices(["xyz"]))
    vectorizer.set_weights(vectorizer_disk['weights'])
    
    embedding_dim = 50

    model = Sequential()
    model.add(Embedding(len(embedding_matrix), embedding_dim, keras.initializers.Constant(embedding_matrix), trainable=False))
    model.add(Dropout(0.5))
    model.add(LSTM(384))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy",optimizer="adam",metrics=["accuracy"])
    model.load_weights(DUMP)


    text = np.array(text)
    text = vectorizer([text]).numpy()
    y_preds = model.predict(text)
    return "The news is {0} % Fake!".format(int(y_preds.item()*10000)/100)


print(detect(sys.argv[1]))