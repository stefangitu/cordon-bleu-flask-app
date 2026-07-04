pipeline {
    agent any

    stages {
        stage('Install Python') {
            steps {
                sh 'apt-get update && apt-get install -y python3 python3-pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install flask pytest pylint --break-system-packages'
            }
        }

        stage('Lint') {
            steps {
                sh 'pylint gastronomie.py app/lib/biblioteca_gastronomie.py app/tests/test_cordon_bleu.py || true'
            }
        }

        stage('Test') {
            steps {
                sh 'PYTHONPATH=$(pwd) python3 -m pytest app/tests/test_cordon_bleu.py -v'
            }
        }
    }

    post {
        success {
            echo 'Toate testele au trecut! ✅'
        }
        failure {
            echo 'Testele au esuat! ❌'
        }
    }
}
