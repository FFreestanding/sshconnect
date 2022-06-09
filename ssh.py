import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys()
ip=input("IP:")
port=input("PORT:")
username=input("USERNAME:")
passwd=input("PASSWD:")
ssh.connect(ip,port,username,passwd)
cd=""
while 1:
    cmd=input("$>")
    if(cmd=='q'):
        break
        ssh.close()
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cd+cmd,get_pty=True)
    content = ssh_stdout.read().decode()
    if(content!=''):
        print(content,end='')
    if "cd" in cmd:
        cd+=cmd+';'
