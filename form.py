from datetime import datetime
import streamlit as st

st.title('Form for the Users')
st.write('Here, you can answer to some questions in this form.')

user_id = st.text_input('ID', value='Your ID', max_chars=5)

info = st.text_area('Share some information about you', 'Put information here',
                    help='You can write about your hobbies, job, and family')

age = st.number_input('Age', min_value=18, max_value=100, step=1)

birth_date = st.date_input('Date of birth')

smoke = st.checkbox('Do you smoke?')

drink = st.checkbox('Do you drink regularly?')

genre = st.radio('Which movie genre do you like?', options=[
                 'horror', 'adventure', 'romantic', 'drama', 'sci-fi', 'comedy', 'Thriller'])

weight = st.slider('Choose your weight', min_value=40., max_value=150., step=.5)

physical_form = st.selectbox("Select level of your physical condition", options=['Bad', 'Normal', 'Good', 'Excelent'])

colors = st.multiselect('What are your favorite color', options=['Green', 'Red', 'Blue', 'White', 'Black', 'Yellow'])

image = st.file_uploader('Upload your photo', type=['jpg', 'png'])

submit = st.button('Submit')
if submit:
    st.write('Form submitted!!!')

click = st.sidebar.button('Click me!')
if click:
    st.sidebar.write('You clicked the button')

col1, col2 = st.columns(2)

with col1:
    st.image('https://static.streamlit.io/examples/cat.jpg', width=250)
    st.button('Like Cats')

with col2:
    st.image('https://static.streamlit.io/examples/dog.jpg', width=300)
    st.button('Like Dogs')
