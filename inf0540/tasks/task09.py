import os
import paramiko


HOSTNAME = 'ssh.students.ic.unicamp.br'
PORT = 22


if __name__ == "__main__":
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh_user = os.getenv("SSH_USER")
    ssh_pass = os.getenv("SSH_PASS")
    ssh.connect(HOSTNAME, username=ssh_user, password=ssh_pass)

    date_cmd = "date >> /tmp/eredesNNN.execucao.txt"
    stdin, stdout, stderr = ssh.exec_command(date_cmd)

    history_cmd = "history | grep -c 'date >> /tmp/eredesNNN.execucao.txt'"
    stdin, stdout, stderr = ssh.exec_command(history_cmd)
    print(stdout.readlines())
    ssh.close()
