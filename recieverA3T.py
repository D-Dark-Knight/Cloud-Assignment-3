from azure.servicebus import ServiceBusService, Message, Queue
from multiprocessing import Pool
import thread
from azure.storage.table import TableService, Entity

from flask import Flask
app = Flask(__name__)

bus_service = ServiceBusService(
    service_namespace='batmanandrobin491fb9',
    shared_access_key_name='assignment3',
    shared_access_key_value='AHQLYr22ggrKjA8JNUJpQpDyQYQuXxj7lZY/yrDVxKI=')

table_service = TableService(account_name='batmanandrobin491fb9', account_key='MPsdcQOiLZewcUIYHYtPkjRDtKrzHRq7Z/AVkIt9Zo6IvQP2/Zff4a19GXOwI4MIxOLvQ00lCIwo/lkqml4jbw==')

@app.route('/')
def hello_world(i,j ):
	while (i < j): 
		msg = bus_service.receive_queue_message('assignment3', peek_lock=True)
		print(msg.body)
		task = {'PartitionKey': "1", 'RowKey': str(i), 'description' : msg.body, 'priority' : 200}
		table_service.insert_entity('assignment3', task)
		msg.delete()
		i = i +1
	return "finished"	
		
if __name__ == '__main__':
	try:
	   thread.start_new_thread( hello_world, (0,19999) )
	   thread.start_new_thread( hello_world, (20000,39999) )
	   thread.start_new_thread( hello_world, (40000,59999) )
	   thread.start_new_thread( hello_world, (60000,79999) )
	   thread.start_new_thread( hello_world, (80000,99999) )
	   thread.start_new_thread( hello_world, (100000,119999) )
	   thread.start_new_thread( hello_world, (120000,139999) )
	except:
	   print "Error: unable to start thread"
	while 1:
		app.run()
		pass

	