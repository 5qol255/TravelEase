import streamlit as st
from db import manager as dbm

st.title("数据管理")


def __add_flight():
    flight_table = [
        st.text_input("航班号", key="flight_number"),
        st.number_input("价格", min_value=1, step=1, format="%d", key="price"),
        st.number_input("座位数", min_value=1, step=1, key="num_seats"),
        st.number_input("可用座位数", min_value=0, step=1, key="num_avail"),
        st.text_input("出发城市", key="from_city"),
        st.text_input("到达城市", key="ariv_city"),
    ]
    flag = True
    # 排除非法输入
    if not flight_table[0]:
        st.error("航班号不能为空")
        flag = False
    if not flight_table[4]:
        st.error("出发城市不能为空")
        flag = False
    if not flight_table[5]:
        st.error("到达城市不能为空")
        flag = False
    if flight_table[3] > flight_table[2]:
        st.error("可用座位数不能大于座位数")
        flag = False
    # 合法输入，准备提交
    if st.button("提交") and flag:
        try:
            dbm.create_flight(
                flight_table[0],
                flight_table[1],
                flight_table[2],
                flight_table[3],
                flight_table[4],
                flight_table[5],
            )
        except Exception as e:
            st.error(f"提交失败：{e}")
        else:
            st.text("提交成功！")


def __add_bus():
    bus_table = [
        st.text_input("地点", key="location"),
        st.number_input("价格", key="price", min_value=1, step=1),
        st.number_input("数量", key="num_bus", min_value=1, step=1),
        st.number_input("可用数量", key="num_avail", min_value=0, step=1),
    ]
    flag = True
    # 排除非法输入
    if not bus_table[0]:
        st.error("地点不能为空")
        flag = False
    if bus_table[1] < 1:
        st.error("价格不能小于1")
        flag = False
    if bus_table[2] < 1:
        st.error("数量不能小于1")
        flag = False
    if bus_table[3] < 1:
        st.error("可用数量不能小于1")
        flag = False
    if bus_table[3] > bus_table[2]:
        st.error("可用数量不能大于数量")
        flag = False
    # 合法输入，准备提交
    if st.button("提交") and flag:
        try:
            dbm.create_bus(
                bus_table[0],
                bus_table[1],
                bus_table[2],
                bus_table[3],
            )
        except Exception as e:
            st.error(f"提交失败：{e}")
        else:
            st.success("提交成功！")


def __add_hotel():
    hotel_table = [
        st.text_input("地点", key="location"),
        st.number_input("价格", key="price", min_value=1, step=1),
        st.number_input("房间数", key="num_rooms", min_value=1, step=1),
        st.number_input("可用房间数", key="num_avail", min_value=0, step=1),
    ]
    flag = True
    # 排除非法输入
    if not hotel_table[0]:
        st.error("地点不能为空")
        flag = False
    if hotel_table[1] < 1:
        st.error("价格不能小于1")
        flag = False
    if hotel_table[2] < 1:
        st.error("房间数不能小于1")
        flag = False
    if hotel_table[3] < 1:
        st.error("可用房间数不能小于1")
        flag = False
    if hotel_table[3] > hotel_table[2]:
        st.error("可用房间数不能大于房间数")
        flag = False
    # 合法输入，准备提交
    if st.button("提交") and flag:
        try:
            dbm.create_hotel(
                hotel_table[0],
                hotel_table[1],
                hotel_table[2],
                hotel_table[3],
            )
        except Exception as e:
            st.error(f"提交失败：{e}")
        else:
            st.success("提交成功！")


def __add_customer():
    customer_table = [
        st.text_input("用户名", key="cust_name"),
        st.text_input("用户ID", key="cust_id"),
    ]
    flag = True
    # 排除非法输入
    if not customer_table[0]:
        st.error("用户名不能为空")
        flag = False
    if not customer_table[1]:
        st.error("用户ID不能为空")
        flag = False
    # 合法输入，准备提交
    if st.button("提交") and flag:
        try:
            dbm.create_customer(
                customer_table[0],
                customer_table[1],
            )
        except Exception as e:
            st.error(f"提交失败：{e}")
        else:
            st.success("提交成功！")


def __delete_flight():
    flight_table = [
        st.text_input("航班号", key="flight_number"),
        st.number_input("价格", min_value=1, step=1, format="%d", key="price"),
        st.number_input("座位数", min_value=1, step=1, key="num_seats"),
        st.number_input("可用座位数", min_value=0, step=1, key="num_avail"),
        st.text_input("出发城市", key="from_city"),
        st.text_input("到达城市", key="ariv_city"),
    ]
    # 准备提交
    if st.button("提交"):
        try:
            dbm.delete_flight(flight_table[0])
        except Exception as e:
            st.error(f"删除失败：{e}")
        else:
            st.success("删除成功！")


def __delete_bus():
    bus_table = [
        st.text_input("地点", key="location"),
        st.number_input("价格", key="price", min_value=1, step=1),
        st.number_input("数量", key="num_bus", min_value=1, step=1),
        st.number_input("可用数量", key="num_avail", min_value=0, step=1),
    ]
    # 准备提交
    if st.button("提交"):
        try:
            dbm.delete_bus(bus_table[0])
        except Exception as e:
            st.error(f"删除失败：{e}")
        else:
            st.success("删除成功！")


def __delete_hotel():
    hotel_table = [
        st.text_input("地点", key="location"),
        st.number_input("价格", key="price", min_value=1, step=1),
        st.number_input("房间数", key="num_rooms", min_value=1, step=1),
        st.number_input("可用房间数", key="num_avail", min_value=0, step=1),
    ]
    # 准备提交
    if st.button("提交"):
        try:
            dbm.delete_hotel(hotel_table[0])
        except Exception as e:
            st.error(f"删除失败：{e}")
        else:
            st.success("删除成功！")


def __delete_customer():
    customer_table = [
        st.text_input("用户名", key="cust_name"),
        st.text_input("用户ID", key="cust_id"),
    ]
    # 准备提交
    if st.button("提交"):
        try:
            dbm.delete_customer(customer_table[1])
        except Exception as e:
            st.error(f"删除失败：{e}")
        else:
            st.success("删除成功！")


def __delete_reservation():
    del_cust_name = st.text_input("客户姓名", key="del_cust_name")

    if not del_cust_name:
        st.error("请输入客户姓名")
        return
    if st.button("查询预订"):
        st.session_state.resv_result = dbm.get_reservations(del_cust_name)
    if "resv_result" not in st.session_state:
        return
    if not st.session_state.resv_result:
        st.info("该客户无预订记录")
    else:
        st.table(st.session_state.resv_result)
        delete_target = st.number_input(
            "请输入要删除的预订编号",
            format="%d",
            min_value=0,
            step=1,
            key="reservation_id_",
        )
        if st.button("删除"):
            result = st.session_state.resv_result
            if not result:
                st.error("没有找到预订记录")
            elif delete_target >= len(result):
                st.error("输入的编号超出范围")
            else:
                try:
                    reservation_id = result[delete_target]["resvKey"]
                    resv_type = result[delete_target]["resvType"]
                    dbm.delete_reservation(reservation_id)
                    primary_key = reservation_id[: reservation_id.find("_")]
                    if resv_type == 1:
                        flight = dbm.get_flight(primary_key)
                        if flight is not None:
                            if flight["numAvail"] >= flight["numSeats"]:
                                flight["numAvail"] = flight["numSeats"] - 1
                            dbm.update_flight(
                                flight["flightNum"],
                                flight["price"],
                                flight["numSeats"],
                                flight["numAvail"] + 1,
                                flight["FromCity"],
                                flight["ArivCity"],
                            )
                    elif resv_type == 2:
                        hotel = dbm.get_hotel(primary_key)
                        if hotel is not None:
                            if hotel["numAvail"] >= hotel["numRooms"]:
                                hotel["numAvail"] = hotel["numRooms"] - 1
                            dbm.update_hotel(
                                hotel["location"],
                                hotel["price"],
                                hotel["numRooms"],
                                hotel["numAvail"] + 1,
                            )
                    elif resv_type == 3:
                        bus = dbm.get_bus(primary_key)
                        if bus is not None:
                            if bus["numAvail"] >= bus["numBus"]:
                                bus["numAvail"] = bus["numBus"] - 1
                            dbm.update_bus(
                                bus["location"],
                                bus["price"],
                                bus["numBus"],
                                bus["numAvail"] + 1,
                            )
                    else:
                        st.error("未知预订类型")
                    st.success("删除成功！")
                    st.info("请刷新页面以更新预订列表")
                    st.session_state.resv_result = dbm.get_reservations(del_cust_name)
                except Exception as e:
                    st.error(f"删除失败：{e}")


def __modify_flight():
    changes_table = [
        st.text_input("航班号", key="flight_number"),
        st.number_input("价格", min_value=1, step=1, format="%d", key="price"),
        st.number_input("座位数", min_value=1, step=1, key="num_seats"),
        st.number_input("可用座位数", min_value=0, step=1, key="num_avail"),
        st.text_input("出发城市", key="from_city"),
        st.text_input("到达城市", key="ariv_city"),
    ]
    # 准备提交
    if st.button("提交"):
        try:
            dbm.update_flight(
                changes_table[0],
                changes_table[1],
                changes_table[2],
                changes_table[3],
                changes_table[4],
                changes_table[5],
            )
        except Exception as e:
            st.error(f"修改失败：{e}")
        else:
            st.success("修改成功！")


def __modify_bus():
    bus_table = [
        st.text_input("地点", key="location"),
        st.number_input("价格", key="price", min_value=1, step=1),
        st.number_input("数量", key="num_bus", min_value=1, step=1),
        st.number_input("可用数量", key="num_avail", min_value=0, step=1),
    ]
    # 准备提交
    if st.button("提交"):
        try:
            dbm.update_bus(bus_table[0], bus_table[1], bus_table[2], bus_table[3])
        except Exception as e:
            st.error(f"修改失败：{e}")
        else:
            st.success("修改成功！")


def __modify_hotel():
    hotel_table = [
        st.text_input("地点", key="location"),
        st.number_input("价格", key="price", min_value=1, step=1),
        st.number_input("房间数", key="num_rooms", min_value=1, step=1),
        st.number_input("可用房间数", key="num_avail", min_value=0, step=1),
    ]
    # 准备提交
    if st.button("提交"):
        try:
            dbm.update_hotel(
                hotel_table[0], hotel_table[1], hotel_table[2], hotel_table[3]
            )
        except Exception as e:
            st.error(f"修改失败：{e}")
        else:
            st.success("修改成功！")


def __modify_customer():
    customer_table = [
        st.text_input("用户名", key="cust_name"),
        st.text_input("用户ID", key="cust_id"),
    ]
    name_or_id = st.radio(
        "选择修改内容", ("修改用户名", "修改用户ID"), key="name_or_id", index=0
    )
    # 准备提交
    if st.button("提交"):
        try:
            if name_or_id == "修改用户名":
                dbm.update_customer_name(customer_table[0], customer_table[1])
            else:
                dbm.update_customer_id(customer_table[0], customer_table[1])
        except Exception as e:
            st.error(f"修改失败：{e}")
        else:
            st.success("修改成功！")
            st.json(dbm.get_customer(customer_table[0]))


def __operate_options_columns():
    st.header("选择操作")
    st.session_state.operate_option = st.radio(
        "选择操作",
        ("增加", "删除", "修改"),
        label_visibility="collapsed",
    )


def __operate_target_columns():
    st.header("选择对象")
    if st.session_state.operate_option == "删除":
        targets = ("航班", "公交", "酒店", "用户", "预定")
    else:
        targets = ("航班", "公交", "酒店", "用户")
    st.session_state.operate_target = st.radio(
        "选择对象", targets, label_visibility="collapsed"
    )


def __operate_columns():
    st.header("填写数据")
    skip_tab = {
        "增加": {
            "航班": __add_flight,
            "公交": __add_bus,
            "酒店": __add_hotel,
            "用户": __add_customer,
        },
        "删除": {
            "航班": __delete_flight,
            "公交": __delete_bus,
            "酒店": __delete_hotel,
            "用户": __delete_customer,
            "预定": __delete_reservation,
        },
        "修改": {
            "航班": __modify_flight,
            "公交": __modify_bus,
            "酒店": __modify_hotel,
            "用户": __modify_customer,
        },
    }
    skip_tab[st.session_state.operate_option][st.session_state.operate_target]()


columns = st.columns(3)
with columns[0]:
    __operate_options_columns()
with columns[1]:
    __operate_target_columns()
with columns[2]:
    __operate_columns()
