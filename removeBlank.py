## A program to remove blank spaces, 
## written by Chenghao Li, 27/01/2000


from tkinter import *  # GUI module
import time

#define:
LOG_LINE_NUM = 0


## A class for application windows
class MY_WINDOW():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    # Initialize windows
    def set_initial_window(self):
        #窗口
        self.init_window_name.title("移除空格工具_v1.0")     
        #self.init_window_name.geometry('320x160+10+10')             #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name.resizable(False, False)
        #标签
        self.init_data_label = Label(self.init_window_name, text="待处理数据")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=65, height=35) #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=65, height=49) #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=65, height=9) # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.remove_blank_button = Button(self.init_window_name, text="转换", bg="lightblue", width=10,command=self.removeblank) # 调用内部方法 加()为直接调用
        self.remove_blank_button.grid(row=1, column=11)

    #functional Function, Remove Blank
    def removeblank(self):
        #根据输入Value
        out_str = self.init_data_Text.get(1.0,END).strip().replace(" ","")
        self.result_data_Text.delete(1.0,END)
        self.result_data_Text.insert(1.0,out_str)
        self.write_log_to_Text("INFO:Operation success")

    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time

    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"   #换行
        # 删除之前的记录
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)



#Start APP
def start_my_app():
    #初始化Tk()
    myWindow = Tk()
    MYApp = MY_WINDOW(myWindow)
    # 设置根窗口默认属性
    MYApp.set_initial_window()
    #进入消息循环
    myWindow.mainloop()

start_my_app()