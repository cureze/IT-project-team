import wtforms
from wtforms.validators import Email, Length, EqualTo
from models import UserModel, EmailCaptchaModel
from exts import db


# Form: 用来验证前端提交的数据是否符合要求
class RegisterForm(wtforms.Form):
    username_register = wtforms.StringField(validators=[Length(min=3, max=20, message="用户名格式错误！")])
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message="验证码格式错误！")])
    password_register = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误！ ")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password_register", message="两次密码不一致")])

    # 自定义验证：
    # 1. 邮箱是否已经被注册
    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="该邮箱已被注册！")

    # 2. 验证码是否正确
    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email, captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError(message="邮箱或验证码错误！")
        else:
            db.session.delete(captcha_model)
            db.session.commit()


class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="用户名格式错误！")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误！ ")])


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3, max=100, message="标题格式错误！ ")])
    content = wtforms.StringField(validators=[Length(min=3, message="内容格式错误！ ")])

