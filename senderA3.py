from azure.servicebus import ServiceBusService, Message, Queue
from multiprocessing import Pool
import json
from random import randint
import datetime
from flask import Flask
app = Flask(__name__)

bus_service = ServiceBusService(
    service_namespace='rossamrit',
    shared_access_key_name='RootManageSharedAccessKey',
    shared_access_key_value='WQ8H90SmQA7OZEux1jpGP7bh4gZBJuVcJzooReElV74=')

@app.route('/')
def hello_world(i):
	m =  i+14999
	while (i < m): 
		msg = {
			"TransactionID": str(i),
			"UserId":"A1",
			"SellerID":"S1",
			"Product Name":"Financial Trap",
			"Sale Price":500,
			"Transaction Date": datetime.date.today().strftime("%B %d, %Y")
		}
		
		msg1 = json.dumps(msg)
		msg1 = Message(msg1)
		#parsed_json = json.loads(list[num])
		#msg = Message(parsed_json)
		bus_service.send_queue_message('ross', msg1)
		i = i+1
	return "finished"	
		
if __name__ == '__main__':
	p = Pool(40)
	
	(p.map(hello_world, [1, 15001, 30001,45001,60001,75001,90001,105001,120001,135001,150001,165001,180001,195001,210001,225001,140001,155001,170001,185001,300001,315001,330001,345001,360001,385001,400001,415001,430001,445001,460001,475001,490001,505001,520001,535001,550001,565001,580001,595001]))
	app.run()
