import os
from flask import Flask, render_template, url_for, request, redirect, send_from_directory
import tensorflow as tf
from caption1 import *
import warnings
warnings.filterwarnings("ignore")

global graph

graph = tf.get_default_graph()

app = Flask(__name__ , template_folder="templates")


@app.route('/')
def hello():
    return render_template('upload.html')

@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/', methods = ['GET','POST'])
def upload_file():
    try:
        os.system("find static/ -name "*jpg" -mmin +5 -delete")
    except OSError:
        pass
    if request.method == 'POST':
        img = request.files['image']
        img.save("static/"+ img.filename)
        with graph.as_default():
            caption = caption_this_image("static/"+ img.filename)
        
        result_dic = {'image' : "static/" + img.filename,
			'description' : caption}
        return render_template('success.html', results = result_dic)
    return render_template('upload.html')
    #return render_template('index.html', results = result_dic)



if __name__ == '__main__':
	app.run(debug = True)
