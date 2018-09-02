#导入监控服务库
from QuickLibMonitor import *
monitor = QuickLibMonitor()   #交易接口类赋值给变量 

''' 
#cmd字段及函数定义
def fun1():
    print u"指令:重新启动电脑\n"
    #monitor.restart() 
    
def fun2():
    print u"指令:重新启动交易程序\n"   
    #monitor.exit()
    
def fun3():
    print u"指令:平掉所有仓位\n"  
    #加入自己的平仓逻辑
    
def fun4():
    print u"指令:禁止开仓\n"
    #应该在所有开仓指令前，判断autostate是否为True,若为False则不开仓 
    autostate=False

#含有MONITOR表示监控客户端发来的指令，含有SERVER表示发送给监控端的指令
#含有SYSTEM表示QuickLib监控库内置指令,含有TRADER表示用户需在交易系统中自定义的指令逻辑
cmddict = {MONITOR_SYSTEM_RESTART:fun1, MONITOR_SYSTEM_RESTARTAPP:fun2, MONITOR_TRADER_CLOSEALLPOSITION:fun3,MONITOR_TRADER_ABITIONOPEN:fun4}

#Index = dict()
#Index[str(data[0].InstrumentID)] = data 

def CheckCmd():
    global cmddict
    lastid=0
    while (1):
        cmdsize=monitor.GetCmdSize()
        if cmdsize>0:
            #print u"还有%d条未处理"%cmdsize
            print(u'获得新指令\n');
            #方法1：python没有switch语句，用dict字典替代switch语句，效果高
            cmddict[monitor.GetCmd()]()
        time.sleep(0.1)	
'''        
#------------------------------------------Monitor回调代码段开始----------------------------------------------
#TRADER_SYSTEM_MUSIC                = 8500 #获得预警音乐状态
#TRADER_SYSTEM_ALERT                = 8501 #获得预警弹窗状态
#TRADER_SYSTEM_READ                 = 8502 #获得预警朗读状态
#交易系统指令同步、转发给监控器的指令类型(MD,TD->TRADER->MONITOR)(QuickLib交易系统指令相同其它交易平台需需按QuickLib指令类型转发给监控器)
SERVER_SYSTEM_NONE                  =8000 #无
SERVER_LOGIN_SCUESS                 =8001 #登录成功
SERVER_LOGIN_DENIED                 =8002 #登录被拒绝
SERVER_LOGIN_ERRORPASSWORD          =8003 #密码错误 ??
SERVER_LOGINOUT_SCUESS              =8004 #登出成功
SERVER_NETCONNECT_SCUESS            =8005 #连接成功
SERVER_NETCONNECT_BREAK             =8006 #断开连接
SERVER_NETCONNECT_FAILER            =8007 #连接失败 ??
SERVER_SUBCRIBE_SCUESS              =8008 #订阅成功
SERVER_UNSUBCRIBE_SCUESS            =8009 #取消订阅成功
SERVER_NEWTICK                      =8010 #新Tick到来
SERVER_SYSTEM_ERROR                 =8011 #错误应答
SERVER_SYSTEM_SHUTDOWN             = 8012 #监控服务关闭
 
#TRADER发送的指令类型(TRADER->MONITOR)
TRADER_SYSTEM_RESTART               =8503
TRADER_SYSTEM_FULLMEMORY            =8504
TRADER_MONITOR_NOMONEY              =8505
TRADER_MONITOR_FULLMONEY            =8506
TRADER_MONITOR_INSERTORDER          =8507
TRADER_MONITOR_DELETEORDER          =8508

TRADER_TRADER_DEFINE1               =8900 #自定义消息1，仅用于在监控器端显示
TRADER_TRADER_DEFINE2               =8901 #自定义消息1，仅用于在监控器端显示
TRADER_TRADER_DEFINE3               =8902 #自定义消息1，仅用于在监控器端显示
#字典中的指令类型：
#监控器发送的状态指令类型(MONITOR->TRADER)
MONITOR_EMPTY                       =9000 #无
MONITOR_LOGIN_SCUESS                =9001 #登录成功
MONITOR_LOGIN_DENIED                =9002 #登录被拒绝
MONITOR_LOGIN_ERRORPASSWORD         =9003 #密码错误
MONITOR_LOGINOUT_SCUESS             =9004 #登出成功
MONITOR_NETCONNECT_SCUESS           =9005 #连接成功
MONITOR_NETCONNECT_BREAK            =9006 #断开连接
MONITOR_NETCONNECT_FAILER           =9007 #连接失败
MONITOR_SYSTEM_ERROR                =9008 #错误应答

#(2)监控器发送的远程管理指令类型(MONITOR->TRADER)
MONITOR_TRADER_MUSICON               =9500
MONITOR_TRADER_MUSICOFF              =9501
MONITOR_TRADER_ALERTON               =9502
MONITOR_TRADER_ALERTOFF              =9503
MONITOR_TRADER_READON                =9504
MONITOR_TRADER_READOFF               =9505
MONITOR_LOGIN                        =9506

MONITOR_SYSTEM_RESTART             = 9600  #重新启动windows
MONITOR_TRADER_RESTART             = 9601  #重新启动交易程序
MONITOR_TRADER_CLOSEALLPOSITION    = 9602  #平掉所有仓位
MONITOR_TRADER_ABITIONOPEN         = 9603  #继续行情接收，但禁止开仓
MONITOR_TRADER_CLOSEMARKED         = 9604  #停止行情接收
MONITOR_TRADER_SETGRADE1           = 9605  #设置发送监控器详细级别1(发送所有消息到监控器)
MONITOR_TRADER_SETGRADE2           = 9606  #设置发送监控器详细级别2(忽略数据量大的次要消息，例如tick信息)
MONITOR_TRADER_SETGRADE3           = 9607  #自定发送监控器详细级别3(只发送重要消息，例如与行情服务器失去连接、与交易服务器事情连接、断网事件、连网事件等)



MONITOR_DEFINE1             = 9900  #自定义指令1
MONITOR_DEFINE2             = 9901  #自定义指令2
MONITOR_DEFINE3             = 9902  #自定义指令3
MONITOR_DEFINE4             = 9903  #自定义指令4
MONITOR_DEFINE5             = 9904  #自定义指令5
MONITOR_DEFINE6             = 9905  #自定义指令6
MONITOR_DEFINE7             = 9906  #自定义指令7
MONITOR_DEFINE8             = 9907  #自定义指令8

def Monitor_OnEmptyCmd():
            #回调指令缓冲区已为空（因为短时间获得多个指令，时间间隔态度，在下面的for i in range(market.GetUnGetCmdSize()):循环执行了多次已经完成了）
            print "---------------Monitor_OnEmptyCmd---------------"    
def Monitor_OnUserLogin():
            #登录成功
            print "---------------Monitor_OnUserLogin---------------"
            #market.GetCmd_LoginScuess()
            #data = cast(market.GetCmd_LoginScuess(), POINTER(QL_CThostFtdcRspUserLoginField))
            #print "TradingDay %s"%(str(data[0].TradingDay))              #交易日       
def Monitor_OnUserLoginDenied():
            #登录被拒绝
            print "---------------Monitor_OnUserLoginDenied---------------"       
def Monitor_OnUserLoginErrorPassword():
            #登录密码错误
            print "---------------Monitor_OnUserLoginErrorPassword---------------"        
def Monitor_OnUserLogout():
            #登出成功
            print "---------------Monitor_OnUserLogout---------------"
            time.sleep(3)
            monitor.OnStart('wdg','123456',GB2312)
def Monitor_OnFrontConnected():
            #连接成功
            print "---------------Monitor_OnFrontConnected---------------"    
def Monitor_OnFrontDisconnected():
            #断开连接
            print "---------------Monitor_OnFrontDisconnected---------------"    
def Monitor_OnFrontConnectedFailer():
            #连接失败
            print "---------------Monitor_OnFrontConnectedFailer---------------"      
def Monitor_OnError():
            print "---------------MD_OnRspError---------------"   
def Monitor_OnShutdown():
            print "---------------Monitor_OnShutdown---------------"            
def Monitor_OnSystemRestart():
            print "---------------Monitor_OnSystemRestart---------------"   
            print u"指令:[重新启动计算机]"
            #monitor.restart() 
def Monitor_OnTraderRestart():
            print "---------------Monitor_OnTraderRestart---------------"   
            print u"指令:[重新启动交易程序]"
            #monitor.exit()
def Monitor_OnClosePosition():
            print "---------------Monitor_OnClosePosition---------------"              
            print u"指令:[平掉所有仓位]"  
            #加入自己的平仓逻辑
def Monitor_OnAbitiionOpen():
            print "---------------Monitor_OnAbitiionOpen---------------"                  
            print u"指令:[禁止开仓]"
            #应该在所有开仓指令前，判断autostate是否为True,若为False则不开仓 
            autostate=False
def Monitor_OnCloseMrrked():
            print "---------------Monitor_OnCloseMrrked---------------"                  
            print u"指令:[停止行情接收]"
            #应该在所有开仓指令前，判断autostate是否为True,若为False则不开仓 
            #autostate=False
def Monitor_OnSetGrade1():
            print "---------------Monitor_OnSetGrade1---------------"                   
            print u"指令:[设置发送监控器详细级别1(发送所有消息到监控器)]"
def Monitor_OnSetGrade2():
            print "---------------Monitor_OnSetGrade2---------------"                 
            print u"指令:[设置发送监控器详细级别2(忽略数据量大的次要消息，例如tick信息)]"
def Monitor_OnSetGrade3():
            print "---------------Monitor_OnSetGrade3---------------"               
            print u"指令:[自定发送监控器详细级别3(只发送重要消息，例如与行情服务器失去连接、与交易服务器事情连接、断网事件、连网事件等)]"
            
def Monitor_Define1():
            print "---------------Monitor_Define1---------------"               
            print u"指令: [自定义指令1]"
def Monitor_Define2():
            print "---------------Monitor_Define2---------------"               
            print u"指令: [自定义指令2]"
def Monitor_Define3():
            print "---------------Monitor_Define3---------------"               
            print u"指令: [自定义指令3]"
def Monitor_Define4():
            print "---------------Monitor_Define4---------------"
            print u"指令: [自定义指令4]"
def Monitor_Define5():
            print "---------------Monitor_Define5---------------"               
            print u"指令: [自定义指令5]"
def Monitor_Define6():
            print "---------------Monitor_Define6---------------"               
            print u"指令: [自定义指令6]"
def Monitor_Define7():
            print "---------------Monitor_Define7---------------"               
            print u"指令: [自定义指令7]"
def Monitor_Define8():
            print "---------------Monitor_Define8---------------"               
            print u"指令: [自定义指令8]"                
        
monitor_dict={
                  MONITOR_EMPTY:Monitor_OnEmptyCmd,
                  MONITOR_LOGIN_SCUESS:Monitor_OnUserLogin,
                  MONITOR_LOGIN_DENIED:Monitor_OnUserLoginDenied,
                  MONITOR_LOGIN_ERRORPASSWORD:Monitor_OnUserLoginErrorPassword,
                  MONITOR_LOGINOUT_SCUESS:Monitor_OnUserLogout,
                  MONITOR_NETCONNECT_SCUESS:Monitor_OnFrontConnected,
                  MONITOR_NETCONNECT_BREAK:Monitor_OnFrontDisconnected,
                  MONITOR_NETCONNECT_FAILER:Monitor_OnFrontConnectedFailer,
                  #SYSTEM_SUBCRIBE_SCUESS:Monitor_OnSubMarketData,
                  #SYSTEM_UNSUBCRIBE_SCUESS:Monitor_OnUnSubMarketData,
                  #SYSTEM_NEWTICK:MONITOR_OnTick,
                  MONITOR_SYSTEM_ERROR:Monitor_OnError,
                  SERVER_SYSTEM_SHUTDOWN:Monitor_OnShutdown,
                  MONITOR_SYSTEM_RESTART:Monitor_OnSystemRestart,
                  MONITOR_TRADER_RESTART:Monitor_OnTraderRestart,
                  MONITOR_TRADER_CLOSEALLPOSITION:Monitor_OnClosePosition,
                  MONITOR_TRADER_ABITIONOPEN:Monitor_OnAbitiionOpen,                  
                  MONITOR_TRADER_CLOSEMARKED:Monitor_OnAbitiionOpen,
                  MONITOR_TRADER_SETGRADE1:Monitor_OnSetGrade1,
                  MONITOR_TRADER_SETGRADE2:Monitor_OnSetGrade2,
                  MONITOR_TRADER_SETGRADE3:Monitor_OnSetGrade3,
                  MONITOR_DEFINE1:Monitor_Define1,
                  MONITOR_DEFINE2:Monitor_Define2,
                  MONITOR_DEFINE3:Monitor_Define3,
                  MONITOR_DEFINE4:Monitor_Define4,
                  MONITOR_DEFINE5:Monitor_Define5,
                  MONITOR_DEFINE6:Monitor_Define6,
                  MONITOR_DEFINE7:Monitor_Define7,
                  MONITOR_DEFINE8:Monitor_Define8
                  
        }
#------------------------------------------Monitor回调代码段结束----------------------------------------------        
            
# main()为程序入口函数，所有的行情、交易订阅、指标调用、下单的逻辑均写在此函数内执行
def main():
            print(u"官方QQ群 5172183 \n")
            #监控同步服务开启
            #               用户名 、密码、用户等级、传输数据的编码格式(即本文件的编码格式) 
            monitor.OnStart('wdg' ,'123123',QL_ADMIN,GB2312)  #远程管理员账户（有管理权限、有生成跟单文件权限）
            monitor.AddUser('lucky','111111',QL_ADMIN,GB2312)  #远程管理员账户（有管理权限、有生成跟单文件权限）
            monitor.AddUser('try','000000',QL_GUEST,GB2312)   #观摩用户，无跟单权限（不生成跟单文件，也无管理权限）
            #monitor.OnStart(u'wdg',u'123456',UTF_8)
            js=0
            while(1):   #死循环，防止退出
                        #time.sleep(5)
                        #这里应该有相应下单指令
                        #下单同时，将下单的消息同步给监控器
                        #monitor.OnSend(SERVER_TRADER_INSERTORDER,u'rb1701',6,2301,u'这是策略1执行的',u'备注字段1',u'备注字段2')
                        js=js+1
                        if(js>10000000):
                                    js=0
                                    monitor.OnSend(TRADER_MONITOR_INSERTORDER,u'rb1701',6,2301,u'策略id',u'备注字段1',u'备注字段2')
                                    
                        print(u"Wait for a New Cmd(Monitor)\n");
                        #判断是否有新Tick数据，while循环不需要Sleep,当没有新Tick时，会处在阻塞状态
                        monitor_dict[monitor.OnCmd()]()
                        print(u"Get A New cmd(Monitor)\n")
         
                        #CheckCmd();
        
                        #这里应该有相应的撤单指令
                        #撤单同时，将下单的消息同步给监控器
                        
                        
                        #monitor.OnSend(SERVER_TRADER_DELETEORDER,u'rb1701',6,2301,u'这是策略1执行的',u'备注字段1',u'备注字段2')
        
                        #监控同步服务停止
                        #monitor.OnStop()

if __name__ == '__main__':
            main()
    

    
 
    
    
    