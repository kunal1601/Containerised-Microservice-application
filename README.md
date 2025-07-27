🐳 Microservices-Based Dockerized Application with PostgreSQL

This project demonstrates a containerized microservices architecture using Docker and Docker Compose. It includes two Python-based microservices—user_service and data_service—each running independently in its own container and communicating with each other via RESTful APIs. Both services interact with a shared PostgreSQL database for persistent data storage.

This setup is ideal for understanding microservices communication, container orchestration, and service isolation in a real-world environment.

📦 Features
🚀 Microservices Architecture — Modular design using independent services

🐳 Dockerized Services — Each service is containerized using Docker

📡 Inter-Service Communication — Services talk to each other via internal Docker network

🗄️ PostgreSQL Database — Shared DB with initialization SQL script

⚙️ Docker Compose — One command to spin up the entire app


📁 Project Structure
microservices-docker-app/
├── docker-compose.yml         # Orchestrates all services
├── init.sql                   # Initializes PostgreSQL schema
├── user_service/
│   ├── app.py                 # User service application logic
│   ├── Dockerfile             # Docker image setup for user_service
│   └── requirements.txt       # Python dependencies
└── data_service/
    ├── app.py                 # Data service application logic
    ├── Dockerfile             # Docker image setup for data_service
    └── requirements.txt       # Python dependencies

⚙️ How It Works
1. docker-compose.yml spins up:

  - user_service (Python + Flask)

  - data_service (Python + Flask)

  - PostgreSQL database

2. Services are built from individual Dockerfiles and run on isolated containers.

3. Flask apps interact with PostgreSQL using a database connection string defined in environment variables.

4. REST API calls are exchanged between user_service and data_service.

🛠️ Setup & Installation
📌 Prerequisites
Docker installed and running
Docker Compose installed

🔧 Steps
# Clone the repository
git clone https://github.com/kunal1601/Containerised-Microservice-application.git
cd Containerised-Microservice-application

# Build and run all containers
docker-compose up --build

✅ The services will be available on:

- user_service → http://localhost:5001

- data_service → http://localhost:5002

🧹 Tear Down
To stop and remove containers:
- docker-compose down

🚀 Future Improvements
- Add Nginx as a reverse proxy

- Integrate logging and monitoring

- Container healthchecks

- Unit testing and CI/CD pipeline 

🙋‍♂️ **Author**
------------

**Kunal Sharma**  
DevOps Engineer | Cloud Enthusiast  

🔗 [Portfolio](https://kunal-sharmaportfolio.netlify.app/)  
🐙 [GitHub](https://github.com/kunal1601)  
💼 [LinkedIn](https://www.linkedin.com/in/kunal1601/)

