def Monte_Carlo(k,j,l,m):
    b=[]
    a=np.random.random(k)
    for i in a:
        if i>(j/100):
            i=1-(l/100)
            b.append(i)  #i大於自己的勝率代表賠錢
        else:
            i=1+(m/100)
            b.append(i) #i小於自己的勝率 代表賺錢
            
    K=[] #帳戶逐筆狀況
    F=[]
    G=1 #本金
    for i in range(0,k):
        F.append(i)
    for i in b:
        G=G*i
        K.append(G)
        
    plt.style.use('ggplot')
    plt.figure(figsize=(15,9),facecolor='lightblue')
    plt.plot(F,K,'k')
    plt.grid(True)
    plt.xlabel('times')
    plt.ylabel('capital')
    
    if K[-1]>1.3:
        print()
        print('********可執行的策略!********\n\n賺賠比有{0:},勝率有{1:}%,交易{2:}次以後,資金有機率膨脹到{3:.2f}倍'\
              .format(m/l,j,k,K[-1]))
    elif (K[-1]>=1) & (K[-1]<=1.3):
        print()
        print('********策略要再想一下了********\n\n冒了{0:}次風險,可是本金只膨脹到{1:.2f}倍'.format(k,K[-1]))
    else:
        print()
        print('********這策略母湯!********\n\n資金正在縮水啦!,交易{0:}次以後,資金只剩原本的{1:.2f}倍'\
              .format(k,K[-1]))

####################################################################################

import numpy as np
import matplotlib.pyplot as plt

print('1.你想要測試的"交易次數"(建議80筆以上),2.過去平均"勝率",3."平均一次損失本金百分比",4.最後是"平均一次賺本金百分比"')
print('均為"整數"數字!,ex:600,47,3,7\n')
k,j,l,m=eval(input('在這邊輸入=>'))

Monte_Carlo(k,j,l,m)