pipeline {
    agent any
    stages {
        stage('Example Build') {
            steps {
                println 'Hello OpenLegacy'
                withPythonEnv('/usr/bin/python3.6') {
                    sh 'python compile_script.py'
                }    
            }
        }
    }
}
