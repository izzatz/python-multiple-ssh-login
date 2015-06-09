import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    #specify the ip range
    for num in range(20,30):
        address = "192.168.1." + str(num)
        
        print "======================="
        
        ssh.connect(address, username='user', password='pass')
        print "Connected", address

        #execute simple command on each system ip
        stdin,stdout,stderr = ssh.exec_command("ls /root/Desktop")
        for line in stdout.readlines():
            print line.strip()

except paramiko.SSHException:
    print "Connection failed"
    quit()

ssh.close()
