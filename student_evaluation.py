#from numpy.lib.npyio import load
import numpy as np
import streamlit as st
import pandas as pd


st.write(""" 
# Web Application 
Let's enjoy **data science** project! 
""")

st.sidebar.header('Student Input')
st.sidebar.subheader('Please enter your data:')
st.sidebar.subheader('1:strongly disagree, 2:disagree, 3:No comment, 4:agree, 5:strongly agree')


# Display widgets and store their values in variables
v_learning1 = st.sidebar.selectbox('ฉันเข้าใจได้ดีเท่าอาจารย์สอน', [1, 2, 3, 4, 5])
v_learning2 = st.sidebar.selectbox('ฉันชอบเรียนโดยการลงมือกระทำ', [1, 2, 3, 4, 5])
v_learning3 = st.sidebar.selectbox('ฉันทำงานได้ดีเมื่อทำงานร่วมกับเพื่อน', [1, 2, 3, 4, 5])
v_learning4 = st.sidebar.selectbox('ฉันเรียนได้ดีเมื่อเรียนกลุ่ม', [1, 2, 3, 4, 5])
v_learning5 = st.sidebar.selectbox('ในชั้นเรียนฉันเรียนได้ดีเมื่อทำงานกับผู้อื่น', [1, 2, 3, 4, 5])
v_learning6 = st.sidebar.selectbox('ฉันเรียนได้ดีโดยการอ่านจากสิ่งที่อาจารย์เขียนบนกระดาษ', [1, 2, 3, 4, 5])
v_learning7 = st.sidebar.selectbox('ฉันเรียนได้ดีเมื่อมีผู้บอกวิธีทำให้ฉัน', [1, 2, 3, 4, 5])
v_learning8 = st.sidebar.selectbox('เมื่อฉันได้ลงมือทำสิ่งใดก็ตามในชั้น ฉันมักทำได้ดี', [1, 2, 3, 4, 5])
v_learning9 = st.sidebar.selectbox('ฉันจำสิ่งที่ได้ยินในชั้นเรียนได้ดีกว่าสิ่งที่ฉันได้อ่าน', [1, 2, 3, 4, 5])
v_learning10 = st.sidebar.selectbox('เมื่อฉันอ่านสิ่งที่เรียนฉันจำได้ดี', [1, 2, 3, 4, 5])
v_learning11 = st.sidebar.selectbox('ฉันเรียนรู้ได้ดีเมื่อสิ่งที่เรียนต้องลงมือสร้างโครงแบบ', [1, 2, 3, 4, 5])
v_learning12 = st.sidebar.selectbox('ฉันเข้าใจได้ดีเมื่ออ่านสิ่งที่เรียน', [1, 2, 3, 4, 5])
v_learning13 = st.sidebar.selectbox('ฉันเรียนได้ดีเมื่อเรียนลำพังคนเดียว', [1, 2, 3, 4, 5])
v_learning14 = st.sidebar.selectbox('ฉันเรียนได้ดีเมื่อเรียนจากการทำโครงงาน', [1, 2, 3, 4, 5])
v_learning15 = st.sidebar.selectbox('ฉันชอบการเรียนเมื่อมีการทดลอง', [1, 2, 3, 4, 5])
v_learning16 = st.sidebar.selectbox('ฉันเรียนได้ดีเมื่ออาจารย์มอบหมายงานให้ทำ', [1, 2, 3, 4, 5])
v_learning17 = st.sidebar.selectbox('ฉันเรียนได้ดีเมื่ออาจารย์บรรยายให้ฟัง', [1, 2, 3, 4, 5])
v_learning18 = st.sidebar.selectbox('ฉันเรียนได้ดีเมื่อทำงานคนเดียว', [1, 2, 3, 4, 5])
v_learning19 = st.sidebar.selectbox('ฉันเข้าใจสิ่งที่เรียนดีเมื่อได้แสดงบทบาทสมมุติ', [1, 2, 3, 4, 5])
v_learning20 = st.sidebar.selectbox('ฉันเรียนได้ดีจากการฟังคนพูดในชั้นเรียน', [1, 2, 3, 4, 5])
v_learning21 = st.sidebar.selectbox('ฉันสนุกกับการทำงานที่ได้รับมอบหมายเมื่อทำร่วมกับเพื่อน ๆ', [1, 2, 3, 4, 5])
v_learning22 = st.sidebar.selectbox('เมื่อฉันได้สร้างสิ่งใดเรียนฉันจะเรียนสิ่งนั้นได้ดี', [1, 2, 3, 4, 5])
v_learning23 = st.sidebar.selectbox('ฉันชอบเรียนร่วมกับผู้อื่น', [1, 2, 3, 4, 5])
v_learning24 = st.sidebar.selectbox('ฉันเรียนได้ดีจากการอ่านมากกว่าจากการฟัง', [1, 2, 3, 4, 5])
v_learning25 = st.sidebar.selectbox('ฉันสนุกกับการเรียนแบบทำโครงงาน', [1, 2, 3, 4, 5])
v_learning26 = st.sidebar.selectbox('ฉันเรียนดีเมื่อได้มีส่วนร่วมในกิจกรรม', [1, 2, 3, 4, 5])
v_learning27 = st.sidebar.selectbox('ในชั้นเรียนฉันทำงานได้ดีเมื่อทำตามลำพัง', [1, 2, 3, 4, 5])
v_learning28 = st.sidebar.selectbox('ฉันชอบทำโครงงานด้วยตนเองตามลำพัง', [1, 2, 3, 4, 5])
v_learning29 = st.sidebar.selectbox('ฉันเรียนได้ดีจากการอ่านตำรามากกว่าโดยการฟังคำบรรยาย', [1, 2, 3, 4, 5])
v_learning30 = st.sidebar.selectbox('ฉันชอบทำงานด้วยตนเอง', [1, 2, 3, 4, 5])

# Store user input data in a dictionary
data = {'ฉันเข้าใจได้ดีเท่าอาจารย์สอน': v_learning1,
        'ฉันชอบเรียนโดยการลงมือกระทำ': v_learning2,
        'ฉันทำงานได้ดีเมื่อทำงานร่วมกับเพื่อน': v_learning3,
        'ฉันเรียนได้ดีเมื่อเรียนกลุ่ม': v_learning4,
        'ในชั้นเรียนฉันเรียนได้ดีเมื่อทำงานกับผู้อื่น': v_learning5,
        'ฉันเรียนได้ดีโดยการอ่านจากสิ่งที่อาจารย์เขียนบนกระดาษ': v_learning6,
        'ฉันเรียนได้ดีเมื่อมีผู้บอกวิธีทำให้ฉัน': v_learning7,
        'เมื่อฉันได้ลงมือทำสิ่งใดก็ตามในชั้น ฉันมักทำได้ดี': v_learning8,
        'ฉันจำสิ่งที่ได้ยินในชั้นเรียนได้ดีกว่าสิ่งที่ฉันได้อ่าน': v_learning9,
        'เมื่อฉันอ่านสิ่งที่เรียนฉันจำได้ดี': v_learning10,
        'ฉันเรียนรู้ได้ดีเมื่อสิ่งที่เรียนต้องลงมือสร้างโครงแบบ': v_learning11,
        'ฉันเข้าใจได้ดีเมื่ออ่านสิ่งที่เรียน': v_learning12,
        'ฉันเรียนได้ดีเมื่อเรียนลำพังคนเดียว': v_learning13,
        'ฉันเรียนได้ดีเมื่อเรียนจากการทำโครงงาน': v_learning14,
        'ฉันชอบการเรียนเมื่อมีการทดลอง': v_learning15,
        'ฉันเรียนได้ดีเมื่ออาจารย์มอบหมายงานให้ทำ': v_learning16,
        'ฉันเรียนได้ดีเมื่ออาจารย์บรรยายให้ฟัง': v_learning17,
        'ฉันเรียนได้ดีเมื่อทำงานคนเดียว': v_learning18,
        'ฉันเข้าใจสิ่งที่เรียนดีเมื่อได้แสดงบทบาทสมมุติ': v_learning19,
        'ฉันเรียนได้ดีจากการฟังคนพูดในชั้นเรียน': v_learning20,
        'ฉันสนุกกับการทำงานที่ได้รับมอบหมายเมื่อทำร่วมกับเพื่อน ๆ': v_learning21,
        'เมื่อฉันได้สร้างสิ่งใดเรียนฉันจะเรียนสิ่งนั้นได้ดี': v_learning22,
        'ฉันชอบเรียนร่วมกับผู้อื่น': v_learning23,
        'ฉันเรียนได้ดีจากการอ่านมากกว่าจากการฟัง': v_learning24,
        'ฉันสนุกกับการเรียนแบบทำโครงงาน': v_learning25,
        'ฉันเรียนดีเมื่อได้มีส่วนร่วมในกิจกรรม': v_learning26,
        'ในชั้นเรียนฉันทำงานได้ดีเมื่อทำตามลำพัง': v_learning27,
        'ฉันชอบทำโครงงานด้วยตนเองตามลำพัง': v_learning28,
        'ฉันเรียนได้ดีจากการอ่านตำรามากกว่าโดยการฟังคำบรรยาย': v_learning29,
        'ฉันชอบทำงานด้วยตนเอง': v_learning30,
}

# Create a data frame from the above dictionary
df = pd.DataFrame(data, index=[0])

# Combines user input data with sample dataset 
data_sample = pd.read_csv('Social Innovation New sample.csv')

X_new = data

#Show the X_new data frame on the screen
st.subheader('Pre Processed Input:')
st.write(X_new)

import pickle
# Reads the saved normalization model
load_nor = pickle.load(open('normalization_student.pkl', 'rb'))

#Apply the normalization model to new data
X_new = load_nor.transform(X_new)

#Show the X_new data frame on the screen 
st.subheader('Normalized Input:') 
st.write(X_new)

# Reads the saved classification model
load_knn = pickle.load(open('Best_knn_Student.pkl', 'rb'))
# Apply model for prediction
prediction = load_knn.predict(X_new)

#Show the prediction result on the screen
st.subheader('Prediction:') 
st.write(prediction)
