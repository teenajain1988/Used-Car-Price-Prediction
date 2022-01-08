#!/usr/bin/env python
# coding: utf-8

# In[70]:

from flask import Flask,request,jsonify


# In[77]:


import util


# In[78]:


app = Flask(__name__)


# In[79]:


@app.route("/get_data_column")
def get_data_column():
    response = ({"features":util.get_feature_columns()})
    return response


# In[81]:


@app.route("/predict_price",methods=['POST'])
def predict_price():
    age = float(request.form['age'])
    kms = float(request.form['kms'])
    mlg = float(request.form['mileage'])
    eng = float(request.form['engine'])
    pwr = float(request.form['power'])
    sts = float(request.form['seats'])
    name = request.form['name']
    loc = request.form['location']
    fu_type = request.form['fuel_type']
    trans = request.form['transmission']
    owner = request.form['owner']
    price = util.predict_the_price(age,kms,mlg,eng,pwr,sts,name,loc,fu_type,trans,owner)
    response = jsonify({'Estimated Price' : price})
    return response


# In[ ]:


app.run(port = 8000)


# In[ ]:





# In[ ]:




