from azure.servicebus import ServiceBusService, Message, Queue
from multiprocessing import Pool
import thread
from azure.storage.table import TableService, Entity
import json

bus_service = ServiceBusService(
    service_namespace='rossamrit',
    shared_access_key_name='RootManageSharedAccessKey',
    shared_access_key_value='WQ8H90SmQA7OZEux1jpGP7bh4gZBJuVcJzooReElV74=')

table_service = TableService(account_name='amrittable', account_key='Cgqr5ZSRv/K/9ftaeQMMHzQcEL06VlyulbDtqnXD0eb6QujMkijdYzk0m37kJaswlyyVgGd9zyPw8P0ArdZy2Q==')

msgl = ""
msgl2 = ""

def hello_world(name):
	while 1:
		try:
			msg = bus_service.receive_queue_message('ross', peek_lock=True)
			msg1 = msg.body
			msgl2 = json.loads(msg1)
			print(msgl2["UserId"])
			print(msgl2["SellerID"])
			print(msgl2["Product Name"])
			print(msgl2["Sale Price"])
			print(msgl2["Transaction Date"])
			task = {"PartitionKey"    : msgl2["TransactionID"], 
					"RowKey"          : "Anything", 
					"User_ID"         : msgl2["UserId"],
					"SellerID"        : msgl2["SellerID"] ,
					"Product Name"    : msgl2["Product Name"],
					"Sale Price"      : msgl2["Sale Price"] }
					
					
			#table_service.insert_entity('amritTable', task)
			msg.delete()
		except Exception as e:
			s = str(e)
			print(s)

		
if __name__ == '__main__':
	p = Pool(10)
	
	(p.map(hello_world, ["dummy", "dummy", "dummy","dummy","dummy","dummy","dummy","dummy","dummy","dummy"]))
	app.run()
	
