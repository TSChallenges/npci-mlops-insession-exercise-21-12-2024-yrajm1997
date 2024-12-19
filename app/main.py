import re
import joblib
import gradio
import gradio as gr
import numpy as np
import pandas as pd


# Load model
trained_model = joblib.load(filename = "app/model/iris_model.pkl")


# UI - Input componentsmodel/iris_model
in_sepal_l = gradio.Textbox(lines=1, placeholder=None, value="3.4", label='sepal length (cm)')
in_sepal_w = gradio.Textbox(lines=1, placeholder=None, value="4.2", label='sepal width (cm)')
in_petal_l = gradio.Textbox(lines=1, placeholder=None, value="3.6", label='petal length (cm)')
in_petal_w = gradio.Textbox(lines=1, placeholder=None, value="4.5", label='petal width (cm)')


# UI - Output component
out_label = gradio.Textbox(type="text", label='Prediction', elem_id="out_textbox")


# Label prediction function
def get_output_label(in_sepal_l, in_sepal_w, in_petal_l, in_petal_w):
        
    features = np.array([in_sepal_l, in_sepal_w, in_petal_l, in_petal_w])
    prediction = trained_model.predict(features.reshape(-1,4))[0]
    
    # Return result
    return ['Setosa', 'Versicolor', 'Virginica'][prediction]


# Create Gradio interface object
iface = gradio.Interface(fn = get_output_label,
                         inputs = [in_sepal_l, in_sepal_w, in_petal_l, in_petal_w],
                         outputs = [out_label],
                         title="Iris Flower Classification",
                         description="To classify the iris flower”",
                         flagging_mode='never'
                         )

# Launch gradio interface
iface.launch(server_name = "0.0.0.0", server_port = 7860)
                         # set server_name = "0.0.0.0" and server_port = 7860 while launching it inside container.
                         # default server_name = "127.0.0.1", and server_port = 7860