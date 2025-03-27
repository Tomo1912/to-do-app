# To-Do App

## Description
Built a simple **To-Do** application using **Python** and **Flask** for development.

Deployed on a **Hetzner VPS** using **Docker** and **Nginx** for deployment.

Added availability monitoring with **UptimeRobot**.

## Features

### Feature List
- **Add and Delete Tasks**: Accessible through a web interface.
- **Public Availability**: [http://strictodolist.duckdns.org](http://strictodolist.duckdns.org).
- **Monitoring with UptimeRobot**: Checks every **5 minutes**.
  - Result: **100% uptime**, average response time **273 ms**.

## Technologies

### Technology Stack
- **Backend**: **Python** with **Flask** for web requests.
- **Frontend**: **HTML** for the user interface.
- **Deployment**: **Docker** for containerization, **Nginx** as a reverse proxy.
- **Hosting**: **Hetzner Cloud VPS** (**CAX11**), Specs: **2 vCPU**, **4 GB RAM**, **40 GB** disk.
- **Monitoring**: **UptimeRobot** for uptime checks.

## Project Setup from Scratch

### 1. Local Setup of the Application

#### 1.1. Project Creation
Created a project directory and set up a virtual environment:

```bash
mkdir ToDoApp
cd ToDoApp
python3 -m venv venv
source venv/bin/activate
```

Installed Flask:

```bash
pip install flask
```

#### 1.2. Building the Application
Created **app.py**:

- Added a basic Flask application.
- Code snippet:

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to store tasks (in memory)
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append(todo)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Created a **templates** directory for storing HTML templates:

```bash
mkdir templates
```

Created **index.html** for the web interface:

```bash
nano templates/index.html
```

Content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
</head>
<body>
    <h1>To-Do List</h1>
    <form action="/add" method="post">
        <input type="text" name="todo" placeholder="Add a task" required>
        <button type="submit">Add</button>
    </form>
    <ul>
        {% for i in range(todos|length) %}
            <li>{{ todos[i] }} <a href="/delete/{{ i }}">Delete</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

### 1.3. Local Testing
Ran the application locally to test functionality:

```bash
python app.py
```

Visited [http://localhost:5000](http://localhost:5000) to confirm adding and deleting tasks worked.

### 1.4. Creating **requirements.txt**
Generated the dependency list:

```bash
pip freeze > requirements.txt
```

Content of **requirements.txt**:

```
Flask==2.0.1
```

---

## 2. Pushing to GitHub

### 2.1. Initializing Git Repository
Initialized Git and added project files:

```bash
git init
git add app.py templates/index.html requirements.txt Dockerfile
git commit -m "Initial To-Do App files"
```

### 2.2. Creating a **Dockerfile**
Created a **Dockerfile** to containerize the application:

```bash
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

Committed the Dockerfile:

```bash
git add Dockerfile
git commit -m "Add Dockerfile"
```

### 2.3. Pushing to GitHub
Pushed the project to GitHub:

```bash
git remote add origin https://github.com/Tomo1912/to-do-app.git
git branch -M main
git push -u origin main
```

---

## 3. Deployment on Hetzner VPS

### 3.1. Creating the VPS
Set up a **Hetzner CAX11** server with **Ubuntu 22.04**.

### 3.2. Connecting to the VPS
Connected via SSH:

```bash
ssh root@37.27.8.233
```

### 3.3. Installing Required Tools

```bash
apt update
apt install -y git nginx
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

### 3.4. Cloning the Repository

```bash
cd ~
git clone https://github.com/Tomo1912/to-do-app.git
cd to-do-app
```

### 3.5. Running the App with Docker

```bash
docker build -t to-do-app .
docker run -d --name to-do-app -p 5000:5000 to-do-app
docker ps
```

### 3.6. Configuring Nginx as a Reverse Proxy

```bash
nano /etc/nginx/sites-available/default
```

Config:

```nginx
server {
    listen 80;
    server_name strictodolist.duckdns.org;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Restarted Nginx:

```bash
systemctl restart nginx
```

---

## 4. Setting Up Monitoring

### 4.1. Registering with UptimeRobot
- Created an account on [uptimerobot.com](https://uptimerobot.com).
- Added a new **HTTP(s)** monitor for **strictodolist.duckdns.org**.
- Set interval to **5 minutes**.
- Enabled email notifications.
- Results: **100% uptime**, **273 ms** average response time.

---

## 5. Maintenance

### 5.1. Restarting Docker Container

```bash
docker start to-do-app
```

### 5.2. Checking Nginx Status

```bash
systemctl status nginx
```




