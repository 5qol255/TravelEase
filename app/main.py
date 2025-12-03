import streamlit as st


class TravelEase:
    def __init__(self):
        # 加载页面
        self.pages = st.navigation(
            [
                st.Page("pages/home.py", title="开始"),
                st.Page("pages/booking.py", title="预订服务"),
                st.Page("pages/query.py", title="数据查询"),
                st.Page("pages/trip.py", title="客户行程"),
                st.Page("pages/data.py", title="数据管理"),
            ]
        )

    def run(self):
        # 运行页面
        self.pages.run()


app = TravelEase()
app.run()
