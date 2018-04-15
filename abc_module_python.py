from abc import ABCMeta,abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self,money):
        pass


class Wechatpay(Payment):
    def fuqian(self,money):
        print('微信支付了%s元'%money)

p = Wechatpay() #不调就报错了

##############这是个啥，完全看不懂~~~~~~