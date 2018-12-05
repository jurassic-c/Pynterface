from events import *

class event_manager:
	event_bindings = None
	pynterface_event_bindings = None
	callback_ids = None
	max_id = 0

	def __init__(self):
		self.event_bindings = {}
		self.pynterface_event_bindings = {}
		self.callback_ids = {}
		self.bind(PYNTERFACE_EVENT, self._handle_pynterface_event)

	def bind(self, event, callback):
		self.max_id+=1
		id = self.max_id
		if not self.event_bindings.has_key(event):
			self.event_bindings[event] = {}
		self.event_bindings[event][id] = callback
		self.callback_ids[id] = event
		return id

	def bind_pynterface(self, event, callback):
		self.max_id+=1
		id = self.max_id
		if not self.pynterface_event_bindings.has_key(event):
			self.pynterface_event_bindings[event] = {}
		self.pynterface_event_bindings[event][id] = callback
		self.callback_ids[id] = event
		return id

	def _handle_pynterface_event(self, event):
		if not self.pynterface_event_bindings.has_key(event.pface_type):
			return
		for callback_id in self.pynterface_event_bindings[event.pface_type]:
			self.pynterface_event_bindings[event.pface_type][callback_id](event)
		

	def unbind(self, callback_id):
		if not self.callback_ids.has_key(callback_id):
			return
		del self.event_bindings[self.callback_ids[callback_id]][callback_id]
		del self.callback_ids[callback_id]

	def run(self, events):
		for event in events:
			if not self.event_bindings.has_key(event.type):
				continue
			for callback_id in self.event_bindings[event.type]:
				self.event_bindings[event.type][callback_id](event)
