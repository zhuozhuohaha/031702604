# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 00:40:43 2019

@author: zy-pc
"""
import json
import re
Alist=[]
Alist.append("北京")
Alist.append("上海")
Alist.append("天津")
Alist.append("重庆")
Alist.append("西藏自治区")
Alist.append("新疆维吾尔族自治区")
Alist.append("广西壮族自治区")
Alist.append("宁夏回族自治区")
Alist.append("内蒙古自治区")
Alist.append("河北")
Alist.append("河南")
Alist.append("山东")
Alist.append("山西")
Alist.append("江苏")
Alist.append("安徽")
Alist.append("陕西")
Alist.append("甘肃")
Alist.append("青海")
Alist.append("湖北")
Alist.append("湖南")
Alist.append("浙江")
Alist.append("江西")
Alist.append("福建")
Alist.append("贵州")
Alist.append("四川")
Alist.append("广东")
Alist.append("云南")
Alist.append("海南")
Alist.append("黑龙江")
Alist.append("吉林")
Alist.append("辽宁")
allCityList=[]
allCityList.append(["北京"])
allCityList.append(["上海"])
allCityList.append(["天津"])
allCityList.append(["重庆"])
allCityList.append(["拉萨","昌都地区","山南地区","阿里地区","那曲地区","林芝地区","日喀则地区"])
allCityList.append(["乌鲁木齐", "阿勒泰", "阿克苏", "昌吉", "哈密", "和田", "喀什", "克拉玛依", "石河子", "塔城", "库尔勒", "吐鲁番", "伊宁"])
allCityList.append(["南宁", "桂林", "阳朔", "柳州", "梧州", "玉林", "桂平", "贺州", "钦州", "贵港", "防城港", "百色", "北海", "河池", "来宾", "崇左"])
allCityList.append(["银川", "固原", "中卫", "石嘴山", "吴忠"])
allCityList.append(["呼和浩特", "呼伦贝尔", "锡林浩特", "包头", "赤峰", "海拉尔", "乌海", "鄂尔多斯", "通辽"])
allCityList.append(["石家庄", "唐山", "张家口", "廊坊", "邢台", "邯郸", "沧州", "衡水", "承德", "保定", "秦皇岛"])
allCityList.append(["郑州", "开封", "洛阳", "平顶山", "焦作", "鹤壁", "新乡", "安阳", "濮阳", "许昌", "漯河", "三门峡", "南阳", "商丘", "信阳", "周口", "驻马店"])
allCityList.append(["济南", "青岛", "淄博", "威海", "曲阜", "临沂", "烟台", "枣庄", "聊城", "济宁", "菏泽", "泰安", "日照", "东营", "德州", "滨州", "莱芜", "潍坊"])
allCityList.append(["太原", "阳泉", "晋城", "晋中", "临汾", "运城", "长治", "朔州", "忻州", "大同", "吕梁"])
allCityList.append(["南京", "苏州", "昆山", "南通", "太仓", "吴县", "徐州", "宜兴", "镇江", "淮安", "常熟", "盐城", "泰州", "无锡", "连云港", "扬州", "常州", "宿迁"])
allCityList.append(["合肥", "巢湖", "蚌埠", "安庆", "六安", "滁州", "马鞍山", "阜阳", "宣城", "铜陵", "淮北", "芜湖", "毫州", "宿州", "淮南", "池州"])
allCityList.append(["西安", "韩城", "安康", "汉中", "宝鸡", "咸阳", "榆林", "渭南", "商洛", "铜川", "延安"])
allCityList.append(["西宁", "海北", "海西", "黄南", "果洛", "玉树", "海东", "海南"])
allCityList.append(["武汉", "宜昌", "黄冈", "恩施", "荆州", "神农架", "十堰", "咸宁", "襄樊", "孝感", "随州", "黄石", "荆门", "鄂州"])
allCityList.append(["长沙", "邵阳", "常德", "郴州", "吉首", "株洲", "娄底", "湘潭", "益阳", "永州", "岳阳", "衡阳", "怀化", "韶山", "张家界"])
allCityList.append(["杭州", "湖州", "金华", "宁波", "丽水", "绍兴", "雁荡山", "衢州", "嘉兴", "台州", "舟山", "温州"])
allCityList.append(["南昌", "萍乡", "九江", "上饶", "抚州", "吉安", "鹰潭", "宜春", "新余", "景德镇", "赣州"])
allCityList.append(["福州", "厦门", "龙岩", "南平", "宁德", "莆田", "泉州", "三明", "漳州"])
allCityList.append(["贵阳", "安顺", "赤水", "遵义", "铜仁", "六盘水", "毕节", "凯里", "都匀"])
allCityList.append(["成都", "泸州", "内江", "凉山", "阿坝", "巴中", "广元", "乐山", "绵阳", "德阳", "攀枝花", "雅安", "宜宾", "自贡", "甘孜州", "达州", "资阳", "广安", "遂宁", "眉山", "南充"] )
allCityList.append(["广州", "深圳", "潮州", "韶关", "湛江", "惠州", "清远", "东莞", "江门", "茂名", "肇庆", "汕尾", "河源", "揭阳", "梅州", "中山", "德庆", "阳江", "云浮", "珠海", "汕头", "佛山"])
allCityList.append(["昆明", "保山", "楚雄", "德宏", "红河", "临沧", "怒江", "曲靖", "思茅", "文山", "玉溪", "昭通", "丽江", "大理"])
allCityList.append(["海口", "三亚", "儋州", "琼山", "通什", "文昌"])
allCityList.append(["哈尔滨", "齐齐哈尔", "牡丹江", "大庆", "伊春", "双鸭山", "鹤岗", "鸡西", "佳木斯", "七台河", "黑河", "绥化", "大兴安岭"])
allCityList.append(["长春", "延边", "吉林", "白山", "白城", "四平", "松原", "辽源", "大安", "通化"])
allCityList.append(["沈阳", "大连", "葫芦岛", "旅顺", "本溪", "抚顺", "铁岭", "辽阳", "营口", "阜新", "朝阳", "锦州", "丹东", "鞍山"])
x=input()
x=x.replace(".","")
dict={}
S=0
if x[0]=="1":
    x=x.replace("1!","")
    y=x.split(",",1)
    dict["姓名"]=y[0]
    m=y[1]
    k=re.findall(r"\d\d\d\d\d\d\d\d\d\d\d",m)
    dict["号码"]=k[0]
    m=m.replace(k[0],"")
    k=re.findall(r".*?省|.*?自治区",m)
    t=[]
    if k:
        t.append(k[0])
        m=m.replace(k[0],"")
    else:
        for i in range(len(Alist)):
            a=re.findall(Alist[i],m)
            if(a):
                S=i
                if i<4:      
                    t.append(a[0])
                if 8<i<31:
                    b=a[0]
                    a[0]+="省"
                    t.append(a[0])
                    m=m.replace(b,"")
                break
    
    k=re.findall(r".*?市",m)
    if k:
        t.append(k[0])
        m=m.replace(k[0],"")
    if k==None:
        for j in range(allCityList[S]):
            r=re.findall(len(allCityList))
            if(r):
                b=r[0]
                r[0]=r[0]+'市'
                m=m.replace(b,"")
                t.append(r[0])
                break
    k=re.findall(r".*?区",m)
    if k:
        t.append(k[0])
        m=m.replace(k[0],"")
    k=re.findall(r".*?镇",m)
    if k:
        t.append(k[0])
        m=m.replace(k[0],"")
    k=re.findall(r".*?乡",m)
    if k:
        t.append(k[0])
        m=m.replace(k[0],"")
    k=re.findall(r".*?街道|.*?街",m)
    if k:
        t.append(k[0])
        m=m.replace(k[0],"")
    if m:
        t.append(m)
    dict["地址"]=t
    json1=json.dumps(dict,ensure_ascii=False)
    print(json1)
    
if x[0]=="2":
    x=x.replace("2!","")
    y=x.split(",",1)
    dict["姓名"]=y[0]
    m=y[1]
    k=re.findall(r"\d\d\d\d\d\d\d\d\d\d\d",m)
    dict["号码"]=k[0]
    m=m.replace(k[0],"")
    k=re.findall(r".*?省|.*?自治区",m)
    t=[]
    if k:
        t.append(k[0])
        m=m.replace(k[0],"")
    else:
        for i in range(len(Alist)):
            a=re.findall(Alist[i],m)
            if(a):
                S=i
                if i<4:      
                    t.append(a[0])
                if 8<i<31:
                    b=a[0]
                    a[0]+="省"
                    t.append(a[0])
                    m=m.replace(b,"")
                break
    
    k=re.findall(r".*?市",m)
    if k:
        t.append(k[0])
        m=m.replace(k[0],"")
    if k==None:
        for j in range(allCityList[S]):
            r=re.findall(len(allCityList))
            if(r):
                b=r[0]
                r[0]=r[0]+'市'
                m=m.replace(b,"")
                t.append(r[0])
                break
    k=re.findall(r".*?区",m)
    if k:
        t.append(k[0])
        m=m.replace(k[0],"")
    k=re.findall(r".*?镇",m)
    if k:
        t.append(k[0])
        m=m.replace(k[0],"")
    k=re.findall(r".*?乡",m)
    if k:
        t.append(k[0])
        m=m.replace(k[0],"")
    k=re.findall(r".*?街道|.*?街",m)
    if k:
        t.append(k[0])
        m=m.replace(k[0],"")
    k=k=re.findall(r".*?路",m)
    if k:
        t.append(k[0])
        m=m.replace(k[0],"")
    k=re.findall(r".*?号",m)
   
    if k:
        t.append(k[0])
        m=m.replace(k[0],"")
    #p="".join(k)
    #m=m.replace(p,"")
    if m:
        t.append(m)
    dict["地址"]=t
    json1=json.dumps(dict,ensure_ascii=False)
    print(json1)