# TravelEase - 旅行助手

TravelEase 是一个基于Python + Streamlit构建的轻量级旅行预订与管理系统。

---

## 功能概览

- **预订服务（Booking）**
  - 预订航班、酒店、大巴
  - 自动检查资源可用性并扣减库存

- **数据查询（Query）**
  - 查询单个或全部：航班 / 公交 / 酒店 / 用户 / 预订记录

- **客户行程检查（Trip）**
  - 输入客户姓名，自动判断是否已同时预订“酒店 + 交通工具”
  - 提供友好提示（完整行程 / 仅酒店 / 仅交通 / 无预订）

- **数据管理（Data Management）**
  - 增、删、改：航班、公交、酒店、用户信息
  - 删除预订时自动释放对应资源（如座位/房间）

---

## 配置数据库

本项目使用MySQL数据库，需要先安装MySQL并创建数据库。

运行init.sql文件，创建数据库travel_reservation。

创建app\config\dbconfig.py并向其中添加以下内容：

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "travel_reservation",
}
```

---

## 启动应用

在终端中运行以下命令：
```bash
streamlit run main.py
```

应用将在浏览器中自动打开，默认地址：http://localhost:8501