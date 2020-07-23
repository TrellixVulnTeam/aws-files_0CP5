class Deer:
    
    sound="Buck Buck"
    
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if age_in_months >1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months=age_in_months
        self._breed=breed
        if required_food_in_kgs > 0:
            self._required_food_in_kgs=required_food_in_kgs
        else:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=2
    @classmethod    
    def make_sound(cls):
        print(cls.sound)
        
    def breathe(self):
        print("Breathe in air")
        
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
class Lion(Deer):
    
    sound="Roar Roar"
    
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if age_in_months >1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months=age_in_months
        self._breed=breed
        if required_food_in_kgs > 0:
            self._required_food_in_kgs=required_food_in_kgs
        else:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=4
        
    #def make_sound(self):
     #   print("Roar Roar")
        
    #def breathe(self):
     #   print("Breathe in air")
        
    def hunt(self,park):
        if park.count > 0:
            park.count-=1
            if park.count == 0:
                print("No deers to hunt")
                
    """@property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs"""
   
class Shark:
    
    sound="Shark Sound"
    
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if age_in_months >1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months=age_in_months
        self._breed=breed
        if required_food_in_kgs > 0:
            self._required_food_in_kgs=required_food_in_kgs
        else:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=8
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    def breathe(self):
        print("Breathe oxygen from water")
        
    def hunt(self,park):
        if park.count > 0:
            park.count-=1
            if park.count == 0:
                print("No deers to hunt")
                
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
  
  
class GoldFish(Shark):
    sound="Hum Hum"
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if age_in_months >1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months=age_in_months
        self._breed=breed
        if required_food_in_kgs > 0:
            self._required_food_in_kgs=required_food_in_kgs
        else:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=0.2
        
    #def make_sound(self):
     #   print("Hum Hum")
        
    #def breathe(self):
     #   print("Breathe oxygen from water")
        
    """@property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs"""
        
        
class Snake(Deer):
    
    sound="Hiss Hiss"
    
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if age_in_months >1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months=age_in_months
        self._breed=breed
        if required_food_in_kgs > 0:
            self._required_food_in_kgs=required_food_in_kgs
        else:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=0.5
        
    #def make_sound(self):
     #   print("Hiss Hiss")
        
    #def breathe(self):
     #   print("Breathe in air")
        
    def hunt(self,park):
        if park.count > 0:
            park.count-=1
            if park.count == 0:
                print("No deers to hunt")
                
    """@property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs"""
   
        
        
class Zoo:
    
    counter=0
    All_zoo_animals=[]
    
    def __init__(self):
        self._reserved_food_in_kgs=0
        self.count=0
        self.zoo_animals=[]
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    
    def add_food_to_reserve(self,value):
        self._reserved_food_in_kgs=value
        
    def add_animal(self,animal):
        self.zoo_animals.append(animal)
        type(self).All_zoo_animals.append(animal)
        Zoo.counter+=1
        self.count+=1
        
    def count_animals(self):
        return self.count
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return cls.counter
        
    @staticmethod
    def count_animals_in_given_zoos(list1):
        number=0
        for i in list1:
             number+=i.count_animals()
        return number
        
    def feed(self,animal):
        if self._reserved_food_in_kgs >= animal._required_food_in_kgs:
            self._reserved_food_in_kgs-=animal._required_food_in_kgs
            animal.grow()
        
    
   
    
 
        