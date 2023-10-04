import smtplib

# SMTP host: 1)smtp.gmail.com; 2) hotmail: smtp.live.com; 3) yahoo: smtp.mail.yahoo.com
# TLS: 传输层的安全性 Transport layer security (防止自己发的邮件被别人拦截)
# 添加 subject 可避免被当成垃圾邮件： msg=“Subject:主题\n\正文”

my_email = "xxx@gmail.com"
password = "xxx"

# create object
# connection = smtplib.SMTP("smtp.gmail.com")
try:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=password,
            to_addrs="xxx@outlook.com",
            msg="Subject:Hello\n\nThis is the body of my email.",
        )
except smtplib.SMTPException as e:
    print("An error occurred:", str(e))
# 有 with 关键词可以不用写：connection.close()
