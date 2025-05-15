import streamlit as st
import numpy as np
import pickle

with open ('mod.pkl','rb') as file:
     data= pickle.load(file)
reg_loaded=data['model']
le_country=data['le_country']
le_education=data['le_education']


 

def predict_pg(): 
      st.title("Software Developer Salary Prediction")
      st.write("""### We need some information to predict the salary""")
      country=('United Kingdom of Great Britain and Northern Ireland',
       'United States of America', 'France', 'Germany', 'Canada',
       'Brazil', 'Ukraine', 'Italy', 'India', 'Spain', 'Netherlands',
       'Australia')
      education=('Professional degree', 'Master’s degree', 'Less than a Bachelor',
       'Bachelor’s degree')
      country=st.selectbox("**Select Country**",country)
      education=st.selectbox("**Education Qualificaition**",education)
      experience=st.slider("**Work Experience**",0,50,3)
      ok=st.button("Calculate Salary")
      if ok:
          x=np.array([[country,education,experience]])
          x[:,0]=le_country.transform(x[:,0])
          x[:,1]=le_education.transform(x[:,1])
          x=x.astype(float)
          salary=reg_loaded.predict(x)
          st.subheader(f"The estimated salary is ${salary[0]:.2f}")



