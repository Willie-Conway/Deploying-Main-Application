# 🚀 Deploying Main Application

Welcome to the **Deploying Main Application** repository! This repository contains code for deploying microservices with Flask, Django, and Kubernetes.

## 🎯 Learning Objectives

- **Create a Dockerfile** to containerize Django applications 🐳
- **Use the kubectl CLI** to interact with Kubernetes clusters ⚙️
- **Work with Kubernetes deployment YAML files** 📄
- **Create a Kubernetes Deployment** on IBM Cloud Kubernetes Service (IKS) ☁️

---

## 📦 Description

This application consists of several microservices, including:
- **Songs Microservice** 🎶
- **Photos Microservice** 📸
- **Main Web Application** 🌐

The main web application allows users to sign up, log in, view concerts, and browse songs with lyrics. It connects to the **Songs** and **Photos** microservices to fetch data and display it on the web interface.

## 🔧 Technologies Used

- **Django** for the main web application 🐍
- **Flask** for the Songs microservice 🎵
- **MongoDB** for storing song data 🗃️
- **Docker** for containerization 🐳
- **Kubernetes** for orchestration ⚙️
- **IBM Cloud** for deployment ☁️

## 🛠️ Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/Willie-Conway/Deploying-Microservices.git
```

### 2. Install Dependencies

If you're setting up the project locally, first, make sure you have Python and pip installed.

Then, install the necessary dependencies:

```bash
cd Deploying-Microservices
pip install -r requirements.txt
```

### 3. Setup MongoDB

Make sure you have access to MongoDB or the `mongo` service is running in your Kubernetes cluster.

```bash
kubectl apply -f mongodb-deployment.yaml
```

### 4. Configure Environment Variables

Make sure your environment variables are set for the Songs and Photos services in the main app.

For local development, you can add these in your `.env` file:

```env
SONGS_URL=http://songs.example.com
PHOTO_URL=https://photos.example.com
```

### 5. Run the Application

Run the main application:

```bash
python manage.py runserver
```

The application should be accessible at [http://localhost:8000](http://localhost:8000).

---

## ⚡ Deployment Instructions

### Deploy to IBM Cloud using Kubernetes

To deploy your app on **IBM Cloud Kubernetes Service (IKS)**, follow the steps below:

1. Set up IBM Cloud CLI if you haven’t already:

   ```bash
   ibmcloud login
   ```

2. Create a Kubernetes cluster:

   ```bash
   ibmcloud ks cluster create --name my-cluster --zone us-south
   ```

3. Set the `KUBECONFIG` environment variable to configure kubectl:

   ```bash
   export KUBECONFIG=~/.bluemix/plugins/code-engine/my-cluster-kubeconfig.yaml
   ```

4. Deploy the microservices:

   ```bash
   kubectl apply -f deployment.yaml
   ```

5. Check if the pods are running:

   ```bash
   kubectl get pods -w
   ```

6. Forward ports to your local machine for testing:

   ```bash
   kubectl port-forward pod/songs-abc123 8080:8080
   ```

7. Visit the application on the provided URL.

---

## 💻 Usage

Once the application is running, you can:

1. **Sign Up** 📝: Register as a new user.
2. **Login** 🔑: Log into the system to access your personal concert information.
3. **View Songs** 🎵: Browse the list of songs with their lyrics.
4. **View Photos** 📸: Explore images related to the concerts.
5. **Concerts** 🎤: Check upcoming concerts and mark your attendance.

---

## 🧑‍💻 Contributing

We welcome contributions to improve this project! If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -m "Add new feature"`)
4. Push to your fork (`git push origin feature-branch`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Acknowledgements

- **IBM Cloud** for hosting the microservices ☁️
- **MongoDB** for storage solutions 🗄️
- **Django** for the backend framework 🔥
- **Flask** for the songs microservice 🎶

---

Feel free to reach out if you have any questions or issues! 😊
