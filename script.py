import subprocess
a = "Hello"
print (a)
subprocess.call(["mvn", "clean", "install"], shell=True)
