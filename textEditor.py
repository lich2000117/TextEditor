## A program as a text Editor, 
## written by Chenghao Li, 27/01/2000
## Functions:
##      1. Remove Blank Spaces
##      2. Replace Text
##      3. Currency Convert


from tkinter import *  # GUI module
import time

#define:
LOG_LINE_NUM = 0


## A class for application windows
class MY_WINDOW():
    def __init__(self,init_window_name):
        self.flag = 0  # flag to check if a button has been pressed several times.
        self.init_window_name = init_window_name


    # Initialize windows
    def set_initial_window(self):
        #window
        self.init_window_name.title("Text Process Tool  -- by Chenghao Li")     
        #self.init_window_name.geometry('320x160+10+10')             #290 160 is the window size ;  +10 +10 define window appear location
        self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name.resizable(False, False)
        #label
        self.init_data_label = Label(self.init_window_name, text="Input")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="Output")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="Log")
        self.log_label.grid(row=12, column=0)
        #text
        self.init_data_Text = Text(self.init_window_name, width=65, height=35) # Original input box
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=65, height=49) # output
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=65, height=9) # log
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #button
        #label
        self.removespace_button_label = Label(self.init_window_name, text="--Other Functions--")
        self.removespace_button_label.grid(row=7, column=11)
        self.remove_blank_button = Button(self.init_window_name, text="Remove Space", bg="lightblue", width=10,command=self.removeblank) # use  method
        self.remove_blank_button.grid(row=8, column=11)
        #button2
        self.change_case_button = Button(self.init_window_name, text="To Lower Case", bg="lightblue", width=10,command=self.caseConverter)
        self.change_case_button.grid(row=9, column=11)
        #Button3
        #Label
        self.money_button_label = Label(self.init_window_name, text="Digital ￥ TO Character ￥:")
        self.money_button_label.grid(row=11, column=11)
        self.money_button = Button(self.init_window_name, text="Convert Now", bg="lightblue", width=10,command=self.numToBig)
        self.money_button.grid(row=12, column=11)
        # # Text Replacement # #
        #Label
        self.replace_original_label = Label(self.init_window_name, text="Target Character:")
        self.replace_original_label.grid(row=1, column=11)
        # text box
        self.replace_original_text = Text(self.init_window_name, width=10, height=1) # to be replaced
        self.replace_original_text.grid(row=2, column=11)
        # label
        self.replace_with_label = Label(self.init_window_name, text="Replaced Character")
        self.replace_with_label.grid(row=3, column=11)
        # label
        self.replace_with_text = Text(self.init_window_name, width=10, height=1) # to be replaced
        self.replace_with_text.grid(row=4, column=11)
        # button
        self.replace_button = Button(self.init_window_name, text="Replace", bg="lightblue", width=10,command=self.replaceText)
        self.replace_button.grid(row=5, column=11)

    #insert output values to the window
    def insertOutput(self,output):
        self.result_data_Text.delete(1.0,END)
        self.result_data_Text.insert(1.0,output)

    def getInput(self):
        return str(self.init_data_Text.get(1.0,END))

    #functional Function, Remove Blank
    def removeblank(self):
        #input
        input_str = self.getInput()
        #去除空格
        out_str = input_str.strip().replace(" ","")
        out_str = out_str.strip().replace("\t","")
        #Print value
        self.insertOutput(out_str)
        self.write_log_to_Text("INFO: Space Removal SUCCESS!")

    ## replace input text functions
    def replaceText(self):
        input_str = self.getInput()
        #get replace original input
        replace_original = self.replace_original_text.get(1.0,END).strip()
        replace_with = self.replace_with_text.get(1.0,END).strip()
        out_str = input_str.replace(replace_original,replace_with)
        #Print value
        self.insertOutput(out_str)
        self.write_log_to_Text("INFO: Character Replacement SUCCESS!")

    ## To lower or upper case characters depends on how many times this button been clicked
    def caseConverter(self):
        input_str = self.getInput()
        #get replace original input
        if self.flag == 0:
            out_str = input_str.lower()
            self.write_log_to_Text("INFO: To Lower Case SUCCESS!")
            self.change_case_button.config(text="To Upper Case")
            self.flag = 1
        else:
            out_str = input_str.upper()
            self.write_log_to_Text("INFO: To Upper Case SUCCESS!")
            self.change_case_button.config(text="To Lower Case")
            self.flag = 0
        # Print value
        self.insertOutput(out_str)

    # Get current Time
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time

    # Print log
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"   #next line
        # Delete old log
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)

    
    #author：FarryNiu
    #https://blog.csdn.net/qq_43474959/article/details/107852510
    #Implemented by Chenghao Li on 27/01/2021
    def numToBig(self):
        dict1 = {1:'壹',2:'贰',3:'叁',4:'肆',5:'伍',6:'陆',7:'柒',8:'捌',9:'玖',0:'零'}
        dict2 = {2:'拾',3:'佰',4:'仟',5:'万',6:'拾',7:'佰',8:'仟',1:'元',11:'整'}
        money = '' #最终大写数字
        flag = False #去掉多余的十百千
        flag2 = False #增加零
        ifint = False #整
        count = 0
        num = self.getInput()
        ## Error Security Check
        try:
            strnum = str(int(num))
            if int(strnum) > 99999999:   # MAX 为一亿
                self.insertOutput("请检查金额格式，最大金额小于1亿元")
                self.write_log_to_Text("INFO: 金额转换 failed!")
                return
        except:
            self.insertOutput("请检查金额格式，仅支持整数")
            self.write_log_to_Text("INFO: 金额转换 failed!")
            return
        #splitting the number
        aa = strnum.split('.')   #split money into int and decimal part
        bb = list(str(aa[:1])[2:-2])  # int part
        cc = list(str(aa[1:])[2:-2])   # decimal part
        #此处控制：无小数时输出xxx元整
        #若要求一位小数也带整，即xxx元整并且xxx元xx角整，则修改下方0为1
        if len(cc) <= 0:
            ifint = True
        else:
            ifint = False
        #整数部分
        for i in reversed(bb):
            count = count + 1
            if(int(i) == 0):
                if(flag == True):
                    if(count != 5):
                        continue
                    else:
                        money = dict2[count] + money 
                else:
                    if(flag2 == False):
                        money = dict2[count] + money 
                    else:
                        if(count != 5):
                            money = '零' + money
                        else:
                            money = dict2[count] + '零' +money 
                flag = True
            else:
                flag = False
                flag2 = True
                money = dict1[int(i)]+dict2[count]+money
        if(ifint == True):
            money = money + '整'
        #Print value
        self.insertOutput(money)
        self.write_log_to_Text("INFO: ￥" + str(int(num)) + " 金额转换 success!")




#Start APP
def start_my_app():
    # Initialise TK ()
    myWindow = Tk()
    MYApp = MY_WINDOW(myWindow)
    # Set window properties
    MYApp.set_initial_window()
    # Go into Loop
    myWindow.mainloop()

start_my_app()