#from __future__ import print_function
from Exscript.util.interact import read_login
from Exscript.protocols import SSH2

fh = open("output.txt", 'wb', 0)

account = read_login()            

#conn = SSH2()
conn = SSH2(debug=255)

#conn.buffer = 2048
#conn.set_driver('ios')
#conn.set_prompt('Hole#')
conn.set_timeout(5)

conn.connect('84.209.164.198')     

conn.login(account)

conn.execute('term len 0')
conn.execute('show running')

print >> fh, conn.response
#print(conn.response, end='', file=fh)

conn.send('exit\r')               
conn.close()

fh.close()