import streamlit as st
from db import manager as dbm

st.title("数据查询")


def __operate_target_columns():
    st.header("选择对象")
    st.session_state.query_operate_target = st.radio(
        "选择对象",
        ("航班", "公交", "酒店", "用户", "预订"),
        label_visibility="collapsed",
    )


def __display_columns():
    st.header("查询结果")
    target = st.session_state.query_operate_target

    if target == "航班":
        flight_num = st.text_input("航班号", key="flight_number")
        if not flight_num:
            st.error("请输入航班号")
        if st.button("查询航班"):
            flight = dbm.get_flight(flight_num)
            if flight:
                st.json(flight)
            else:
                st.error("航班不存在")

    elif target == "公交":
        location = st.text_input("地点", key="location")
        if not location:
            st.error("请输入地点")
        if st.button("查询公交"):
            bus = dbm.get_bus(location)
            if bus:
                st.json(bus)
            else:
                st.error("公交不存在")

    elif target == "酒店":
        location = st.text_input("地点", key="location")
        if not location:
            st.error("请输入地点")
        if st.button("查询酒店"):
            hotel = dbm.get_hotel(location)
            if hotel:
                st.json(hotel)
            else:
                st.error("酒店不存在")

    elif target == "用户":
        cust_id = st.text_input("用户ID", key="cust_id")
        if not cust_id:
            st.error("请输入用户ID")
        if st.button("查询用户"):
            customer = dbm.get_customer(cust_id)
            if customer:
                st.json(customer)
            else:
                st.error("用户不存在")

    elif target == "预订":
        cust_name = st.text_input("客户姓名", key="cust_name")
        if not cust_name:
            st.error("请输入客户姓名")
        if st.button("查询预订"):
            reservations = dbm.get_reservations(cust_name)
            if reservations:
                st.json(reservations)
            else:
                st.error("没有预订信息")


columns = st.columns(2)
with columns[0]:
    __operate_target_columns()
with columns[1]:
    __display_columns()
