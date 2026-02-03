import streamlit as st
import pandas as pd
import joblib
from src.function import *
from src.processor import processor


#LOAD MODEL
model = joblib.load('model/panda.joblib')

if "df_data" not in st.session_state:
    st.session_state.df_data = None

st.title("Pandas AI")
st.caption("Manage and manipulate your dataset in narutal language (indonesian only)")

uploaded_file = st.sidebar.file_uploader("Upload file CSV", type=["csv"])
existing_dataset = st.pills("Dataset yang tersedia", ["dummy/StudentPerformance.csv"] )

if uploaded_file or existing_dataset:   
    if st.session_state.df_data is None:
        try:
            if uploaded_file:
                st.session_state.df_data = pd.read_csv(uploaded_file)
            else:
                st.session_state.df_data = pd.read_csv("data_sample/StudentPerformance.csv")
            st.success("File berhasil dibaca!")
        except Exception as e: 
            st.error(f"Gagal membaca file: {e}")

    df = st.session_state.df_data

    if st.session_state.df_data is not None:
        st.sidebar.markdown("---")
        csv_string = df.to_csv(index=False)
        csv_bytes = csv_string.encode('utf-8')
        st.sidebar.download_button(
            label="Save dataset",
            data=csv_bytes,
            file_name='dataset_baru.csv',
            mime='text/csv'
        )
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if "data" in message:
                st.write(message["data"])

    
    if prompt := st.chat_input("Apa yang bisa saya bantu?"):
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)


        response_text = ""
        output_data = None
        user_input = prompt.lower()
        processInput = processor(user_input=user_input, model=model, number=0)
        predict, number = processInput.process()
        predict = int(predict)
        number = int(number)
        

        function = {
            1: df,
            2: describe(df),
            3: info(df),
            4: dropna(df),
            5: head(df, number),  
            6: tail(df, number),
            7: selectColumn(df, number),
            8: meanColumn(df, number),
            9: medianColumn(df, number),
            10: sumColumn(df, number),
            11: checkDtype(df, number),
            12: changeType(user_input, number, df), 
            13: fillna(df, number, user_input),
            14: deleteRow(df, number),
            15: modusColumn(df, number)
        }

        response = {
            1: "Menampilkan seluruh baris",
            2: "Menampilkan deskripsi Dataset",
            3: "Menampilkan Informasi Dataset: ",
            4: "Menghapus baris berisi NULL/NaN",
            5: f"Menampilkan {number} baris awal",
            6: f"Menampilkan {number} baris terakhir",
            7: f"Menampilkan kolom dengan index ke-{number}",
            8: f"Nilai rata-rata/mean dari kolom index ke-{number} adalah: ",
            9: f"Nilai tengah/median kolom index ke-{number} adalah: ",
            10: f"Total-nilai/sum dari kolom index ke-{number} adalah: ",
            11: f"",
            12: f"",
            13: f"Mengisi data kosong: ",
            14: f"Menghapus baris index ke-{number}",
            15: f"Modus dari kolom index ke-{number}"
        }

        output_data = function[predict]
        response_text = response[predict]
        
        try:
            with st.chat_message("assistant"):
                response_text = ("".join(response_text))
                st.write(response_text)
                if output_data is not None:
                    try:
                        st.dataframe(output_data)
                    except:
                        st.write(output_data)
        except:
            st.write("Terjadi kesalahan!")

        st.session_state.messages.append({
            "role": "assistant", 
            "content": response_text, 
            "data": output_data
        })
else:
    st.info("Silakan unggah file CSV di sidebar atau pilih dataset yang disediakan untuk memulai.")