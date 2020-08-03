from notify_run import Notify

def send_notification(msg):
	notifiy = Notify()
	notifiy.send(msg)