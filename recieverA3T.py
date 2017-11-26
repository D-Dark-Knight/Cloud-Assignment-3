from azure.servicebus import ServiceBusService, Message, Queue
from multiprocessing import Pool
import thread
from azure.storage.table import TableService, Entity

from flask import Flask
app = Flask(__name__)

bus_service = ServiceBusService(
    service_namespace='batmanandrobin491fb9',
    shared_access_key_name='ross',
    shared_access_key_value='i7vczr8lLmA3XeyWEMfekhob0J3eWk09JUMv/qX2afs=')

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
	   thread.start_new_thread( hello_world, (20000,999999999) )
	   thread.start_new_thread( hello_world, (40000,999999999) )
	   thread.start_new_thread( hello_world, (60000,999999999) )
	   thread.start_new_thread( hello_world, (80000,999999999) )
	   thread.start_new_thread( hello_world, (100000,999999999) )
	   thread.start_new_thread( hello_world, (120000,999999999) )
	   thread.start_new_thread( hello_world, (120000,999999999) )
	   thread.start_new_thread( hello_world, (120000,999999999) )
	   thread.start_new_thread( hello_world, (120000,999999999) )
	   thread.start_new_thread( hello_world, (120000,999999999) )
	   thread.start_new_thread( hello_world, (120000,999999999) )
	   thread.start_new_thread( hello_world, (120000,999999999) )
	   thread.start_new_thread( hello_world, (120000,999999999) )
	   thread.start_new_thread( hello_world, (120000,999999999) )
	except:
	   print "Error: unable to start thread"
	while 1:
		app.run()
		pass

	
	
