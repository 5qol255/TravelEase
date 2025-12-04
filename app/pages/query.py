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


def __argument_columns():
    st.header("输入信息")
    target = st.session_state.query_operate_target

    if target == "航班":
        flight_num = st.text_input("航班号", key="flight_number")
        query_all = st.checkbox("查询全部", key="query_all_flights")
        if not flight_num and not query_all:
            st.error("请输入航班号")
        if st.button("查询航班"):
            if query_all:
                result = dbm.get_all_flights()
            else:
                result = dbm.get_flight(flight_num)
            st.session_state.query_result = result

    elif target == "公交":
        location = st.text_input("地点", key="location")
        query_all = st.checkbox("查询全部", key="query_all_buses")
        if not location and not query_all:
            st.error("请输入地点")
        if st.button("查询公交"):
            if query_all:
                result = dbm.get_all_buses()
            else:
                result = dbm.get_bus(location)
            st.session_state.query_result = result

    elif target == "酒店":
        location = st.text_input("地点", key="location")
        query_all = st.checkbox("查询全部", key="query_all_hotels")
        if not location and not query_all:
            st.error("请输入地点")
        if st.button("查询酒店"):
            if query_all:
                result = dbm.get_all_hotels()
            else:
                result = dbm.get_hotel(location)
            st.session_state.query_result = result

    elif target == "用户":
        cust_name = st.text_input("用户名", key="cust_name")
        query_all = st.checkbox("查询全部", key="query_all_customers")
        if not cust_name and not query_all:
            st.error("请输入用户名")
        if st.button("查询用户"):
            if query_all:
                result = dbm.get_all_customers()
            else:
                result = dbm.get_customer(cust_name)
            st.session_state.query_result = result

    elif target == "预订":
        cust_name = st.text_input("客户姓名", key="cust_name")
        if not cust_name:
            st.error("请输入客户姓名")
        if st.button("查询预订"):
            result = dbm.get_reservations(cust_name)
            st.session_state.query_result = result


def __display_columns():
    st.header("查询结果")
    target = st.session_state.query_operate_target
    try:
        result = st.session_state.query_result
    except:
        result = None
    if result:
        st.json(result)
    elif target == "航班":
        st.error("航班不存在")
    elif target == "公交":
        st.error("公交不存在")
    elif target == "酒店":
        st.error("酒店不存在")
    elif target == "用户":
        st.error("用户不存在")
    elif target == "预订":
        st.error("没有预订信息")


columns = st.columns(3)
with columns[0]:
    __operate_target_columns()
with columns[1]:
    __argument_columns()
with columns[2]:
    __display_columns()
