import subprocess
subprocess.call(["docker", "run", "--name", "demoContainer", "-p", "8080:8080", "demo"])
