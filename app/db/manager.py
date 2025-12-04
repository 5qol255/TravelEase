from config.dbconfig import DB_CONFIG
from pymysql import connect
from pymysql.cursors import DictCursor
from contextlib import contextmanager


@contextmanager
def get_connection():
    """提供一个安全的数据库连接上下文管理器"""
    conn = None
    try:
        conn = connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"],
            cursorclass=DictCursor,
            charset="utf8mb4",  # 建议显式指定字符集
            autocommit=False,  # 禁用自动提交
        )
        yield conn
    finally:
        if conn:
            conn.close()


def create_flight(flight_num, price, num_seats, num_avail, from_city, ariv_city):
    """创建航班记录"""
    with get_connection() as conn:
        cursor = conn.cursor()
        query = """
        INSERT INTO FLIGHTS (flightNum, price, numSeats, numAvail, FromCity, ArivCity)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(
            query, (flight_num, price, num_seats, num_avail, from_city, ariv_city)
        )
        conn.commit()


def create_bus(location, price, num_bus, num_avail):
    """创建公交记录"""
    with get_connection() as conn:
        cursor = conn.cursor()
        query = """
        INSERT INTO BUS (location, price, numBus, numAvail)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (location, price, num_bus, num_avail))
        conn.commit()


def create_hotel(location, price, num_rooms, num_avail):
    """创建酒店记录"""
    with get_connection() as conn:
        cursor = conn.cursor()
        query = """
        INSERT INTO HOTELS (location, price, numRooms, numAvail)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (location, price, num_rooms, num_avail))
        conn.commit()


def create_customer(cust_name, cust_id):
    """创建客户记录"""
    with get_connection() as conn:
        cursor = conn.cursor()
        query = """
        INSERT INTO CUSTOMERS (custName, custID)
        VALUES (%s, %s)
        """
        cursor.execute(query, (cust_name, cust_id))
        conn.commit()


def delete_flight(flight_num):
    """删除航班记录"""
    with get_connection() as conn:
        cursor = conn.cursor()
        query = "DELETE FROM FLIGHTS WHERE flightNum = %s"
        cursor.execute(query, (flight_num,))
        conn.commit()


def delete_bus(location):
    """删除公交记录"""
    with get_connection() as conn:
        cursor = conn.cursor()
        query = "DELETE FROM BUS WHERE location = %s"
        cursor.execute(query, (location,))
        conn.commit()


def delete_hotel(location):
    """删除酒店记录"""
    with get_connection() as conn:
        cursor = conn.cursor()
        query = "DELETE FROM HOTELS WHERE location = %s"
        cursor.execute(query, (location,))
        conn.commit()


def delete_customer(cust_id):
    """删除客户记录"""
    with get_connection() as conn:
        cursor = conn.cursor()
        query = "DELETE FROM CUSTOMERS WHERE custID = %s"
        cursor.execute(query, (cust_id,))
        conn.commit()


def update_flight(flight_num, price, num_seats, num_avail, from_city, ariv_city):
    """更新航班记录"""
    with get_connection() as conn:
        cursor = conn.cursor()
        query = """
        UPDATE FLIGHTS 
        SET price = %s, numSeats = %s, numAvail = %s, FromCity = %s, ArivCity = %s
        WHERE flightNum = %s
        """
        cursor.execute(
            query, (price, num_seats, num_avail, from_city, ariv_city, flight_num)
        )
        conn.commit()


def update_bus(location, price, num_bus, num_avail):
    """更新公交记录"""
    with get_connection() as conn:
        cursor = conn.cursor()
        query = """
        UPDATE BUS 
        SET price = %s, numBus = %s, numAvail = %s
        WHERE location = %s
        """
        cursor.execute(query, (price, num_bus, num_avail, location))
        conn.commit()


def update_hotel(location, price, num_rooms, num_avail):
    """更新酒店记录"""
    with get_connection() as conn:
        cursor = conn.cursor()
        query = """
        UPDATE HOTELS 
        SET price = %s, numRooms = %s, numAvail = %s
        WHERE location = %s
        """
        cursor.execute(query, (price, num_rooms, num_avail, location))
        conn.commit()


def update_customer(cust_name, cust_id):
    """更新客户记录"""
    with get_connection() as conn:
        cursor = conn.cursor()
        query = """
        UPDATE CUSTOMERS 
        SET custName = %s
        WHERE custID = %s
        """
        cursor.execute(query, (cust_name, cust_id))
        conn.commit()


def reserve_flight(cust_name, flight_num):
    """预订航班"""
    with get_connection() as conn:
        cursor = conn.cursor()

        # 检查航班是否存在
        cursor.execute(
            "SELECT numAvail FROM FLIGHTS WHERE flightNum = %s", (flight_num,)
        )
        flight = cursor.fetchone()

        if not flight:
            raise ValueError("航班不存在")

        # 检查是否有可用座位
        if flight["numAvail"] <= 0:
            raise ValueError("该航班已满员")

        # 更新航班可用座位数
        cursor.execute(
            "UPDATE FLIGHTS SET numAvail = numAvail - 1 WHERE flightNum = %s",
            (flight_num,),
        )

        # 创建预订记录
        cursor.execute(
            """
        INSERT INTO RESERVATIONS (custName, resvType, resvKey)
        VALUES (%s, 1, CONCAT(%s, '_', NOW(3)))
        """,
            (cust_name, flight_num),
        )

        conn.commit()


def reserve_hotel(cust_name, location):
    """预订酒店"""
    with get_connection() as conn:
        cursor = conn.cursor()

        # 检查酒店是否存在
        cursor.execute("SELECT numAvail FROM HOTELS WHERE location = %s", (location,))
        hotel = cursor.fetchone()

        if not hotel:
            raise ValueError("酒店不存在")

        # 检查是否有可用房间
        if hotel["numAvail"] <= 0:
            raise ValueError("该酒店已满员")

        # 更新酒店可用房间数
        cursor.execute(
            "UPDATE HOTELS SET numAvail = numAvail - 1 WHERE location = %s", (location,)
        )

        # 创建预订记录
        cursor.execute(
            """
        INSERT INTO RESERVATIONS (custName, resvType, resvKey)
        VALUES (%s, 2, CONCAT(%s, '_', NOW(3)))
        """,
            (cust_name, location),
        )

        conn.commit()


def reserve_bus(cust_name, location):
    """预订大巴"""
    with get_connection() as conn:
        cursor = conn.cursor()

        # 检查大巴是否存在
        cursor.execute("SELECT numAvail FROM BUS WHERE location = %s", (location,))
        bus = cursor.fetchone()

        if not bus:
            raise ValueError("大巴不存在")

        # 检查是否有可用座位
        if bus["numAvail"] <= 0:
            raise ValueError("该大巴已满员")

        # 更新大巴可用座位数
        cursor.execute(
            "UPDATE BUS SET numAvail = numAvail - 1 WHERE location = %s", (location,)
        )

        # 创建预订记录
        cursor.execute(
            """
        INSERT INTO RESERVATIONS (custName, resvType, resvKey)
        VALUES (%s, 3, CONCAT(%s, '_', NOW(3)))
        """,
            (cust_name, location),
        )

        conn.commit()


def get_flight(flight_num):
    """获取航班信息"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM FLIGHTS WHERE flightNum = %s", (flight_num,))
        return cursor.fetchone()


def get_all_flights():
    """获取所有航班信息"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM FLIGHTS")
        return cursor.fetchall()


def get_bus(location):
    """获取公交信息"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM BUS WHERE location = %s", (location,))
        return cursor.fetchone()


def get_all_buses():
    """获取所有公交信息"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM BUS")
        return cursor.fetchall()


def get_hotel(location):
    """获取酒店信息"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM HOTELS WHERE location = %s", (location,))
        return cursor.fetchone()


def get_all_hotels():
    """获取酒店信息"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM HOTELS")
        return cursor.fetchall()


def get_customer(cust_name):
    """获取客户信息"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CUSTOMERS WHERE custName = %s", (cust_name,))
        return cursor.fetchone()


def get_all_customers():
    """获取客户信息"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CUSTOMERS")
        return cursor.fetchall()


def get_reservations(cust_name):
    """获取客户预订信息"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT resvType, resvKey FROM RESERVATIONS WHERE custName = %s",
            (cust_name,),
        )
        return cursor.fetchall()
