import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictPipeline:
    def __init__(self,filename):
        self.filename = filename

    def predict(self):
        model = load_model(os.path.join('artifacts','training','model.h5'))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))   # WE ARE LOADING THE IMAGE AND GIVING IT A SPECIFIC SIZE
        test_image = image.img_to_array(test_image)                       # CONVERTING THE IMAGE TO A 2D ARRAY

        # THE test_image initially will be of the dimention (224,224,3), BUT AFTER APPLYING THE np.expand_dims, axis = 0
        # THE SHAPE WILL BE (1, 224, 224, 3) WHERE THE ADDED DIMENTION OF SIZE 1 CORRESPONDS TO BATCH OF IMAGES
        test_image = np.expand_dims(test_image, axis = 0)

        result = np.argmax(model.predict(test_image), axis = 1) # axis = 1, FINDING THE MAX VALUE ALONG THE COLUMN AXIS
        print(result)

        if result[0] == 1:
            predict = 'healthy'
            return [{'image ' : predict}]
        else:
            predict = 'not healthy'
            return [{'image' : predict}]