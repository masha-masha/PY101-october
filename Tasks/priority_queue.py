"""
Priority Queue

Queue priorities are from 0 to 5
"""

Queue=[[],[],[],[],[]]
def enqueue(elem, priority: int = 0) -> None:
	global Queue
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	if priority < 5:
		Queue[priority].append(elem)
	return None


def dequeue():
	global Queue
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	i=0
	while len(Queue[i])<1:
		i+=1
		if i==5:
			break
	if i<5:
		deq=Queue[i][0]
		Queue[i]=Queue[i][1:]
		return deq
	else:
		return None


def peek(ind: int = 0, priority: int = 0):
	global Queue
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	step=0
	i=0
	j=0
	while step<ind and i<5:
		step+=1
		if j<len(Queue[i]):
			j+=1
		else:
			i+=1
	if i==5:
		return None
	else:
		return Queue[i][j]


def clear() -> None:
	global Queue
	"""
	Clear my queue

	:return: None
	"""
	Queue = [[], [], [], [], []]
	return None
