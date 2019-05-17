# -*- coding: utf-8 -*-
# 有点难，看不懂
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c07/p10_carry_extra_state_with_callback_functions.html


# 以下代码无意义
class CallbackBase:
    def __init__(self):
        self.__callbackMap = {}
        for k in (getattr(self, x) for x in dir(self)):
            if hasattr(k, "bind_to_event"):
                self.__callbackMap.setdefault(k.bind_to_event, []).append(k)
            elif hasattr(k, "bind_to_event_list"):
                for j in k.bind_to_event_list:
                    self.__callbackMap.setdefault(j, []).append(k)
    # staticmethod is only used to create a namespace

    @staticmethod
    def callback(event):
        def f(g, ev=event):
            g.bind_to_event = ev
            return g
        return f

    @staticmethod
    def callbacklist(eventlist):
        def f(g, evl=eventlist):
            g.bind_to_event_list = evl
            return g
        return f

    def dispatch(self, event):
        # def send_param(l, *args, **kwargs):
        #     return map(lambda x: x(*args, **kargs), l)
        l = self.__callbackMap[event]
        # f = lambda *args, **kargs: map(lambda x: x(*args, **kargs), l)
        # f = send_param(l, *args, **kwargs)
        return l


class MyClass(CallbackBase):
    # Sample
    EVENT1 = 1
    EVENT2 = 2

    @CallbackBase.callback(EVENT1)
    def handler1(self, param=None):
        print("handler1 with param: {}".format(str(param)))
        return None

    @CallbackBase.callbacklist([EVENT1, EVENT2])
    def handler2(self, param=None):
        print("handler2 with param: {}".format(str(param)))
        return None

    def run(self, event, param=None):
        self.dispatch(event)(param)

if __name__ == "__main__":
    a = MyClass()
    a.run(MyClass.EVENT1, 'mandarina')
    a.run(MyClass.EVENT2, 'naranja')
