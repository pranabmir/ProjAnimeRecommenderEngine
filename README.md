# 🎬 ProjAnimeRecommenderEngine

A machine learning–based **Anime Recommendation System** that suggests anime titles based on a user’s watch history.  
It uses a neural network with user and anime embeddings to learn preferences and generate recommendations.

---

## 🚀 Features

- Recommends **10 anime titles** for a given user ID  
- Neural collaborative filtering model with embeddings  
- Model training and artifact management using **DVC**  
- Web API (Flask/FastAPI) for serving recommendations  
- Containerized with **Docker**, deployable on **Kubernetes** or **Cloud Run**  
- Configurable via YAML (`config/config.yaml`)  

---

## 📂 Repository Structure

| Path | Description |
|------|-------------|
| `src/` | Core source code for training & inference |
| `pipeline/` | ML pipeline code (data preprocessing, model training, evaluation) |
| `config/` | Configuration files (e.g., model parameters, training config) |
| `artifacts/` | Trained models & intermediate outputs (not stored in GitHub due to size) |
| `notebooks/` | Jupyter notebooks for experimentation |
| `static/`, `templates/` | Web UI assets (if running as a web app) |
| `logs/` | Log files |
| `custom_jenkins/` | Jenkins setup (custom Jenkins Dockerfile with gcloud & Docker) |
| `.dvc/` | DVC metadata for dataset & model versioning |
| `Dockerfile` | Docker image for app deployment |
| `deployment.yaml` | Kubernetes deployment manifest |
| `application.py` | Main entrypoint (API server) |
| `requirements.txt` | Python dependencies |
| `setup.py` | Python packaging info |
| `test_gcs.py` | Tests for Google Cloud Storage integration |

---

## 🧑‍💻 Model Architecture

The recommender model is a neural net with embeddings for users and anime items:

```python
user_embedding = Embedding(input_dim=n_users, output_dim=embedding_size)(user)
anime_embedding = Embedding(input_dim=n_anime, output_dim=embedding_size)(anime)

x = Dot(axes=2, normalize=True)([user_embedding, anime_embedding])
x = Flatten()(x)
x = Dense(1, kernel_initializer='he_normal')(x)
x = BatchNormalization()(x)
x = Activation("sigmoid")(x)

## Sample input: user_id
#sameple output: {
  "recommendations": [
    "Naruto",
    "One Piece",
    "Attack on Titan",
    "Bleach",
    "Death Note",
    "Fullmetal Alchemist: Brotherhood",
    "My Hero Academia",
    "Dragon Ball Z",
    "Sword Art Online",
    "Fairy Tail"
  ]
}
