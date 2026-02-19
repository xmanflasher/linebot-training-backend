# 系統分析文件 (System Analysis)

本文件詳述了 LineBot 練習管理系統的現有功能與系統邊界分析。

## 1. 系統邊界 (System Boundary)

系統主要由 LINE Bot 介面與 LIFF 網頁介面組成，與外部實體的互動如下：

- **使用者 (User)**：透過 LINE App 與 Bot 互動、透過 LIFF 網頁填寫表單。
- **LINE 平台 (LINE Platform)**：轉發 Webhook 事件至後端，並提供 LIFF 運行環境。
- **後端伺服器 (Backend Server)**：運行 Flask 應用程式，處理業務邏輯與資料庫存取。
- **資料庫 (Database)**：儲存使用者、團隊及練習記錄（目前主要使用 SQLAlchemy 搭配 SQLite 或 Firebase 模擬）。
- **Mock 資料層 (Mock Data)**：前端提供完整的 Mock 機制，可用於無後端環境下的開發測試。

## 2. 資料夾結構 (Directory Structure)

### 後端 (Backend) - `linebot-training-backend`
```text
/
├── app.py                # 應用程式入口點，配置路由與 CORS
├── config.py             # 環境變數與全域配置
├── requirements.txt      # Python 依賴清單
├── docs/                 # 系統文件 (本文件所在地)
├── models/               # 資料庫模型 (User, Team, Event, Database)
├── repositories/         # 資料存取層 (Repository Pattern)
├── routes/               # API 路由 (team, user, event, linebot)
├── utils/                # 工具函式 (auth, mock_data)
└── verify_*.py           # 驗證與測試腳本
```

### 前端 (Frontend) - `linebot-training-frontend`
```text
/src
├── App.jsx               # 前端入口點，配置 Provider 與 路由
├── config.js             # 前端全域配置 (API_URL, isMock)
├── components/           # 共用元件 (Toolbar, Layouts 等)
├── context/              # 全域狀態管理 (Auth, User, Team)
├── hooks/                # 自定義 React Hooks
├── mock/                 # Mock 資料集 (Profiles, Teams, Events)
├── pages/                # 分頁元件 (Practice, Team, Admin 等)
├── routes/               # 路由定義 (AppRoutes)
└── services/             # 資料存取層 (API 呼叫封裝)
```

## 3. 介面設計 (Interface Design)

### 後端 API 介面

#### System
- `POST /callback`：LINE Webhook 接收點。
- `GET /`：確認後端運行狀態。

#### Team
- `POST /api/teams/create`：建立新團隊 (需 JWT)。
- `POST /api/teams/<id>/join`：成員加入團隊 (需 JWT)。
- `GET /api/teams`：獲取所有團隊列表。
- `GET /api/teams/<id>`：獲取單一團隊資訊。
- `GET /api/teams/search`：搜尋團隊 (Query param: `inviteCode`)。

#### User
- `GET /api/users/<userId>`：獲取使用者個人資料 (含所屬團隊)。

#### Event
- `GET /api/events`：獲取活動/練習列表。
- `GET /api/events/<event_id>`：獲取活動詳情。

### 前端 LIFF 介面功能
- **練習管理**：發起新練習、查看練習清單。
- **團隊管理**：建立團隊、加入團隊、切換團隊。
- **個人資料**：查看當前 LINE Profile與角色權限。
- **管理後台**：群組管理員專屬功能介面。
