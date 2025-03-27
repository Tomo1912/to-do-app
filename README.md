# To-Do App

## Description
A simple **To-Do** application built with **Python** and **Flask**. Deployed on a **Hetzner VPS** using **Docker** and **Nginx**. Monitoring is set up with **UptimeRobot**.

## Features
- **Add/Delete Tasks** via web interface.
- Publicly available at: [http://37.27.8.233](http://37.27.8.233).
- **Uptime** monitored by **UptimeRobot**: **100% uptime** with an average response time of **273 ms**.

## Technologies
- **Backend**: Python, Flask.
- **Frontend**: HTML.
- **Deployment**: Docker, Nginx.
- **Hosting**: Hetzner Cloud VPS (CAX11: 2 vCPU, 4 GB RAM, 40 GB disk).
- **Monitoring**: UptimeRobot.

## Project Setup

### 1. Local Setup
- Create and activate virtual environment:
    ```bash
    mkdir ToDoApp
    cd ToDoApp
    python3 -m venv venv
    source venv/bin/activate
    ```
- Install Flask:
    ```bash
    pip install flask
    ```

### 2. GitHub Setup
- Initialize Git, add files:
    ```bash
    git init
    git add app.py templates/index.html requirements.txt
    git commit -m "Initial commit"
    ```
- Push to GitHub.

### 3. Deployment on Hetzner VPS
- Create VPS on Hetzner with Ubuntu 22.04.
- SSH into VPS:
    ```bash
    ssh root@37.27.8.233
    ```
- Install required tools:
    ```bash
    apt update
    apt install -y git docker nginx
    ```
- Clone the repo and build Docker image:
    ```bash
    git clone https://github.com/Tomo1912/to-do-app.git
    cd to-do-app
    docker build -t to-do-app .
    docker run -d --name to-do-app -p 5000:5000 to-do-app
    ```
- Configure Nginx as reverse proxy:
    ```nginx
    server {
        listen 80;
        server_name 37.27.8.233;
        location / {
            proxy_pass http://localhost:5000;
        }
    }
    ```
    Restart Nginx:
    ```bash
    systemctl restart nginx
    ```

### 4. Monitoring
- Set up **UptimeRobot** for HTTP monitoring every **5 minutes**.
- Monitor result: **100% uptime**, average response time: **273 ms**.

### 5. Maintenance
- Restart Docker container if needed:
    ```bash
    docker start to-do-app
    ```



