import subprocess


obj = subprocess.Popen('di', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(obj.stderr.read().decode('gbk'))