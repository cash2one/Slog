#关于tornado用户验证:
class LoginHandler(BaseHandler):
	def post(self):
		if password == user['password']
			self.set_secure_cookie('erp_ktvsky_com',str(username),expire_days=1)
			#self._login(username)

@web.authenticatied
class WorkHandler(BaseHandler)：
	'''
	'''

@web.authenticatied装饰器会调用self.current_user
这是一个属性也是一个方法：
调用get_current_user()
def get_current_user(self):
	username = self.get_secure_cookie("erp_ktvsky_com")
	if not username:
		self._logout()
	return username.decode()
从此以后，username = self.current_user(self)
#-----------

#关于一次调用接口的实例：
gen.coroutine()#异步
def post(self):
	try:
		pay_id = self.get_argument("pay_id")
		openid = self.get_arguemnt("openid")
	except:
		raise ParamError(errocode=10000)
	url = ""
	logging.error(url)
	http_client = utils.get_async_client()
	request = httpclient.HTTPRequest(url,method = 'GET',headers={})
	res = yield http_client.fetch(request)
	if：
		self.write(res)
	else:
		self.write(res)
#----------

#