
# streamlit run app.py

import streamlit as st
from PIL import Image


st.image(Image.open('images/4-star-ball.png'), width=64)
st.title("Hello World!")

# https://github.com/streamlit/30days
# with open(f'content/{j}.md', 'r') as f:
#     st.markdown(f.read())

st.write("""

My name is Nura (nurasaki) 
nurasaki-streamlit@gmail.com

Having recently completed my Applied Data Science degree at the Open University of Catalonia (February 2023), I am seeking to redirect my professional path towards a more technical role, specifically as a data scientist in the field of artificial intelligence.

With over a decade of experience in data analysis and processing, software development, and problem-solving within a publishing company specializing in the sale of books, tourist guides, and merchandising (Triangle Postals S.L), I have undertaken diverse and interdisciplinary tasks which I detail below.

I would like to highlight of my final degree thesis, where I conducted a study on detecting gender bias in natural language models (NLP) based on deep learning (BERT type model) in Catalan. This work represents the first of its kind to use these techniques on Catalan language models.

I consider myself a person with a lot of curiosity, creative in problem-solving, proficient in mathematics and analytical thinking, as well as in understanding changing business needs. Looking ahead, I envision myself as part of a collaborative team dedicated to tackling complex challenges, and where I can continue to learn and grow.

""")

# https://github.com/nurasaki-stream/streamlit_hello-world
