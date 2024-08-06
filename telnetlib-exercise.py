import getpass
import telnetlib

host = "172.31.112.3"
user = input("Enter username: ")
password = getpass.getpass()

commands = '''
conf t
int g0/1
vrf forwarding control-data
ip address 192.168.1.1 255.255.255.0
no shut
exit
int g0/2
vrf forwarding control-data
ip address 192.168.2.1 255.255.255.0
no shut
exit
'''

tn = telnetlib.Telnet(host, 23, timeout=10)

tn.read_until(b"Username:")
tn.write(user.encode('ascii') + b"\n")

tn.read_until(b"Password:")
tn.write(password.encode('ascii') + b"\n")

prompt = tn.read_until(b"#").decode('ascii')
print(prompt)  # Print the prompt to verify login

for command in commands.strip().split('\n'):
    tn.write(command.encode('ascii') + b'\n')

tn.write(b"exit\n")

output = tn.read_until(b"Connection closed by foreign host").decode('ascii')
print(output.decode('ascii'))

tn.close()
