from azure.servicebus import ServiceBusService, Message, Queue
from multiprocessing import Pool

from flask import Flask
app = Flask(__name__)

bus_service = ServiceBusService(
    service_namespace='batmanandrobin491fb9',
    shared_access_key_name='assignment3',
    shared_access_key_value='AHQLYr22ggrKjA8JNUJpQpDyQYQuXxj7lZY/yrDVxKI=')

	
@app.route('/')
def hello_world(i):
	m =  600000/9
	while (i < m): 
		msg = Message(b'Test!')
		bus_service.send_queue_message('assignment3', msg)
		i = i+1
	return "finished"	
		
if __name__ == '__main__':
	p = Pool(40)
	(p.map(hello_world, [1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
	app.run()