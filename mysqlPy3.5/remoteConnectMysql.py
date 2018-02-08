import pymysql
from sshtunnel import SSHTunnelForwarder

with SSHTunnelForwarder(
         ('39.107.77.206', 22),
         ssh_username="root",
         ssh_password="Wjk123456",
         remote_bind_address=('39.107.77.206', 3306)) as server:

    conn = pymysql.connect(host='127.0.0.1',              #此处必须是是127.0.0.1
                           port=3306,
                           user='root',
                           passwd='root',
                           db='')

print ('ok')
