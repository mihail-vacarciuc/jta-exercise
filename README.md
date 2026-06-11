# jta-exercise

# JTA - DummyJSON Dashboard

Fullstack dashboard application built with **FastAPI** (Python) and **Vue 3** (PrimeVue).  
Displays users and products analytics from [DummyJSON](https://dummyjson.com).

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI, HTTPX, Pydantic |
| Frontend | Vue 3, PrimeVue, Axios, Chart.js |

## Features

- Home dashboard with KPI cards and mini charts
- Users table with filter by role and state, multi-column sort
- Users distribution by state and university
- Products analytics — top brands, categories, price ranges, stock levels

## Prerequisites

- Python 3.10+
- Node.js 18+
- Git

## Installation and Running the app

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

Create a `.env` file inside `backend/`:
```
USERS_URL=https://dummyjson.com/users
PRODUCTS_URL=https://dummyjson.com/products
```

Create a `.env` file inside `frontend/`:
```
VITE_API_BASE_URL=http://localhost:8000
```

### 2. Docker (install and run the app)
```bash
docker-compose up --build
```

## OR

### 3. Backend (install)

```bash
cd backend
python -m venv venv
```

#### Windows
```bash
venv\Scripts\activate
```
#### Mac/Linux
```bash
source venv/bin/activate
```

then:
```bash
pip install -r requirements.txt
```

### 4. Frontend (install)
```bash
cd frontend
npm install
```

#### Running the app

Open **two terminals**:

**Terminal 1 — Backend**
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
uvicorn app.main:app --reload --port 8000
```

**Terminal 2 — Frontend**
```bash
cd frontend
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

API docs available at [http://localhost:8000/docs](http://localhost:8000/docs).
