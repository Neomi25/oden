# oden

Learning for AI agents

## 專案說明

一個簡單的 Flask 網站應用程式，顯示「Hello」畫面。該應用已打包成 Docker 映像以便於部署。

## 技術棧

- **框架**: Python Flask
- **容器化**: Docker

## 快速開始

### 本地運行

1. 克隆倉庫:
```bash
git clone https://github.com/Neomi25/oden.git
cd oden
```

2. 安裝依賴:
```bash
pip install -r requirements.txt
```

3. 運行應用:
```bash
python app.py
```

應用將在 `http://localhost:5000` 啟動

### 使用 Docker 運行

1. 構建映像:
```bash
docker build -t oden:latest .
```

2. 運行容器:
```bash
docker run -p 5000:5000 oden:latest
```

訪問 `http://localhost:5000` 查看應用

## 功能

- 簡單的 Flask web 伺服器
- 主頁面顯示「Hello」

## 貢獻

歡迎提交 Issues 和 Pull Requests！