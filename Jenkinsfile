pipeline {
    agent any
    stages {
        stage('Example Build') {
            steps {
                println 'Hello OpenLegacy'
                withPythonEnv('/usr/bin/python3.6') {
                    sh 'python compile_script.py'
                    sh 'python package_script.py'
                    sh 'python build_image_script.py'
                    sh 'python remove_running_container_script.py'
                    sh 'python run_new_container_script.py'
                    //this is a comment
                }    
                println 'Bye'
            }
        }
    }
}
