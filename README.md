# MLOps Project - Vehicle Data Pipeline

## 🚀 Project Overview
This project demonstrates the implementation of an end-to-end MLOps pipeline for managing, processing, and deploying machine learning models. It highlights the use of modern tools, technologies, and best practices to create a robust and scalable system. The goal is to impress recruiters and visitors by showcasing a seamless integration of multiple components into a cohesive workflow.

---

## 📁 Project Structure
- **template.py**: Script to create the initial project template.
- **setup.py & pyproject.toml**: Files for packaging and dependencies (refer to `crashcourse.txt` for details).
- **requirements.txt**: Dependencies required for the project.
- **notebook/**: Contains Jupyter notebooks for EDA, feature engineering, and MongoDB integration.
- **src/**: Source code for configurations, data ingestion, validation, transformation, and model training.
- **static/** & **templates/**: Directories for the web application.

---

## ⚙️ Setup Instructions

### Step 1: Virtual Environment Setup
1. Create and activate a virtual environment:
   ```bash
   conda create -n vehicle python=3.10 -y
   conda activate vehicle
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Verify installation:
   ```bash
   pip list
   ```

### Step 2: MongoDB Atlas Setup
1. Sign up and create a new project on [MongoDB Atlas](https://www.mongodb.com/atlas/database).
2. Create a cluster with the **M0** service tier.
3. Set up a database user with username and password.
4. Configure network access by adding IP address `0.0.0.0/0`.
5. Obtain the connection string and replace `<password>` with your password.
6. Push dataset to MongoDB using the notebook `notebook/mongoDB_demo.ipynb`.
7. Verify data in MongoDB Atlas under **Database > Browse Collections**.

---

## 🛠️ Logging, Exception Handling, and Notebooks
- **Logger and Exception Files**: Implemented and tested using `demo.py`.
- **EDA and Feature Engineering**: Conducted in the notebook folder.

---

## 📥 Data Ingestion
1. Declare constants in `constants.__init__.py`.
2. Set up MongoDB connection in `configuration.mongo_db_connections.py`.
3. Implement data fetching and transformation in `data_access/proj1_data.py`.
4. Define configuration and artifact entities in `entity/config_entity.py` and `entity/artifact_entity.py`.
5. Integrate data ingestion in `components/data_ingestion.py`.
6. Run the pipeline using `demo.py`.

To set MongoDB URL as an environment variable:
```bash
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net/..."
```

---

## 📊 Data Validation, Transformation, and Model Training
1. Add dataset schema in `config.schema.yaml` for validation.
2. Implement components:
   - **Data Validation**: Ensures dataset integrity.
   - **Data Transformation**: Prepares data for modeling.
   - **Model Trainer**: Builds and evaluates machine learning models.
3. Extend `utils.main_utils.py` and `entity/estimator.py` as needed.

---

## ☁️ AWS Integration
1. Set up AWS credentials and S3 bucket:
   - **IAM User**: Create a new user with `AdministratorAccess`.
   - **Environment Variables**:
     ```bash
     export AWS_ACCESS_KEY_ID="<your-access-key>"
     export AWS_SECRET_ACCESS_KEY="<your-secret-key>"
     ```
   - **S3 Bucket**: Create a bucket named `my-model-mlopsproj`.
2. Implement AWS S3 integration in `src.aws_storage` and `entity/s3_estimator.py`.
3. Set model evaluation thresholds in `constants.__init__.py`.

---

## 📈 Model Evaluation and Deployment
1. Develop **Model Evaluation** and **Model Pusher** components.
2. Set up **Prediction Pipeline** and `app.py` for API services.
3. Deploy the application using Docker and CI/CD pipelines.

---

## 🔄 CI/CD Pipeline Setup
1. Create `Dockerfile` and `.dockerignore`.
2. Configure GitHub Actions workflows in `.github/workflows/aws.yaml`.
3. Create an ECR repository on AWS and link it to the project.
4. Deploy a self-hosted GitHub runner on an EC2 instance:
   - Launch an Ubuntu EC2 instance.
   - Install Docker and GitHub Runner.
5. Add secrets in GitHub:
   - `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION`, `ECR_REPO`.

---

## 🌐 Deployment
1. Expose EC2 instance port `5080` for application access.
2. Access the web app via `http://<public-ip>:5080`.
3. Perform model training using `/training` route.

---

## 🤝 Collaboration and Feedback
Feel free to raise issues or contribute to this project by creating pull requests. Your feedback is highly valued!

---

## 📌 Key Features
- **MongoDB Integration**: Seamless database operations.
- **AWS Services**: Secure cloud storage and CI/CD pipeline.
- **Dockerized Deployment**: Efficient containerization for scalability.
- **Data Validation & Transformation**: Robust preprocessing workflows.
- **Model Training & Evaluation**: Automated pipeline for ML tasks.

---

## 📚 References
- [MongoDB Atlas Documentation](https://www.mongodb.com/docs/atlas/)
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/index.html)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Docker](https://docs.docker.com/)

