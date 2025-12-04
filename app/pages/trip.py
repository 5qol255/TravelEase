import streamlit as st
from db import manager as dbm

st.title("客户行程")


def check_trip():
    st.header("检查客户行程")
    cust_name = st.text_input("用户名", key="trip_cust_name")
    if st.button("检查行程"):
        result = dbm.get_reservations(cust_name)
        if result:
            book_hotel = False
            book_viehicle = False
            for resv in result:
                if resv["resvType"] == 2:
                    book_hotel = True
                else:
                    book_viehicle = True
            if book_hotel and book_viehicle:
                st.success("客户已预订酒店和交通工具")
            else:
                if book_hotel:
                    st.warning("客户仅预订了酒店，未预订交通工具")
                else:
                    st.warning("客户仅预订了交通工具，未预订酒店")
        else:
            st.error("客户未预订任何行程")


check_trip()
