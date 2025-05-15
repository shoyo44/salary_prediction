import streamlit as st 
import matplotlib.pyplot as plt
import pandas as pd

def experience_encoder(age):
    if age == 'Less than 1 year':
        return 0.5
    if age == 'More than 50 years':
        return 50
    return float(age)



def shorten_categories(categories,cutoff):
    cat_map={}
    for i in range(len(categories)):
        if categories.values[i]>=cutoff:
            cat_map[categories.index[i]]=categories.index[i]
        else:
             cat_map[categories.index[i]]='Others'
    return cat_map

def edu_encoder(x):
    if 'Bachelor’s degree' in x:
        return "Bachelor’s degree"
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x:
        return 'Professional degree'
    return "Less than a Bachelor"

@st.cache_data
def load_data():
    df=pd.read_csv("survey_results_public.csv")
    df=df[['Employment','EdLevel','YearsCodePro','Country','ConvertedCompYearly']]
    df=df.rename({'ConvertedCompYearly':'Salary'},axis=1)
    df=df.dropna()
    df=df[df['Employment']=='Employed, full-time']
    df=df.rename({'YearsCodePro':'Experience'},axis=1)
    df=df.drop(['Employment'],axis=1)
    Country_map=shorten_categories(df.Country.value_counts(),400)
    df['Country']=df['Country'].map(Country_map)
    df['EdLevel']=df['EdLevel'].apply(edu_encoder)
    df['Experience']=df['Experience'].apply(experience_encoder)
    df=df[df['Salary']<=250000]
    df=df[df['Salary']>=20000]
    df=df[df['Country']!='Others']
    return df

df=load_data()

def show_explore_page():
    st.title("Explore Software Engineer Salaries")

    st.write(
        """
    ### Stack Overflow Developer Survey 2020
    """
    )

    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Number of Data from different countries""")

    st.pyplot(fig1)
    
    st.write(
        """
    #### Mean Salary Based On Country
    """
    )

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### Mean Salary Based On Experience
    """
    )

    data = df.groupby(["Experience"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)
    

    