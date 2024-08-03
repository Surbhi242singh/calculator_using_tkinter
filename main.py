from tkinter import *

first_op=second_op=op=None

def operate(operator):
    global first_op,op
    first_op=int(res_lbl['text'])
    op=operator
    res_lbl.config(text='')

def result():
    global first_op,op,second_op
    second_op=int(res_lbl['text'])
    if op=='+':
        res=first_op+second_op
    elif op=='-':
        res=first_op-second_op
    elif op=='x':
        res=first_op*second_op
    else:
        if second_op==0:
            res='Error'
        else:
            res=round(first_op/second_op,3)   

    res_lbl.config(text=res)

def disp_digit(digit):
    current=res_lbl['text']
    new=current+str(digit)
    res_lbl.config(text=new)

def clear_scn():
    res_lbl.config(text='')

root=Tk()
root.title('Calculator')
root.iconbitmap('favicon.ico')
root.config(background='black')
root.geometry('280x350')
root.resizable(0,0)               #no movement in any direction

res_lbl=Label(root,text='',bg='black',fg='white')
res_lbl.grid(row=0,column=0,columnspan=5,pady=(50,10),padx=(10),sticky='w')           #top-left
res_lbl.config(font=('verdana',20,'bold'))

btn7=Button(root,text='7',bg='#939E8F',fg='white',width=5,height=2,command=lambda: disp_digit(7))         #lambda used for calling function with parameter
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14))

btn4=Button(root,text='4',bg='#939E8F',fg='white',width=5,height=2,command=lambda: disp_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14))

btn1=Button(root,text='1',bg='#939E8F',fg='white',width=5,height=2,command=lambda: disp_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14))

btn0=Button(root,text='0',bg='#939E8F',fg='white',width=5,height=2,command=lambda: disp_digit(0))
btn0.grid(row=4,column=0)
btn0.config(font=('verdana',14))

btn8=Button(root,text='8',bg='#939E8F',fg='white',width=5,height=2,command=lambda: disp_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14))

btn5=Button(root,text='5',bg='#939E8F',fg='white',width=5,height=2,command=lambda: disp_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14))

btn2=Button(root,text='2',bg='#939E8F',fg='white',width=5,height=2,command=lambda: disp_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14))

btn_clear=Button(root,text='C',bg='#939E8F',fg='white',width=5,height=2,command=clear_scn)
btn_clear.grid(row=4,column=1)
btn_clear.config(font=('verdana',14))

btn9=Button(root,text='9',bg='#939E8F',fg='white',width=5,height=2,command=lambda: disp_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14))

btn6=Button(root,text='6',bg='#939E8F',fg='white',width=5,height=2,command=lambda: disp_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14))

btn3=Button(root,text='3',bg='#939E8F',fg='white',width=5,height=2,command=lambda: disp_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14))

btn_equal=Button(root,text='=',bg='#939E8F',fg='white',width=5,height=2,command=result)
btn_equal.grid(row=4,column=2)
btn_equal.config(font=('verdana',14))

btn_mul=Button(root,text='x',bg='#939E8F',fg='white',width=5,height=2,command=lambda:operate('x'))
btn_mul.grid(row=1,column=3)
btn_mul.config(font=('verdana',14))

btn_div=Button(root,text='/',bg='#939E8F',fg='white',width=5,height=2,command=lambda:operate('/'))
btn_div.grid(row=2,column=3)
btn_div.config(font=('verdana',14))

btn_add=Button(root,text='+',bg='#939E8F',fg='white',width=5,height=2,command=lambda:operate('+'))
btn_add.grid(row=3,column=3)
btn_add.config(font=('verdana',14))

btn_sub=Button(root,text='-',bg='#939E8F',fg='white',width=5,height=2,command=lambda:operate('-'))
btn_sub.grid(row=4,column=3)
btn_sub.config(font=('verdana',14))

root.mainloop()