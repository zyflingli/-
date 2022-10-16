#  *_* coding:utf8 *_*
import tkinter
from functools import partial

#切换到费用分摊计算器
     
def jiemian1():
    
# 按钮输入调用
    def get_input(entry, argu):
    # 从entry窗口展示中获取输入的内容
      input_data = entry.get()

    # 出现连续+，则第二个+为无效输入，不做任何处理
      if (input_data[-1:] == '+') and (argu == '+'):
        return
    # 出现连续+--，则第三个-为无效输入，不做任何处理
      if (input_data[-2:] == '+-') and (argu == '-'):
        return
    # 窗口已经有--后面字符不能为+或-
      if (input_data[-2:] == '--') and (argu in ['-', '+']):
        return
    # 窗口已经有 ** 后面字符不能为 * 或 /
      if (input_data[-2:] == '**') and (argu in ['*', '/']):
        return

    # 输入合法将字符插入到entry窗口结尾
      entry.insert("end", argu)

# 退格(撤销输入)
    def backspace(entry):
      input_len = len(entry.get())
    # 删除entry窗口中最后的字符
      entry.delete(input_len - 1)

# 清空entry内容(清空窗口)
    def clear(entry):
      entry.delete(0, "end")

# 计算
    def calc(entry):
      input_data = entry.get()
    # 计算前判断输入内容是否为空;首字符不能为*/;*/不能连续出现3次;
      if not input_data:
        return

      clear(entry)

    # 异常捕获，在进行数据运算时如果出现异常进行相应处理
    # noinspection PyBroadException
      try:
        # eval() 函数用来执行一个字符串表达式，并返回表达式的值；并将执行结果转换为字符串
        output_data = str(eval(input_data))
      except Exception:
        # 将提示信息输出到窗口
        entry.insert("end", "Calculation error")
      else:
        # 将计算结果显示在窗口中
        if len(output_data) > 20:
            entry.insert("end", "Value overflow")
        else:
            entry.insert("end", output_data)


    if __name__ == '__main__':

        root = tkinter.Tk()
        root.title("计算器")

    # 框体大小可调性，分别表示x,y方向的可变性；
        root.resizable(0, 0)

        button_bg = 'bisque'
        math_sign_bg = 'orange'
        cal_output_bg = 'cornflowerblue'
        button_active_bg = 'gray'
        button_switchover_bg ='sandybrown'

    # justify:显示多行文本的时候, 设置不同行之间的对齐方式，可选项包括LEFT, RIGHT, CENTER
    # 文本从窗口左方开始显示，默认可以显示20个字符
    # row：entry组件在网格中的横向位置
    # column：entry组件在网格中的纵向位置
    # columnspan:正常情况下,一个插件只占一个单元;可通过columnspan来合并一行中的多个相邻单元
        entry = tkinter.Entry(root, justify="right", font=1)
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        def place_button(text, func, func_params, bg=button_bg, **place_params):
        # 偏函数partial，可以理解为定义了一个模板，后续的按钮在模板基础上进行修改或添加特性
        # activebackground：按钮按下后显示颜place_params色
           my_button = partial(tkinter.Button, root, bg=button_bg, padx=10, pady=3, activebackground=button_active_bg)
           button = my_button(text=text, bg=bg, command=lambda: func(*func_params))
           button.grid(**place_params)

    # 文本输入类按钮
        place_button('7', get_input, (entry, '7'), row=1, column=0, ipadx=5, pady=5)
        place_button('8', get_input, (entry, '8'), row=1, column=1, ipadx=5, pady=5)
        place_button('9', get_input, (entry, '9'), row=1, column=2, ipadx=5, pady=5)
        place_button('4', get_input, (entry, '4'), row=2, column=0, ipadx=5, pady=5)
        place_button('5', get_input, (entry, '5'), row=2, column=1, ipadx=5, pady=5)
        place_button('6', get_input, (entry, '6'), row=2, column=2, ipadx=5, pady=5)
        place_button('1', get_input, (entry, '1'), row=3, column=0, ipadx=5, pady=5)
        place_button('2', get_input, (entry, '2'), row=3, column=1, ipadx=5, pady=5)
        place_button('3', get_input, (entry, '3'), row=3, column=2, ipadx=5, pady=5)
        place_button('0', get_input, (entry, '0'), row=4, column=0, padx=8, pady=5,
                 columnspan=2, sticky=tkinter.E + tkinter.W + tkinter.N + tkinter.S)
        place_button('.', get_input, (entry, '.'), row=4, column=2, ipadx=7, padx=5, pady=5)

    # 运算输入类按钮(只是背景色不同)
    # 字符大小('+','-'宽度不一样,使用ipadx进行修正)
        place_button('+', get_input, (entry, '+'), bg=math_sign_bg, row=1, column=3, ipadx=5, pady=5)
        place_button('-', get_input, (entry, '-'), bg=math_sign_bg, row=2, column=3, ipadx=5, pady=5)
        place_button('*', get_input, (entry, '*'), bg=math_sign_bg, row=3, column=3, ipadx=5, pady=5)
        place_button('/', get_input, (entry, '/'), bg=math_sign_bg, row=4, column=3, ipadx=5, pady=5)

    # 功能输入类按钮(背景色、触发功能不同)
        place_button('<-', backspace, (entry,), row=5, column=0, ipadx=5, padx=5, pady=5)
        place_button('C', clear, (entry,), row=5, column=1, pady=5, ipadx=5)
        place_button('=', calc, (entry,), bg=cal_output_bg, row=5, column=2, ipadx=5, padx=5, pady=5,
                 columnspan=2, sticky=tkinter.E + tkinter.W + tkinter.N + tkinter.S)



def jiemian2():
    import tkinter
    
    def get_content(cArray):
        cArray.append(''.join(startPoint_entry.get()))
        cArray.append(''.join(endPoint1_entry.get()))
        cArray.append(''.join(endPoint2_entry.get()))

    def get_cost(conArray):
        #测试数据，此处还需优化
        if (conArray[0]=="大世界") and (conArray[1]=="同济大学") and (conArray[2]=="上海财经大学"):
            cosArray = [30,20,40,55]
        return cosArray

    #费用分摊函数
    def cost_allocation(cost):
        #如果设置途经点比各自打车便宜，则拼车
        if (cost[2] < cost[0]+cost[1]) or (cost[3] < cost[0]+cost[1]):
            #各自应分摊的金额
            finalCost = min(cost[2], cost[3])
            finalCost1 = finalCost*cost[0]/(cost[0]+cost[1])
            finalCost2 = finalCost*cost[1]/(cost[0]+cost[1])
            tkinter.Label(window, text = "第一名乘客需要分摊{}元，第二名乘客需要分摊{}元".format(finalCost1, finalCost2)).place(x=10,y=150)
            #各自节省的金额
            saveCost1 = cost[0]-finalCost1
            saveCost2 = cost[1]-finalCost2
            tkinter.Label(window, text = "第一名乘客节省了{}元，第二名乘客节省了{}元".format(saveCost1, saveCost2)).place(x=10,y=180)
        #如果各自打车更便宜，则不需要拼车
        else:
            tkinter.Label(window, text = "不需要拼车").place(x=10,y=150)

    def act():
        contentArray = []
        costArray = []
        get_content(contentArray)
        costArray = get_cost(contentArray)
        cost_allocation(costArray)
 
    window = tkinter.Tk()
    window.wm_title("出租车拼车费用分摊")
    window.geometry('400x260')
    #界面：输入起点
    startPoint = tkinter.Label(window, text = "输入起点：")
    startPoint.place(x=10,y=8)
    startPoint_entry = tkinter.Entry(window, bd=5)
    startPoint_entry.place(x=100,y=8)
    #界面：输入终点1
    endPoint1 = tkinter.Label(window, text = "输入终点1：")
    endPoint1.place(x=10,y=38)
    endPoint1_entry = tkinter.Entry(window, bd=5)
    endPoint1_entry.place(x=100,y=38)
    #界面：输入终点2
    endPoint2 = tkinter.Label(window, text = "输入终点2：")
    endPoint2.place(x=10,y=68)
    endPoint2_entry = tkinter.Entry(window, bd=5)
    endPoint2_entry.place(x=100,y=68)
    #按钮
    tkinter.Button(window, text="计算分摊结果", command=act).place(x=50,y=110)
    
    window.mainloop()


jiemian1()
jiemian2()