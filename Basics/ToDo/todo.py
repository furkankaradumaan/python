from datetime import date
import json

class Task:
    
    __tasks = []
    __json_name = "tasks.json"

    def __init__(self, tid: int, task:str, deadline: date, completed: bool = False):
        
        self.__tid = tid
        self.__task = task
        self.__deadline = deadline
        self.__completed = completed
    
        Task.__tasks.append(self)

    def __str__(self):
        return f"ID: {self.tid}\n \
                 Deadline: {self.deadline.strftime('%d.%m.%Y')}\n \
                 Status: {'Completed' if self.completed else 'Not completed'}\n \
                 Task: {self.task}"
    @property
    def tid(self):
        return self.__tid
    @property
    def task(self):
        return self.__task
    @property
    def deadline(self):
        return self.__deadline
    @property
    def completed(self):
        return self.__completed
        
    @task.setter
    def task(self, ntask: str):
        self.__task = ntask
        
    @deadline.setter
    def deadline(self, ndeadline: date):
        self.__deadline = ndeadline
        
    @completed.setter
    def completed(self, ncompleted: bool):
        self.__completed = ncompleted
        
    @classmethod
    def task_exists(cls, tid: int):
        for task in cls.__tasks:
            if task.tid == tid:
                return 1
        return 0
    
    @classmethod
    def update_task(cls, tid, new_task: str = None, new_deadline: date = None):
        task = cls.get_task(tid)
        if task:
            task.task = new_task if new_task else task.task
            task.deadline = new_deadline if new_deadline else task.deadline
            return 1
        return 0

    @classmethod
    def list_tasks(cls, filterfunc = None):
        for task in cls.__tasks:
            if not filterfunc or filterfunc(task):
                print(task)
                print("*" * 40)
    
    @classmethod
    def remove_task(cls, tid: int):
        task = cls.get_task(tid)
        if task:
            cls.__tasks.remove(task)
            return 1
        return 0
    
    @classmethod
    def get_task(cls, tid):
        for task in cls.__tasks:
            if task.tid == tid:
                return task

        return None

    @classmethod
    def load_from_json(cls):
        
        with open(cls.__json_name, "r") as file:
            d = json.load(file)

            for task in d["tasks"]:
                Task(task["id"], task["task"], date.fromisoformat(task["deadline"]), task["completed"])
    
    @classmethod
    def to_dict(cls, tasks):
        d = dict()
        d["tasks"] = list()

        for task in tasks:
            d_task = dict()
            d_task["id"] = task.tid
            d_task["task"] = task.task
            d_task["deadline"] = task.deadline.isoformat()
            d_task["completed"] = task.completed
            
            d["tasks"].append(d_task)

        return d 

    @classmethod
    def save_to_json(cls):

        with open(cls.__json_name, "w") as file:
            d = cls.to_dict(cls.__tasks)
            json.dump(d, file, indent=4)

    


    
    
    
    





