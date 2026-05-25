<<<<<<< HEAD
import streamlit as st

st.title("⚙️ Jenkins CI/CD Pipeline Project")

st.markdown("---")

st.header("📌 Project Overview")

st.write("""
This project demonstrates a CI/CD pipeline using Jenkins to automate 
application build and deployment. It simulates a real-world production workflow.
""")

st.header("🎯 Problem Statement")

st.write("""
Manual deployment processes are time-consuming and error-prone.  
This project solves that by automating the build and deployment pipeline.
""")

st.header("🛠️ Tools & Technologies")

st.markdown("""
- Jenkins  
- GitHub  
- Python  
- Linux  
""")

st.header("🔄 Pipeline Workflow")

st.markdown("""
1. Developer pushes code to GitHub  
2. Jenkins detects changes (webhook/polling)  
3. Build process starts  
4. Tests are executed  
5. Application is deployed  
""")

st.header("⚙️ Sample Jenkins Pipeline Code")

st.code("""
pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/your-repo.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }
}
""", language='groovy')


st.header("💡 Key Features")

st.markdown("""
- Automated CI/CD pipeline  
- Reduced manual deployment effort  
- Faster release cycle  
- Scalable workflow  
""")

st.header("📈 Real-World Relevance")

st.write("""
This project aligns with real production environments where automation is critical.
It also complements my experience in monitoring, incident handling, and system stability.
""")

=======
import streamlit as st

st.title("⚙️ Jenkins CI/CD Pipeline Project")

st.markdown("---")

st.header("📌 Project Overview")

st.write("""
This project demonstrates a CI/CD pipeline using Jenkins to automate 
application build and deployment. It simulates a real-world production workflow.
""")

st.header("🎯 Problem Statement")

st.write("""
Manual deployment processes are time-consuming and error-prone.  
This project solves that by automating the build and deployment pipeline.
""")

st.header("🛠️ Tools & Technologies")

st.markdown("""
- Jenkins  
- GitHub  
- Python  
- Linux  
""")

st.header("🔄 Pipeline Workflow")

st.markdown("""
1. Developer pushes code to GitHub  
2. Jenkins detects changes (webhook/polling)  
3. Build process starts  
4. Tests are executed  
5. Application is deployed  
""")

st.header("⚙️ Sample Jenkins Pipeline Code")

st.code("""
pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/your-repo.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }
}
""", language='groovy')


st.header("💡 Key Features")

st.markdown("""
- Automated CI/CD pipeline  
- Reduced manual deployment effort  
- Faster release cycle  
- Scalable workflow  
""")

st.header("📈 Real-World Relevance")

st.write("""
This project aligns with real production environments where automation is critical.
It also complements my experience in monitoring, incident handling, and system stability.
""")

>>>>>>> 155c84cf7f971c2192d282a23e10e395bc11fd2c
st.success("🚀 Next Step: Add real GitHub repo + Jenkins screenshots")