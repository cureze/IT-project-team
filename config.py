# 数据库配置
HOSTNAME = "127.0.0.1"
PORT = 3306
DATABASE = "zhiliaooa"
USERNAME = "root"
PASSWORD = "586084"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
MAIL_SERVER = "smtp.163.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "tianhanl0329@163.com"
MAIL_PASSWORD = "JQNMJIEPQYSXLGIM"
MAIL_DEFAULT_SENDER = "tianhanl0329@163.com"
# JQNMJIEPQYSXLGIM