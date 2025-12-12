import streamlit as st

# 标题
st.markdown(
    "<h1 style='text-align: center; color: #1890ff;'>✈️🚆旅行助手 - TravelEase🚌🏨</h2>",
    unsafe_allow_html=True,
)
# 子标题
st.markdown(
    "<p style='text-align: center; color: #595959;'>一个旅行管理系统</p>",
    unsafe_allow_html=True,
)
# 分隔线
st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)

# 功能卡片（使用 columns 布局）
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📅 预订服务")
    st.write("快速预订航班、酒店或大巴，实时查看余位/房间。")

with col2:
    st.subheader("🔍 数据查询")
    st.write("查询航班时刻、酒店信息、客户资料或历史预订记录。")

with col3:
    st.subheader("🧳 行程检查")
    st.write("输入客户姓名，一键验证是否完成完整行程规划。")

st.markdown("<hr style='margin: 20px 0;'>", unsafe_allow_html=True)

# 使用说明
st.subheader("📌 使用指南")
st.markdown(
    """
- **首次使用？** 请先在「数据管理」中添加航班、酒店等基础数据。
- **预订前** 请确保客户已在系统中注册。
- **删除预订** 会自动释放资源（如增加可用座位/房间）。
- 所有操作均需点击「提交」或「查询」按钮生效。
"""
)

# 底部提示
st.markdown(
    """
    <div style='text-align: center; margin-top: 30px; color: #8c8c8c; font-size: 0.9em;'>
        © 2025 TravelEase · 旅行助手
    </div>
    """,
    unsafe_allow_html=True,
)
