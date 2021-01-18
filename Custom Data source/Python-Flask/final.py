from flask import Flask, render_template, request, redirect, url_for, session
import re
from io import TextIOWrapper
import csv
import numpy as np
import pandas as pd
from collections import defaultdict
from collections import Counter
#import yaml

app = Flask(__name__,static_url_path='/static')


@app.route("/upload")
def upload():
    return render_template("loginc.html", title="home")

@app.route("/")
def index():

    return render_template('aa.html')

@app.route('/reg', methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        file = request.files['file']
        df = pd.read_csv(file)


        #list to append the column name that has the most number of words in each row
        a=[]

        #iterating the dataframe
        for i in range(0,int(len(df)/4)):
            count = df.iloc[i].str.split().str.len() #'count' stores the number of words for each column in a row.
            a.append(count[count==max(count)].index[0]) #column name with maximum 'count' is stored in list'a'.


        def most_frequent(List):
            occurence_count = Counter(List)
            return occurence_count.most_common(1)[0][0]
        z=most_frequent(a)
        return render_template('loginc.html', caption=z)

@app.route('/json', methods=['GET', 'POST'])
def json():

    return render_template('json.html')





if __name__ == "__main__":
    app.run(debug=True)
