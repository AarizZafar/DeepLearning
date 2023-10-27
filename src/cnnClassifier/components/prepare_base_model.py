import os
import urllib.request as request 
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config:PrepareBaseModelConfig):
        self.config = config

    # THIS IS SAVING THE BASE MODEL THAT IS VGG16
    def get_base_model(self):
        # BELOW THIS self.model WILL BE PASSED INTO THE _prepare_full_model METHOEDc
        self.model        = tf.keras.applications.vgg16.VGG16(
            input_shape   = self.config.params_image_size,
            weights       = self.config.params_weights,
            include_top   = self.config.params_include_top
        )
        
        self.save_model(path  = self.config.base_model_path,
                        model = self.model)

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:      
            for layer in model.layers:
                model.trainable = False

        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:  # -freeze_till WILL FREEZE THE STARTING LAYERS AND NOT INCLUDE THE LAST -freeze_till layes
                model.trainable = False                # WE FREEZE THE SELECTED LAYERS MEANING THAT THEIR WEIGHTS WILL NOT BE UPDATED DURING TRAINING
        
        # IT TAKES THE 2D FEATURE MAP AND CONVERT IT INTO 1D VECTOR THE RESULT IS STORED IN A VARIABLE
        # (model.output) -> IT MEANS THAT WE WANT TO FLATTEN THE OUTPUT PRODUCED BY THE CNN
        flatten_in = tf.keras.layers.Flatten()(model.output) 

        # THIS IS THE FULLEY CONNECTED LAYER THE OUTPUT WILL BE DEPENDANT ON THE NUMBER OF OUTPUT WE HAVE (CLASSES)
        prediction = tf.keras.layers.Dense(
            units = classes,
            activation ='softmax'
        )(flatten_in)

        # THE PROVIDED CODE CREATES A NEW MODEL BY COMBINING TWO PARTS OF THE NEURAL NETWORK 
        full_model = tf.keras.models.Model(
            inputs = model.input,
            outputs = prediction
        )

        full_model.compile(
            optimizer = tf.keras.optimizers.SGD(learning_rate = learning_rate),
            loss = tf.keras.losses.CategoricalCrossentropy(),
            metrics = ['accuracy']
        )

        full_model.summary()
        return full_model

    def update_base_model(self):
        # THESE ARE THE PARAMETERS THAT WE ARE PASSING IN VGG16 IN THE ABOVE FUNCTION THAT WILL RETURN THE SUMMARY OF THE MODEL
        self.full_model    = self._prepare_full_model(
            model          = self.model,
            classes        = self.config.params_classes,
            freeze_all     = True,
            freeze_till    = None,
            learning_rate  = self.config.params_learning_rate
        )

        # AFTER WE RECEIVE THE SUMMARY OF THE MODEL WE WILL SAVE IT
        self.save_model(path  = self.config.update_base_model_path,
                        model = self.full_model)
        
    @staticmethod
    def save_model(path : Path, model: tf.keras.Model):
        print(model.summary)
        model.save(path)