# -*- coding=utf-8 -*-

from ctypes import c_char


#传输数据的编码格式
UTF_8    =6000
GB2312   =6001


#发送给监控器的指令类型
#SERVER_SYSTEM_RESTART 			  =  8000    
#SERVER_SYSTEM_FULLMEMORY 		  =  8001
#SERVER_TRADER_NOMONEY 		          =  8002
#SERVER_TRADER_FULLMONEY			  =  8003
#SERVER_TRADER_INSERTORDER 		  =  8004
#SERVER_TRADER_DELETEORDER	          =  8005

#从监控器接收到的指令类型
#MONITOR_SYSTEM_RESTART 		          = 9001
#MONITOR_SYSTEM_RESTARTAPP		  = 9002
#MONITOR_TRADER_CLOSEALLPOSITION 	  = 9003
#MONITOR_TRADER_ABITIONOPEN 		  = 9004
#MONITOR_TRADER_CLOSEMARKED 		  = 9005



QL_ADMIN                                  =1
QL_USER                                   =2
QL_GUEST                                  =3


# Direction or bsflag
QL_D_Buy 					= c_char('0')	# 买
QL_D_Sell 					= c_char('1')	# 卖



# offsetFlag
QL_OF_Open 					= c_char('0')	# 开仓
QL_OF_Close  				= c_char('1')	# 平仓
QL_OF_ForceClose 			= c_char('2')	# 强平
QL_OF_CloseToday 			= c_char('3')	# 平今
QL_OF_CloseYesterday 		= c_char('4')	# 平昨
QL_OF_ForceOff 				= c_char('5')	# 强减
QL_OF_LocalForceClose 		= c_char('6')	# 本地强平


# price type
QL_OPT_AnyPrice  				= c_char('1')	# 任意价
QL_OPT_LimitPrice  				= c_char('2')	# 限价
QL_OPT_BestPrice  				= c_char('3')	# 最优价
QL_OPT_LastPrice  				= c_char('4')	# 最新价
QL_OPT_LastPricePlusOneTicks  	= c_char('5')	# 最新价浮动上浮1个ticks
QL_OPT_LastPricePlusTwoTicks  	= c_char('6')	# 最新价浮动上浮2个ticks
QL_OPT_LastPricePlusThreeTicks  = c_char('7')	# 最新价浮动上浮3个ticks
QL_OPT_AskPrice1  				= c_char('8')	# 卖一价
QL_OPT_AskPrice1PlusOneTicks  	= c_char('9')	# 卖一价浮动上浮1个ticks
QL_OPT_AskPrice1PlusTwoTicks  	= c_char('A')	# 卖一价浮动上浮2个ticks
QL_OPT_AskPrice1PlusThreeTicks  = c_char('B')	# 卖一价浮动上浮3个ticks
QL_OPT_BidPrice1  				= c_char('C')	# 买一价
QL_OPT_BidPrice1PlusOneTicks  	= c_char('D')	# 买一价浮动上浮1个ticks
QL_OPT_BidPrice1PlusTwoTicks  	= c_char('E')	# 买一价浮动上浮2个ticks
QL_OPT_BidPrice1PlusThreeTicks  = c_char('F')	# 买一价浮动上浮3个ticks


QL_Dynamic					= 1	# 动态止损
QL_Static   				        = 2	# 静态止损





QL_POSITION_Sell_Today               =9001  # 今日空单
QL_POSITION_Buy_Today                =9002  # 今日多单
QL_POSITION_Sell_History             =9003  # 非今日空单
QL_POSITION_Buy_History              =9004  # 非今日多单
QL_POSITION_Sell_All                 =9005  # 空单总计
QL_POSITION_Buy_All                  =9006  # 多单总计
