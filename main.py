from db.manager import get_connection
import streamlit as st


class TravelEase:
    def __init__(self):
        # 加载页面
        self.pages = st.navigation(
            [
                st.Page("pages/开始.py"),
                st.Page("pages/预订服务.py"),
                st.Page("pages/数据查询.py"),
                st.Page("pages/客户行程.py"),
                st.Page("pages/数据管理.py"),
            ]
        )

    def run(self):
        # 运行页面
        self.pages.run()


app = TravelEase()
app.run()
