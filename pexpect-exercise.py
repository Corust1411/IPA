import pexpect

# ตั้งค่าตัวแปร
prompt = '#'
ipr1 = '172.31.112.3'
ipr2 = '172.31.112.4'
username = 'admin'
password = 'cisco'
conf = 'conf t'
interface = 'int loopback 0'
ipaddr = 'ip address'
subnet = '255.255.255.0'
subnetlb = '255.255.255.255'
lb1 = '172.16.1.1'
lb2 = '172.16.2.2'
command = 'show ip interface brief'

# เชื่อมต่อกับอุปกรณ์ R1
child = pexpect.spawn(f'telnet {ipr1}')
child.expect('Username:')
child.sendline(username)
child.expect('Password:')
child.sendline(password)
child.expect(prompt)

# เพิ่ม loopback interface
child.sendline(conf)
child.expect(prompt)
child.sendline(interface)
child.expect(prompt)
child.sendline(f'{ipaddr} {lb1} {subnetlb}')
child.expect(prompt)
child.sendline('end')
child.expect(prompt)

# ตรวจสอบการตั้งค่า
child.sendline(command)
child.expect(prompt)

# แสดงผลลัพธ์
print(child.before.decode('utf-8'))

# ออกจากระบบ
child.sendline('exit')


# เชื่อมต่อกับอุปกรณ์ R2
child = pexpect.spawn(f'telnet {ipr2}')
child.expect('Username:')
child.sendline(username)
child.expect('Password:')
child.sendline(password)
child.expect(prompt)

# เพิ่ม loopback interface
child.sendline(conf)
child.expect(prompt)
child.sendline(interface)
child.expect(prompt)
child.sendline(f'{ipaddr} {lb2} {subnetlb}')
child.expect(prompt)
child.sendline('end')
child.expect(prompt)

# ตรวจสอบการตั้งค่า
child.sendline(command)
child.expect(prompt)

# แสดงผลลัพธ์
print(child.before.decode('utf-8'))

# ออกจากระบบ
child.sendline('exit')