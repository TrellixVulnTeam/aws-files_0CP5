class Deer:
    
    sound="Buck Buck"
    breath="Breathe in air"
    
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
            
        self.age_in_months_increases=1
        self.required_food_in_kgs_increases=2
        
    def grow(self):
        self._age_in_months+=self.age_in_months_increases
        self._required_food_in_kgs+=self.required_food_in_kgs_increases
        
    @classmethod    
    def make_sound(cls):
        print(cls.sound)
        
    @classmethod
    def breathe(cls):
        print(cls.breath)


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
        super().__init__(age_in_months,breed,required_food_in_kgs)
        
        self.age_in_months_increases=1
        self.required_food_in_kgs_increases=4
        
    
        
    def hunt(self,zoo_park):
        if zoo_park.deer_count > 0:
            Zoo.count_all_animals -=1
            zoo_park.count_zoo_animals -= 1
            zoo_park.deer_count -= 1
            #if zoo_park.deer_count == 0:
        else:    
            print("No deers to hunt")

class Snake(Deer):
    
    sound="Hiss Hiss"
    
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)
        
        self.age_in_months_increases=1
        self.required_food_in_kgs_increases=0.5
        
    def hunt(self,zoo_park):
        if zoo_park.deer_count > 0:
            Zoo.count_all_animals -=1
            zoo_park.count_zoo_animals -= 1
            zoo_park.deer_count -= 1
            #if zoo_park.deer_count == 0:
        else:    
            print("No deers to hunt")
        
    

class Shark:
    
    sound="Shark Sound"
    breath="Breathe oxygen from water"
    
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if age_in_months > 1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months=age_in_months
        self._breed=breed
        if required_food_in_kgs > 0:
            self._required_food_in_kgs=required_food_in_kgs
        else:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
            
        self.age_in_months_increases=1
        self.required_food_in_kgs_increases=8
        
    def grow(self):
        self._age_in_months+=self.age_in_months_increases
        self._required_food_in_kgs+=self.required_food_in_kgs_increases
        
    @classmethod    
    def make_sound(cls):
        print(cls.sound)
        
    @classmethod
    def breathe(cls):
        print(cls.breath)
        
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def breed(self):
        return self._breed
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
    def hunt(self,zoo_park):
        if zoo_park.gold_fish_count > 0:
            Zoo.count_all_animals -=1
            zoo_park.count_zoo_animals -= 1
            zoo_park.gold_fish_count -= 1
            #if zoo_park.gold_fish_count == 0:
        else:    
            print("No GoldFish to hunt")
      

class GoldFish(Shark):
    
    sound="Hum Hum"
    
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)
        
        self.age_in_months_increases=1
        self.required_food_in_kgs_increases=0.2

class Zoo:
    
    #all_animals=[]
    count_all_animals=0
    
    def __init__(self):
        self._reserved_food_in_kgs=0
        
        self.count_zoo_animals=0
        #self.zoo_animals=[]
        self.deer_count=0
        self.gold_fish_count=0
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    def add_food_to_reserve(self,value):
        self._reserved_food_in_kgs=value
        
    def add_animal(self,animal):
        if type(animal) == Deer :
            self.deer_count += 1
        elif type(animal) == GoldFish :
            self.gold_fish_count += 1
        #self.zoo_animals.append(animal)
        #type(self).all_animals.append(animal)
        self.count_zoo_animals+=1
        Zoo.count_all_animals+=1
        
    def feed(self,animal):
        if self._reserved_food_in_kgs >= animal._required_food_in_kgs:
            self._reserved_food_in_kgs-=animal._required_food_in_kgs
            animal.grow()
        
    def count_animals(self):
        return self.count_zoo_animals
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return cls.count_all_animals
        
    @staticmethod
    def count_animals_in_given_zoos(list1):
        number=0
        for i in list1:
             number+=i.count_animals()
        return number
        