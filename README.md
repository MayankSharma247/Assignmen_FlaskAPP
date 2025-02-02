# Flask Application with CI/CD

## 🚀 Technologies Used
- Flask (Python)
- Docker
- GitHub Actions

## 📌 CI/CD Pipeline:
1. **Build:** Install dependencies.
2. **Test:** Run unit tests.
3. **Containerize:** Build Docker image.
4. **Deploy:** Run container.
5. **Validate:** Ensure container is running.
6. **Cleanup:** Stop & remove container.

## 🎯 Run Locally
```bash
docker build -t my-flask-app .
docker run -p 5001:5001 my-flask-app


---

## **✅ Step 10: Push and Create a PR**
```bash
git add .
git commit -m "Added CI/CD pipeline for Flask app"
git push origin feature-yourname-assignment1

