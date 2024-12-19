import re
import joblib
import gradio
import gradio as gr
import numpy as np
import pandas as pd


# Load model
trained_model = #Todo


# UI - Input componentsmodel/iris_model
#Todo


# UI - Output component
#Todo


# Label prediction function
def get_output_label(in_sepal_l, in_sepal_w, in_petal_l, in_petal_w):
    #Todo
    
    # Return result
    return ['Setosa', 'Versicolor', 'Virginica'][prediction]


# Create Gradio interface object
iface =#Todo
# Launch gradio interface
iface.launch(server_name = "0.0.0.0", server_port = 7860)
                         # set server_name = "0.0.0.0" and server_port = 7860 while launching it inside container.
                         # default server_name = "127.0.0.1", and server_port = 7860
