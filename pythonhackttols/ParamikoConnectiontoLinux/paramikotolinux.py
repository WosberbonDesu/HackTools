import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.10.10.10",username="msfadmin",password="msfadmin")
stdin, stdout, stderr = ssh.exec_command("ls")
print(stdout.read)