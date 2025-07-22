
```markdown
# 🌦️ Weather API + Kubernetes Test Job

A simple FastAPI weather API with automated tests running as a Kubernetes Job.

---

## 📁 Structure

```

weather/
├── app/main.py              # FastAPI app
├── tests/test\_api.py        # Pytest test
├── Dockerfile
├── requirements.txt
└── k8s/
├── weather-api-deployment.yaml
└── test-job.yaml

````

---

## 🚀 Usage

### 1. Build & Load Docker Image
```bash
docker build -t weather-app:latest .
minikube image load weather-app:latest
````

### 2. Deploy API & Service

```bash
kubectl apply -f k8s/weather-api-deployment.yaml
```

### 3. Run Test Job

```bash
kubectl apply -f k8s/test-job.yaml
kubectl logs job/test-runner
```

---

## 🧪 Example Response

```json
{
  "city": "Tel Aviv",
  "temperature": 31.4,
  "unit": "Celsius",
  "status": "Sunny"
}
```

---

## 🛠️ Tools

* Python + FastAPI
* Pytest
* Docker
* Kubernetes (Minikube)

---

## 👤 Author

Eliram Shemesh

```

---

Let me know if you want badges, GitHub Actions, or license section added too.
```
