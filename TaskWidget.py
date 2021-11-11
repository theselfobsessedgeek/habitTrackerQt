
from auth import Auth
class Task():
    def __init__(self, task_name,description,tf,uid):
        self.task_name = task_name
        self.description = description
        self.tf = tf

    def pull(uid):
        return Auth.pullInfo(uid)
        
    def push(task_name,description,tf,uid):
        return Auth.pushInfo(task_name,description,tf,uid)
        