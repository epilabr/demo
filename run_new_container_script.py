import subprocess
subprocess.call(["docker", "run", "-d", "--name", "demoContainer", "-p", "8080:8080", "demo"])
