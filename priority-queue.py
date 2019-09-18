class PriorityQ:
    def __init__(self):
        self.__queue = []
        print('constructor')
    
    def queue_items(self):
        return self.__queue
    
    def next_in_queue(self):
        try:
            return self.__queue.pop(0) 
        except:
            raise Exception('Queue is empty')

    def __check_priority_assigned(self, q_priority):
        keys = [item[0] for item in self.__queue]
        if q_priority in keys:
           return True
        else:
           return False
       
    def __current_q_item_index(self, q_priority):
        keys = [item[0] for item in self.__queue]
        print(keys)
        if q_priority in keys:
           return keys.index(q_priority)
       
    def add_to_queue(self, q_item):
        if self.__check_priority_assigned(q_item[0]):
            raise Exception('Prioriy {0} is already used'.format(q_item[0]))
        self.__queue.append(q_item)
        self.__queue = sorted(self.__queue, key= lambda item: item[0])

    def add_to_queue_and_update(self, current_priority, q_item):
        print(self.__queue)
        q_index = self.__current_q_item_index(current_priority)
        updated_q_item = (current_priority, q_item[1])
        print(updated_q_item)
        if q_index == 0:
            self.__queue.insert(0, updated_q_item)
        else:
            self.__queue.insert(q_index - 1, updated_q_item)
        for i in range(q_index+1, len(self.__queue)):
            print(i)
            priority = self.__queue[i][0]
            record = self.__queue[i][1]
            print(record)
            self.__queue[i] = (priority+1, record)
        self.__queue = sorted(self.__queue, key= lambda item: item[0])
        
q = PriorityQ()
q.add_to_queue((0, 'cat'))
q.add_to_queue((1, 'dog'))
q.add_to_queue((2, 'bat'))
q.add_to_queue((3, 'elephant'))
q.add_to_queue_and_update(2, (0, 'fish'))
print(q.queue_items())

