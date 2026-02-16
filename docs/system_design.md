# 系統設計文件 (System Design)

本文件使用圖表輔助說明系統架構與關鍵業務流程。

## 1. 系統架構圖 (System Architecture)

系統採用前後端分離架構，前端 LIFF 崁入於 LINE App 中，後端 Flask 提供 API 服務。

```mermaid
graph TD
    User((使用者))
    subgraph LINE_Environment ["LINE 環境"]
        Bot[LINE Bot]
        LIFF[LIFF Webview / React Frontend]
    end
    
    subgraph Backend_Environment ["後端環境 (Flask)"]
        API[API Gateway / Routes]
        Auth[JWT / Auth Utils]
        DB[(Local SQL / Database)]
    end

    User -- 傳送訊息 --> Bot
    Bot -- Webhook / callback --> API
    API -- 回傳訊息 --> Bot
    Bot -- Flex Message --> User
    
    User -- 開啟連結 --> LIFF
    LIFF -- API Request --> API
    API -- Auth Verify --> Auth
    API -- Query/Save --> DB
    DB -- Data --> API
    API -- Response --> LIFF
```

## 2. 關鍵時序圖 (Sequence Diagrams)

### A. 管理員發起練習流程
當管理員在群組輸入 `/newpractice` 時的流程：

```mermaid
sequenceDiagram
    participant U as 管理員
    participant LB as LINE Bot
    participant B as 後端 (Flask)
    participant F as 前端 (LIFF)

    U->>LB: 輸入 /newpractice
    LB->>B: Webhook (MessageEvent)
    B->>B: 驗證管理員身份
    B-->>LB: 回傳 Flex Message (包含 LIFF URL)
    LB-->>U: 顯示「前往填寫」按鈕
    U->>F: 點擊按鈕開啟 LIFF
    F->>F: 載入練習表單
```

### B. 團隊建立與加入流程
使用者透過 LIFF 介面操作：

```mermaid
sequenceDiagram
    participant U as 使用者
    participant F as 前端 (LIFF)
    participant B as 後端 (API)
    participant DB as 資料庫

    U->>F: 輸入團隊名稱點擊建立
    F->>B: POST /teams/create (含 JWT)
    B->>B: 驗證權限 & 產生 ID
    B->>DB: 儲存 Team & 更新 User 角色
    DB-->>B: Success
    B-->>F: 回傳建立成功
    F-->>U: 顯示「建立成功」並導向團隊頁面
```

## 3. 資料模型設計 (Entity Relationship)

主要實體之間的關聯：

```mermaid
erDiagram
    USER ||--o| TEAM : belongs_to
    USER {
        int id
        string line_id
        string display_name
        string role "member/admin"
    }
    TEAM {
        string id
        string name
        string join_code
        datetime created_at
    }
```
