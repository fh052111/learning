import jieba
import string
jieba.load_userdict(r''/Users/fanghao/Desktop/坚果一号/计算社会学习/work/西游记.txt'')
with open(''/Users/fanghao/Desktop/坚果一号/计算社会学习/work/西游记.txt'',encoding='gb18030')as fin:
    l=[]
    d={}
    txt=fin.read()
    txt=txt.replace('\n','')

monkey = ['孙悟空','美猴王','齐天大圣','斗战胜佛','孙行者','猴头','老孙']
pig = ['猪八戒','悟能','呆子','老猪']
fish = ['沙悟净','沙师弟','沙和尚']
human = ['唐僧','御弟','金蝉子','金蝉子']