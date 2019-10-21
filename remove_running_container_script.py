import subprocess
subprocess.call(["docker", "stop", "demoContainer"])
subprocess.call(["docker", "rm", "demoContainer"])
