# PayGrid

# 🧑‍💼 UserGrid

**PayGrid** is a lightweight, FastAPI-powered **payment microservice** designed to manage transactions, invoicing, gateway integrations, and real-time status tracking — all through a clean, RESTful API. It supports multiple payment gateways including Paystack, Flutterwave, Stripe, and PayPal, making it flexible for diverse payment scenarios. It’s containerized with Docker for secure, scalable deployments in any environment.

---

## 🚀 Features

- 💳 Seamless integration with multiple gateways (Paystack, Flutterwave, Stripe, PayPal)
- 💰 Initiate and manage one-time or recurring payments
- 🧾 Invoice generation and automatic tracking
- 🔁 Webhook support for real-time payment status updates
- 📊 APIs for checking payment status (pending, successful, failed, refunded)
- 🔐 Secure API key or JWT-based authentication
- 🧪 Interactive API docs with Swagger UI (via FastAPI)
- 🐳 Docker-ready for fast, containerized deployments

---

## 🏗️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) – high-performance Python web framework
- [Pydantic](https://pydantic-docs.helpmanual.io/) – data validation
- [SQLModel](https://sqlmodel.tiangolo.com/) – ORM for database interactions
- [JWT](https://jwt.io/) – for secure token-based authentication
- [Docker](https://www.docker.com/) – containerization

---

## 📦 Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your system
- Optionally, [Docker Compose](https://docs.docker.com/compose/) if using a `docker-compose.yml`

### 🔧 Clone the Repository

```bash
git clone https://github.com/emperorkez/PayGrid.git
cd PayGrid
```

---

### 🐳 Run with Docker
docker build -t paygrid .
docker run -d -p 8000:8000 --name paygrid paygrid

---

## 🙌 Contributing

Contributions are welcome! To get started:
Fork the repository
Create a new branch
Make your changes
Open a pull request

## 📝 License

MIT License © Emperor Kez

## 📬 Contact
