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
	   thread.start_new_thread( hello_world, (0,30000) )
	   thread.start_new_thread( hello_world, (30001,60000) )
	   thread.start_new_thread( hello_world, (60001,90000) )
	   thread.start_new_thread( hello_world, (90001,120000) )
	   thread.start_new_thread( hello_world, (120001,150000) )
	   thread.start_new_thread( hello_world, (150001,180000) )
	   thread.start_new_thread( hello_world, (180001,210000) )
	   thread.start_new_thread( hello_world, (210001,240000) )
	   thread.start_new_thread( hello_world, (240001,270000) )
	   thread.start_new_thread( hello_world, (270001,300000) )
	   thread.start_new_thread( hello_world, (300001,330000) )
	   thread.start_new_thread( hello_world, (330001,360000) )
	   thread.start_new_thread( hello_world, (360001,390000) )
	   thread.start_new_thread( hello_world, (390001,420000) )
	   thread.start_new_thread( hello_world, (420001,450000) )
	   thread.start_new_thread( hello_world, (450001,480000) )
	   thread.start_new_thread( hello_world, (480001,510000) )
	   thread.start_new_thread( hello_world, (510001,540000) )
	   thread.start_new_thread( hello_world, (540001,570000) )
	   thread.start_new_thread( hello_world, (570001,600000) )
	except:
	   print "Error: unable to start thread"
	while 1:
		app.run()
		pass

	
