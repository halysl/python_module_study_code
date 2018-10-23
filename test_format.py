server=dict()
server['ip']='127.0.0.1'
ORACLE_BASE = "/opt/oracle"
dbname = 'AsdE'
db_ins_name = 'lite1'
OUTPUT_DIR = "/tmp/faq."

str1 = ("scp {ip}:{oracle_base}/diag/rdbms/{dbname}/"
"{db_ins_name}/trace/alert_{db_ins_name}.log {output_dir}/").format(
                        ip=server['ip'],
                        oracle_base=ORACLE_BASE,
                        dbname=dbname.lower(),
                        db_ins_name=db_ins_name,
                        output_dir=OUTPUT_DIR)

str2 = 'scp ' + server['ip'] + ':' + ORACLE_BASE + '/diag/rdbms/' + dbname.lower() + '/' + db_ins_name + '/trace/alert_' + db_ins_name + '.log ' + OUTPUT_DIR + '/'

print(str1)
print(str2)

print("123",
      "sad"
      "qwe",
      """123
      456
      789
      """)
