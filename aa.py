

import  os
file='spend_list.txt'  #全局变量
def main():
    while True:
        menu()
        acc=int(input('请选择功能：'))
        if acc in [0,1,2,3,4,5]:
            if acc==0:
                exit=input('是否真的退出?y/n:')
                if exit=='y':
                    break
                else:
                    continue
        if acc == 1:
            input_spend()
        if acc == 2:
            find_spend()
        if acc == 3:
            del_spend()
        if acc == 4:
            modify_spend()
        if acc == 5:
            show()

def menu():
    print('====欢迎使用小账本====')
    print('     1.输入花销')
    print('     2.查找花销')
    print('     3.删除花销')
    print('     4.修改花销')
    print('     5.显示花销')
    print('     0.退出')

def input_spend():
    spend_list=[]
    while True:
        try:
            date= input('日期(例如20210809)：')
            wear = input('衣：')
            food = input('食：')
            live = input('住：')
            move = input('行：')
            other = input('其他：')
        except:
            print('输入有误，只能输入数字，请重新输入')
            continue
        d={'date':date,'wear':wear,'food':food,'live':live,'move':move,'other':other}
        spend_list.append(d)
        ansewer=input('是否继续添加？y/n：')
        if ansewer=='y':
            continue
        elif ansewer=='n':
            break
    save(spend_list)
    print('输入完毕！')

def save(lst):
    try:
        file1=open(file,'a',encoding='utf-8')
    except:
        file1=open(file,'w',encoding='utf-8')
    for i in lst:
        file1.write(str(i)+'\n')
    file1.close()

def find_spend():
    spend_new=[]
    while True:
        date=''
        if os.path.exists(file):
            date=input('请输入日期(例如20120806)：')
            with open(file,'r',encoding='utf-8') as rfile:
                spend=rfile.readlines()
                for i in spend:
                    d=dict(eval(i))
                    if date!="":
                        if d['date']==date:
                            spend_new.append(d)
            show_spend(spend_new)
            spend_new.clear()
            ansewer = input('是否继续查找？y/n：')
            if ansewer == 'y':
                continue
            elif ansewer == 'n':
                break

def show_spend(lst):
    if len(lst)==0:
        print('没有找到账单信息!')
        return
        # 定义标题显示格式,看不懂照着打的
    format_xinix = '{:^6}\t{:^18}\t{:^7}\t{:^9}\t{:^9}\t{:^7}'
    print(format_xinix.format('日期', '衣服', '饮食', '居住', '出行', '其他'))
    # 定义内容显示格式
    format_date = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for i in lst:
        print(format_date.format(i.get('date'),
                                 i.get('wear'),
                                 i.get('food'),
                                 i.get('live'),
                                 i.get('move'),
                                 i.get('other')))

#有BUG明天查BUG
def del_spend():
        global file
        while True:
            date=input('请输如要删除的日期：')
            if date!='':
                if os.path.exists(file):
                    with open(file,'r',encoding='utf-8') as rfile:
                        spend_old=rfile.readlines()
                        for i in spend_old:
                            d=dict(eval(i))
                            if d['date']==date:
                                pass
                else:
                    spend_old=[]  #如果文件不存在定义一个控列表
                flag=False #定义一个是否删除的标记，默认为没删除
                if spend_old:  #用列表对象并判断True，Flase
                    with open(file,'w',encoding='utf-8') as wfile:
                        d={}
                        for i in  spend_old:
                            d=dict(eval(i))
                            if d['date']!=date:
                                wfile.write(str(i)+'\n')
                            else:
                                file=True  #表示已经删除
                        if flag: #可以利用flag判断是否删除成功
                            print(f'日期为{date}的账目已删除')
                        else:
                            print(f'没有找到日期为{date}的账单')
            else:
                print('没有账目信息')
                break
            #删除之后重新显示账目信息
            show()
            #判断一下是否继续删除
            answer=input('是否继续删除？y/n：')
            if answer=='y' :
                continue
            else:
                break

def modify_spend():
    d={}
    if os.path.exists(file):
        with open(file,'r',encoding='utf-8') as rfile:
            spend_old=rfile.readlines()
    else:
        return
    date=input('请输入要修改的日期：')
    with open(file,'w',encoding='utf-8') as  wfile:
        for i in spend_old:
            d=dict(eval(i)) #把读出来的列表遍历，放入字典中
            if d['date']==date:
                print('找到信息，可以修改信息')
                while True:
                    try: #防止输入出错
                        d['wear']=input('衣:')
                        d['food']=input('食:')
                        d['live']=input('住:')
                        d['move']=input('行:')
                        d['other']=input('其他:')
                    except:
                        print('输入有误！请重新输入！')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功！')
            else:
                wfile.write(str(d)+'\n')
        answer=input('是否继续修改y/n？:\n')
        if answer=='y':
            modify_spend()
        else:
            print('修改结束！')

def show():
    spend_old=[]
    if os.path.exists(file):
        with open(file,'r',encoding='utf-8') as rfile:
            spend=rfile.readlines()
            for i in spend:
                spend_old.append(eval(i))
            if spend_old!='':
                show_spend(spend_old)
    else:
        print('暂时为保存账单信息!')

if __name__ == '__main__':
    main()