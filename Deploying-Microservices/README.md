# 🎶 Deploying Songs Microservices 🎵

Welcome to the **Songs Microservice**! This is a simple microservice that provides access to a collection of songs. It's built using **Flask** and connects to a **MongoDB** database to store song information. 🚀

![Deploying the Songs microservice on RedHat OpenShift](https://github.com/Willie-Conway/Deploying-Microservices/blob/main/Screenshots/Deploying%20the%20Songs%20microservice%20on%20RedHat%20OpenShift.gif)

## 💡 Features
- 🎤 **Add songs** to the database.
- 🎧 **Retrieve all songs** from the database.
- 🎶 **Health Check** endpoint to verify the service is up and running.

## 🛠️ Technologies Used
- **Python** 🐍
- **Flask** 🐚
- **MongoDB** 🗃️
- **OpenShift** ☁️
- **GitHub** 💻

## 🎯 Learning Objectives
After completing this lab, you will be able to:
- Start **Code Engine** service in the lab environment.
- Deploy a **Flask service** to **Code Engine**.
- Access the **RedHat OpenShift** platform in the lab environment.
- Deploy a **Flask service** to **RedHat OpenShift**.

## 📦 Setup Instructions

### 1️⃣ Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/Willie-Conway/Deploying-Microservices.git
```

### 2️⃣ Install Dependencies
Navigate to the project directory and set up a virtual environment:

```bash
cd Back-End-Development-Songs
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3️⃣ Configure MongoDB
Ensure that the MongoDB service is up and running. Use the internal MongoDB URL for OpenShift or any other connection string.

Example MongoDB URL:
```
mongo.sn-labs-hirewillieco.svc.cluster.local
```

### 4️⃣ Running the Service Locally
To run the microservice locally:

```bash
python app.py
```

Visit `http://localhost:5000` to see the service in action! 🎉

### 5️⃣ Deploy to OpenShift
To deploy the microservice to OpenShift, use the following command:

```bash
oc new-app https://github.com/${GITHUB_ACCOUNT}/Back-End-Development-Songs --strategy=source --name=songs --env MONGODB_SERVICE=mongo.${OPENSHIFT_PROJECT}.svc.cluster.local --name songs
```

## 🌐 Accessing the Service

Once deployed, you can access the Songs microservice via the following URL:

```text
http://songs-sn-labs-hirewillieco.labs-prod-openshift-san-a45631dc5778dc6371c67d206ba9ae5c-0000.us-east.containers.appdomain.cloud
```

Use the `/health` endpoint to check if the service is running smoothly:

```text
http://songs-sn-labs-hirewillieco.labs-prod-openshift-san-a45631dc5778dc6371c67d206ba9ae5c-0000.us-east.containers.appdomain.cloud/health
```

It will return a response like:
```json
{
  "status": "OK"
}
```

## 📸 Screenshots

### 1️⃣ Deploying the Songs microservice on RedHat OpenShift
![Deploying Songs Service on OpenShift](https://github.com/Willie-Conway/Deploying-Microservices/blob/main/Screenshots/deploy-getsong-3.jpg)

### 2️⃣ Exposing the Service
![Exposing Songs Service](https://github.com/Willie-Conway/Deploying-Microservices/blob/main/Screenshots/deploy-getsong-4.jpg)

### 3️⃣ Health Check Endpoint Response
![Health Check](https://github.com/Willie-Conway/Deploying-Microservices/blob/main/Screenshots/deploy-getsong-5.jpg)

## 🚧 Contributing

If you'd like to contribute, feel free to open an issue or pull request. 😊

1. Fork the repo 🍴
2. Create your feature branch 🧑‍💻
3. Commit your changes ✍️
4. Push to the branch 🚀
5. Open a pull request 👥

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 📝

## 💬 Contact

For any questions or suggestions, feel free to reach out to me via:

- Email: hire.willie.conway@gmail.com 📧
- GitHub: [Willie-Conway](https://github.com/Willie-Conway) 👨‍💻

Happy coding! 🎉
