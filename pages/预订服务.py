import streamlit as st
from db import manager as dbm

st.title("预订服务")


def __reserve_flight():
    flight_num = st.text_input("航班号", key="flight_number")
    cust_name = st.text_input("客户姓名", key="cust_name")

    if st.button("预订航班"):
        try:
            dbm.reserve_flight(cust_name, flight_num)
            st.success("预订成功！")
        except Exception as e:
            st.error(f"预订失败: {str(e)}")


def __reserve_hotel():
    location = st.text_input("酒店地点", key="location")
    cust_name = st.text_input("客户姓名", key="cust_name")

    if st.button("预订酒店"):
        try:
            dbm.reserve_hotel(cust_name, location)
            st.success("预订成功！")
        except Exception as e:
            st.error(f"预订失败: {str(e)}")


def __reserve_bus():
    location = st.text_input("大巴地点", key="location")
    cust_name = st.text_input("客户姓名", key="cust_name")

    if st.button("预订大巴"):
        try:
            dbm.reserve_bus(cust_name, location)
            st.success("预订成功！")
        except Exception as e:
            st.error(f"预订失败: {str(e)}")


reserve_type = st.radio("选择预订类型", ("航班", "酒店", "大巴"), horizontal=True)

if reserve_type == "航班":
    __reserve_flight()
elif reserve_type == "酒店":
    __reserve_hotel()
elif reserve_type == "大巴":
    __reserve_bus()
