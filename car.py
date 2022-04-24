class Car(object):
  
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.comapany=company
        self.speed_limit=speed_limit
        self.model=model
    
    def start(self):
        print("started")

    def stop(self):
        print("stop")
    
    def Change_gear(self,gear_type):
        print("gear Changed")
        "gear realted functionality here"
    
supra=Car("mk5","midnight Black","toyota", 245)
print(supra.Change_gear(supra,gear_type="8 liter"))
supra.color
