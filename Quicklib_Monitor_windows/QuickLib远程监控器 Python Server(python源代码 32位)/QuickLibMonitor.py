# -*- coding=utf-8 -*-

from ctypes import *
from QuickLibMonitorType import *
import time


class QuickLibMonitor(object):
	savecharset=UTF_8
	def __init__(self):
		self.d2 = CDLL('QuickLibMonitor.dll')
		
		'''
		self.fLogin = self.d2.Login
		self.fLogin.argtypes = []
		self.fLogin.restype = c_int32
		
		self.fInsertOrder = self.d2.InsertOrder
		self.fInsertOrder.argtypes = [c_char_p, c_char, c_char,c_char, c_double, c_int32]
		self.fInsertOrder.restype = c_int32

		self.fDeleteOrder = self.d2.DeleteOrder
		self.fDeleteOrder.argtypes = [c_char_p, c_int32]
		self.fDeleteOrder.restype = c_int32

		self.fQryTradedVol = self.d2.QryTradedVol
		self.fQryTradedVol.argtypes = [c_int32]
		self.fQryTradedVol.restype = c_int32
		
		self.fQryPosition = self.d2.QryPosition
		self.fQryPosition.argtypes = [c_char_p,c_int32]
		self.fQryPosition.restype = c_int32		
		
		self.fQryPositionList = self.d2.QryPositionList
		self.fQryPositionList.argtypes = [c_int32]
		self.fQryPositionList.restype = c_void_p
		
		self.fQryBalance = self.d2.QryBalance
		self.fQryBalance.argtypes = [c_bool]
		self.fQryBalance.restype = c_double	
		
		self.fQryAvailable = self.d2.QryAvailable
		self.fQryAvailable.argtypes = []
		self.fQryAvailable.restype = c_double
		
		self.fSetShowPosition = self.d2.SetShowPosition
		self.fSetShowPosition.argtypes = [c_bool]
		self.fSetShowPosition.restype = c_void_p	
		
		'''
		#增加用户
		self.fAddUser = self.d2.AddUser
		self.fAddUser.argtypes = [c_char_p,c_char_p,c_int32,c_int32]
		self.fAddUser.restype = c_int32			
		
		
		#服务器启动
		self.fOnStart = self.d2.OnStart
		self.fOnStart.argtypes = [c_char_p,c_char_p,c_int32]
		self.fOnStart.restype = c_int32	
		
		#服务器启动
		self.fOnStart_U = self.d2.OnStart_U
		self.fOnStart_Uargtypes = [c_char_p,c_char_p,c_int32]
		self.fOnStart_U.restype = c_int32			
		
		#服务器发送数据到监控端
		self.fOnSend = self.d2.OnSend
		self.fOnSend.argtypes = [c_int32,c_char_p,c_int32,c_double,c_char_p,c_char_p,c_char_p]
		self.fOnSend.restype = c_int32	
		
		#服务器发送数据到监控端
		self.fOnSend_U = self.d2.OnSend_U
		self.fOnSend_U.argtypes = [c_int32,c_char_p,c_int32,c_double,c_char_p,c_char_p,c_char_p]
		self.fOnSend_U.restype = c_int32			
 
		#服务器停止
		self.fOnStop = self.d2.OnStart
		self.fOnStop.argtypes = []
		self.fOnStop.restype = c_int32			
		
		 
		#服务器与监控器断开连接
		self.fOnDisconnect = self.d2.OnStart
		self.fOnDisconnect.argtypes = []
		self.fOnDisconnect.restype = c_int32		
		
		
		#检查未处理的指令数量
		self.fGetCmdSize = self.d2.GetCmdSize
		self.fGetCmdSize.argtypes = []
		self.fGetCmdSize.restype = c_int32		
				
		#获得新指令
		self.fGetCmd = self.d2.GetCmd
		self.fGetCmd.argtypes = []
		self.fGetCmd.restype = c_int32		
		
		#获得新指令		
		self.fOnCmd = self.d2.OnCmd
		self.fOnCmd.argtypes = []
		self.fOnCmd.restype = c_int32
		
		#登录成功		
		self.fGetCmd_LoginScuess = self.d2.GetCmd_LoginScuess
		self.fGetCmd_LoginScuess.argtypes = []
		self.fGetCmd_LoginScuess.restype = c_void_p
		
		#登出成功
		self.fGetCmd_LoginOut = self.d2.GetCmd_LoginOut
		self.fGetCmd_LoginOut.argtypes = []
		self.fGetCmd_LoginOut.restype = c_void_p		
	'''
		
	def Login(self):
		return self.fLogin()

	def InsertOrder(self, instrumentID, direction, offsetFlag, priceType, price, num):
		return self.fInsertOrder(instrumentID, direction, offsetFlag, priceType,c_double(price), c_int32(num))
								 

	def DeleteOrder(self, instrumentID, orderRef):
		return self.fDeleteOrder(instrumentID, orderRef)

	def QryTradedVol(self, orderRef):
		return self.fQryTradedVol(orderRef)
	
	#查询品种持仓
	def QryPosition(self, instrumentID,positiontype):
		return self.fQryPosition(instrumentID,positiontype)
	
	#查询持仓列表
	def QryPositionList(self, orderRef):
		return self.fQryPositionList(orderRef)


        #查询权益   BalanceType=True动态权益    BalanceType=False静态权益
	def QryBalance(self, BalanceType):
		return self.fQryBalance(BalanceType)
	
	#查询可用资金
	def QryAvailable(self):
		return self.fQryAvailable()
			
	#设置更新持仓数据时显示,仅对控制台有效
	def SetShowPosition(self,showstate):
		self.fSetShowPosition(showstate)

	'''
	#开启与监控器的数据同步服务
	def AddUser(self, username,password,usertype,charset):
		global savecharset
		savecharset=charset
		if savecharset==UTF_8:
			self.fAddUser_U(username,password,usertype,charset)
		else:
			self.fAddUser(username,password,usertype,charset)
			
			
	#开启与监控器的数据同步服务
	def OnStart(self, username,password,usertype,charset):
		global savecharset
		savecharset=charset
		if savecharset==UTF_8:
			self.fOnStart_U(username,password,usertype)
		else:
			self.fOnStart(username,password,usertype)
		   
        #发送指令数据至监控器
	def OnSend(self, cmdtype,instrument,volue,price,strategyid,remark1,remark2):
		global savecharset
		if savecharset==UTF_8:
			self.fOnSend_U(cmdtype,instrument,volue,price,strategyid,remark1,remark2)
		else:
			self.fOnSend(cmdtype,instrument,volue,price,strategyid,remark1,remark2)
		   
		#self.fOnSend(cmdtype)
        #关闭与监控器的数据同步服务
	def OnStop(self):
		self.fOnStop()
		
	#关闭与监控器的数据同步服务
	def OnDisconnect(self):
		self.fOnDisconnect()
		
	#获取新的监控器发来的指令
	def GetCmdSize(self):
		self.fGetCmdSize()	 		
		
	#获取新的监控器发来的指令
	def GetCmd(self):
		return self.fGetCmd()
	
	
	def OnCmd(self):
		return self.fOnCmd()
	
	def GetCmd_LoginScuess(self):
		#登录成功回调
		return self.fGetCmd_LoginScuess()
	
	def GetCmd_LoginOut(self):
		#登出成功回调
		return self.fGetCmd_LoginOut()	
	