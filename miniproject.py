# note to myself : mini project hard coded -> create mapping later if have time and refactor the code, do other exception handling later 
from enum import Enum

#classes and enums
class Status(Enum):
    AVAIL = 1
    HIRED = 2

class Facility(Enum):
    AC = 1
    NON_AC = 2

class MaxSeats(Enum):
    THREE = 3
    FOUR = 4
    SIX = 6
    EIGHT = 8

class Size(Enum):
    SEVEN = 7
    TWELVE = 12

class Load(Enum):
    TWOFIVE = 2500
    THREEFIVE = 3500

class Queue():
    def __init__(self):
        self._data=[]

    def add(self,data):
        self._data.append(data)

    def is_empty(self):
        self._length = len(self._data)
        if self._length == 0:
            return True
        else:
            return False
        
    def get(self):
        if (self.is_empty()):
            print('empty queue')
        else:
            return self._data.pop(0)

    def display(self):
        if (self.is_empty()):
            print('empty queue')
        else:
            for data in self._data:
                print(data.getVehicleNo())

    def remove(self, data):
        self._index = 0
        if (self.is_empty(self)):
            print('empty queue')
        else:
            for d in self._data:
                if d.getVehicleNo() == data:
                    self._data.pop(self._index)
                else:
                    self._index += 1
          
        
                   
class Vehicle():
    def __init__(self, vehicleNo, vehicleDriver):
        self.__vehicleNo = vehicleNo
        self.__vehicleDriver = vehicleDriver
        self.__status = Status.AVAIL
   
    def addJob(self):
        self.__status = Status.HIRED
        return self.__status

    def releaseJob(self):
        self.__status = Status.AVAIL
        return self.__status

    def getVehicleNo(self):
        return self.__vehicleNo

    def getVehicleDriver(self):
        return self.__vehicleDriver

    def getStatus(self):
        return self.__status

class Car(Vehicle):
    def __init__(self, vehicleNo, vehicleDriver, maxSeats, facility):
        super().__init__(vehicleNo, vehicleDriver)
        if maxSeats == 3:
            self.__maxSeats = MaxSeats.THREE
        elif maxSeats == 4:
            self.__maxSeats = MaxSeats.FOUR
        else:
            raise ValueError('Seats values are not available')

        if facility == 'AC':
            self.__facility = Facility.AC
        else:
            self.__facility = Facility.NON_AC
      
        
    def getMaxSeats(self):
        return self.__maxSeats

    def getFacility(self):
        return self.__facility

class Van(Vehicle):
    def __init__(self, vehicleNo, vehicleDriver, maxSeats, facility):
        super().__init__(vehicleNo, vehicleDriver)
        if maxSeats == 6:
            self.__maxSeats = MaxSeats.SIX
        elif maxSeats == 8:
            self.__maxSeats = MaxSeats.EIGHT
        else:
            raise ValueError('Seats values are not available')

        if facility == 'AC':
            self.__facility = Facility.AC
        else:
            self.__facility = Facility.NON_AC
        
     
    def getMaxSeats(self):
        return self.__maxSeats

    def getFacility(self):
        return self.__facility


class ThreeWheeler(Vehicle):
    def __init__(self, vehicleNo, vehicleDriver, maxSeats):
        super().__init__(vehicleNo, vehicleDriver)
        if maxSeats == 3:
            self.__maxSeats = MaxSeats.THREE
        else:
            raise ValueError('Seats values are not available')

    def getMaxSeats(self):
        return self.__maxSeats

class Truck(Vehicle):
    def __init__(self, vehicleNo, vehicleDriver, size):
        super().__init__(vehicleNo, vehicleDriver)
        if size == 7:
            self.__size = Size.SEVEN
        elif size == 12:
            self.__size = Size.TWELVE
        else:
            raise ValueError('Seats values are not available')

    def getSize(self):
        return self.__size

class Lorry(Vehicle):
    def __init__(self, vehicleNo, vehicleDriver, load):
        super().__init__(vehicleNo, vehicleDriver)
        if load == 2500:
            self.__load = Load.TWOFIVE
        elif size == 3500:
            self.__load = Load.THREEFIVE
        else:
            raise ValueError('Seats values are not available')

    def getLoad(self):
        return self.__load
#datas -> try later with a json file
vehicles = []
obj = Van('NM 2345','Dasun', 6, 'AC')
vehicles.append(obj)
obj = Car('CAR 0001','Dasun', 3, 'AC')
vehicles.append(obj)

def update():
    global available,car1,car2,car3,car4,van1,van2,van3,van4,threeWheel,truck1,truck2,lorry1,lorry2
    available = Queue()
    car1 = Queue()
    car2 = Queue()
    car3 = Queue()
    car4 = Queue()
    van1 = Queue()
    van2 = Queue()
    van3 = Queue()
    van4 = Queue()
    threeWheel = Queue()
    truck1 = Queue()
    truck2 = Queue()
    lorry1 = Queue()
    lorry2 = Queue()
    

    for vehicle in vehicles:
        if vehicle.getStatus().name == 'AVAIL':
            
            if type(vehicle) is Car and vehicle.getMaxSeats().value == 3 and vehicle.getFacility().value == 1:
                car1.add(vehicle)
            elif type(vehicle) is Car and vehicle.getMaxSeats().value == 3 and vehicle.getFacility().value == 2:
                car2.add(vehicle)
            elif type(vehicle) is Car and vehicle.getMaxSeats().value == 4 and vehicle.getFacility().value == 1:
                car3.add(vehicle)
            elif type(vehicle) is Car and vehicle.getMaxSeats().value == 4 and vehicle.getFacility().value == 2:
                car4.add(vehicle)
            elif type(vehicle) is Van and vehicle.getMaxSeats().value == 6 and vehicle.getFacility().value == 1:
                van1.add(vehicle)
            elif type(vehicle) is Van and vehicle.getMaxSeats().value == 6 and vehicle.getFacility().value == 2:
                van2.add(vehicle)
            elif type(vehicle) is Van and vehicle.getMaxSeats().value == 8 and vehicle.getFacility().value == 1:
                van3.add(vehicle)
            elif type(vehicle) is Van and vehicle.getMaxSeats().value == 8 and vehicle.getFacility().value == 2:
                van4.add(vehicle)
            elif type(vehicle) is ThreeWheeler:
                threeWheel.add(vehicle)
            elif type(vehicle) is Truck and vehicle.getSize().value == 7:
                truck1.add(vehicle)
            elif type(vehicle) is Truck and vehicle.getSize().value == 12:
                truck2.add(vehicle)
            elif type(vehicle) is Lorry and vehicle.getLoad().value == 2500:
                lorry1.add(vehicle)
            elif type(vehicle) is Lorry and vehicle.getLoad().value == 3500:
                lorry2.add(vehicle)
            else:
                available.add(vehicle)
update()
def checkAdd(vehicle):
    if type(vehicle) is Car and vehicle.getMaxSeats().value == 3 and vehicle.getFacility().value == 1:
        car1.add(vehicle)
    elif type(vehicle) is Car and vehicle.getMaxSeats().value == 3 and vehicle.getFacility().value == 2:
        car2.add(vehicle)
    elif type(vehicle) is Car and vehicle.getMaxSeats().value == 4 and vehicle.getFacility().value == 1:
        car3.add(vehicle)
    elif type(vehicle) is Car and vehicle.getMaxSeats().value == 4 and vehicle.getFacility().value == 2:
        car4.add(vehicle)
    elif type(vehicle) is Van and vehicle.getMaxSeats().value == 6 and vehicle.getFacility().value == 1:
        van1.add(vehicle)
    elif type(vehicle) is Van and vehicle.getMaxSeats().value == 6 and vehicle.getFacility().value == 2:
        van2.add(vehicle)
    elif type(vehicle) is Van and vehicle.getMaxSeats().value == 8 and vehicle.getFacility().value == 1:
        van3.add(vehicle)
    elif type(vehicle) is Van and vehicle.getMaxSeats().value == 8 and vehicle.getFacility().value == 2:
        van4.add(vehicle)
    elif type(vehicle) is ThreeWheeler:
        threeWheel.add(vehicle)
    elif type(vehicle) is Truck and vehicle.getSize().value == 7:
        truck1.add(vehicle)
    elif type(vehicle) is Truck and vehicle.getSize().value == 12:
        truck2.add(vehicle)
    elif type(vehicle) is Lorry and vehicle.getLoad().value == 2500:
        lorry1.add(vehicle)
    elif type(vehicle) is Lorry and vehicle.getLoad().value == 3500:
        lorry2.add(vehicle)
    else:
        available.add(vehicle)

def checkRemove(vehicle,num):
    if type(vehicle) is Car and vehicle.getMaxSeats().value == 3 and vehicle.getFacility().value == 1:
        car1.remove(num)
    elif type(vehicle) is Car and vehicle.getMaxSeats().value == 3 and vehicle.getFacility().value == 2:
        car2.remove(num)
    elif type(vehicle) is Car and vehicle.getMaxSeats().value == 4 and vehicle.getFacility().value == 1:
        car3.remove(num)
    elif type(vehicle) is Car and vehicle.getMaxSeats().value == 4 and vehicle.getFacility().value == 2:
        car4.remove(num)
    elif type(vehicle) is Van and vehicle.getMaxSeats().value == 6 and vehicle.getFacility().value == 1:
        van1.remove(num)
    elif type(vehicle) is Van and vehicle.getMaxSeats().value == 6 and vehicle.getFacility().value == 2:
        van2.remove(num)
    elif type(vehicle) is Van and vehicle.getMaxSeats().value == 8 and vehicle.getFacility().value == 1:
        van3.add(vehicle)
    elif type(vehicle) is Van and vehicle.getMaxSeats().value == 8 and vehicle.getFacility().value == 2:
        van4.remove(num)
    elif type(vehicle) is ThreeWheeler:
        threeWheel.remove(num)
    elif type(vehicle) is Truck and vehicle.getSize().value == 7:
        truck1.remove(num)
    elif type(vehicle) is Truck and vehicle.getSize().value == 12:
        truck2.remove(num)
    elif type(vehicle) is Lorry and vehicle.getLoad().value == 2500:
        lorry1.remove(num)
    elif type(vehicle) is Lorry and vehicle.getLoad().value == 3500:
        lorry2.remove(num)
    else:
        available.remove(num)

#functions
def display():
    update()
    view = input('View available : (cars/vans/3wheels/trucks/lorries)')
    if view == 'cars':
        print('3seats and AC : car1')
        print('3seats and NONAC : car2')
        print('4seats and AC : car3')
        print('4seats and NONAC : car4')
        choice = input('car1/car2/car3/car4 : ')
        if choice == 'car1':
            car1.display()
        elif choice == 'car2':
            car2.display()
        elif choice == 'car3':
            car3.display()
        elif choice == 'car4':
            car4.display()
        else:
            print('invalid')
    elif view == 'vans':
        print('6seats and AC : van1')
        print('6seats and NONAC : van2')
        print('8seats and AC : van3')
        print('8seats and NONAC : van4')
        choice = input('van1/van2/van3/van4 : ')
        if choice == 'van1':
            van1.display()
        elif choice == 'van2':
            van2.display()
        elif choice == 'van3':
            van3.display()
        elif choice == 'van4':
            van4.display()
        else:
            print('invalid')
    elif view == '3wheels':
        threeWheel.display()
    elif view == 'trucks':
        print('size = 7ft : truck1')
        print('size = 12ft : truck2')
        choice = input('truck1/truck2 : ')
        if choice == 'truck1':
            truck1.display()
        elif choice == 'truck2':
            truck2.display()
        else:
            print('invalid')
    elif view == 'lorries':
        print('load = 2500kg : lorry1')
        print('load = 3500kg : lorry2')
        choice = input('lorry1/lorry2 : ')
        if choice == 'lorry1':
            lorry1.display()
        elif choice == 'lorry2':
            lorry2.display()
        else:
            print('invalid')
    else:
        print('invalid')
    
def setHire():
    #try direct setting up obj later
    vehicleType = input('Enter the type of veihcle you want to hire : (Car/Van/Three Wheel/Truck/Lorry):')
    #Car
    if vehicleType == 'b':
        return -1
    elif vehicleType.capitalize() == 'Car':
        maxSeat = input('Select Car with 3 seats or 4 seats: (3/4) :')
        facility = input('Select Car Facility : (AC/NON AC):')
        try:
            if maxSeat == '3' and facility == 'AC':
                queue = car1
                currentVehicle = car1.get()
                print('You have hired : ' + currentVehicle.getVehicleNo())
                currentVehicle.addJob()
            elif maxSeat == '4' and facility == 'AC':
                queue = car3
                currentVehicle = car3.get()
                print('You have hired : ' + currentVehicle.getVehicleNo())
                currentVehicle.addJob()
            elif maxSeat == '3' and facility == 'NON AC' or 'NON_AC':
                queue = car2
                currentVehicle = car2.get()
                print('You have hired : ' + currentVehicle.getVehicleNo())
                currentVehicle.addJob()
            elif maxSeat == '4' and facility == 'NON AC' or 'NON_AC':
                queue = car4
                currentVehicle = car4.get()
                print('You have hired : ' + currentVehicle.getVehicleNo())
                currentVehicle.addJob()
        except:
            print('try later or try another vehicle')
            return -1
    #Van
    elif vehicleType.capitalize() == 'Van':
        maxSeat = input('Select Van with 6 seats or 8 seats: (6/8) :')
        facility = input('Select Van Facility : (AC/NON AC):')
        try:
            if maxSeat == '6' and facility == 'AC':
                queue = van1
                currentVehicle = van1.get()
                print(currentVehicle.getVehicleNo())
                print('You have hired : ' + currentVehicle.getVehicleNo())
                currentVehicle.addJob()
            elif maxSeat == '8' and facility == 'AC':
                queue = van3
                currentVehicle = van3.get()
                print('You have hired : ' + currentVehicle.getVehicleNo())
                currentVehicle.addJob()
            elif maxSeat == '6' and facility == 'NON AC' or 'NON_AC':
                queue = van2
                currentVehicle = van2.get()
                print('You have hired : ' + currentVehicle.getVehicleNo())
                currentVehicle.addJob()
            elif maxSeat == '8' and facility == 'NON AC' or 'NON_AC':
                queue = van4
                currentVehicle = van4.get()
                print('You have hired : ' + currentVehicle.getVehicleNo())
                currentVehicle.addJob()
        except:
            print('try later or try another vehicle')
            return -1
            
    #3wheel
    elif vehicleType.capitalize() == 'Three Wheel':
        try:
            queue = threeWheel
            currentVehicle = threeWheel.get()
            print('You have hired : ' + currentVehicle.getVehicleNo())
            currentVehicle.addJob()
        except:
            print('try later or try another vehicle')
            return -1
    #Truck
    elif vehicleType.capitalize() == 'Truck':
        size = input('Select Truck size : (7/12):')
        try:
            if size == '7':
                queue = truck1
                currentVehicle = truck1.get()
                print('You have hired : ' + currentVehicle.getVehicleNo())
                currentVehicle.addJob()
            elif size == '7':
                queue = truck2
                currentVehicle = truck2.get()
                print('You have hired : ' + currentVehicle.getVehicleNo())
                currentVehicle.addJob()
        except:
            print('try later or try another vehicle')
            return -1
    #Lorry
    elif vehicleType.capitalize() == 'Lorry':
        load = input('Select looad in Kg : (2500/3500):')
        try:
            if load == '2500':
                queue = lorry1
                currentVehicle = lorry1.get()
                print('You have hired : ' + currentVehicle.getVehicleNo())
            elif load == '3500':
                queue = lorry2
                currentVehicle = lorry2.get()
                print('You have hired : ' + currentVehicle.getVehicleNo())
                currentVehicle.addJob()
        except:
            print('try later or try another vehicle')
            return -1
    else:
        print('invalid input')
        return -1
    return currentVehicle,queue

def releaseHire(currentVehicle):
    currentVehicle[0].releaseJob()
    currentVehicle[1].add(currentVehicle[0])
  
def addVehicle():
    vehicleType = input('Enter the type of veihcle you want to Add : (Car/Van/Three Wheel/Truck/Lorry):')
    if vehicleType == 'Car':
        while True:
            vehicleNo = input('Vehicle No : ')
            vehicleDriver = input('Vehicle Driver : ')
            seats = int(input('Seats : '))
            facility = input('Facility : (AC/NON_AC)')
            try:
                vehicle = Car(vehicleNo,vehicleDriver,seats,facility)
                vehicles.append(vehicle)
                if type(vehicle) is Car and vehicle.getMaxSeats().value == 3 and vehicle.getFacility().value == 1:
                    car1.add(vehicle)
                elif type(vehicle) is Car and vehicle.getMaxSeats().value == 3 and vehicle.getFacility().value == 2:
                    car2.add(vehicle)
                elif type(vehicle) is Car and vehicle.getMaxSeats().value == 4 and vehicle.getFacility().value == 1:
                    car3.add(vehicle)
                elif type(vehicle) is Car and vehicle.getMaxSeats().value == 4 and vehicle.getFacility().value == 2:
                    car4.add(vehicle)
                print('vehicle added')
                break
            except:
                print('invalid inputs')
                continue
    if vehicleType == 'Van':
        while True:
            vehicleNo = input('Vehicle No : ')
            vehicleDriver = input('Vehicle Driver : ')
            seats = int(input('Seats : '))
            facility = input('Facility : (AC/NON_AC)')
            try:
                vehicle = Van(vehicleNo,vehicleDriver,seats,facility)
                vehicles.append(vehicle)
                if type(vehicle) is Van and vehicle.getMaxSeats().value == 6 and vehicle.getFacility().value == 1:
                    van1.add(vehicle)
                elif type(vehicle) is Van and vehicle.getMaxSeats().value == 6 and vehicle.getFacility().value == 2:
                    van2.add(vehicle)
                elif type(vehicle) is Van and vehicle.getMaxSeats().value == 8 and vehicle.getFacility().value == 1:
                    van3.add(vehicle)
                elif type(vehicle) is Van and vehicle.getMaxSeats().value == 8 and vehicle.getFacility().value == 2:
                    van4.add(vehicle)
                print('vehicle added')
                break
            except:
                print('invalid inputs')
                continue
    if vehicleType.capitalize() == 'Three Wheel':
        while True:
            vehicleNo = input('Vehicle No : ')
            vehicleDriver = input('Vehicle Driver : ')
            seats = 3
            try:
                vehicle = ThreeWheeler(vehicleNo,vehicleDriver,seats)
                vehicles.append(vehicle)
                threeWheel.add(vehicle)
                print('vehicle added')
                break
            except:
                print('invalid inputs')
                continue
    if vehicleType == 'Truck':
        while True:
            vehicleNo = input('Vehicle No : ')
            vehicleDriver = input('Vehicle Driver : ')
            size = int(input('Size : '))
            try:
                vehicle = Truck(vehicleNo,vehicleDriver,size)
                vehicles.append(vehicle)
                if type(vehicle) is Truck and vehicle.getSize().value == 7:
                    truck1.add(vehicle)
                elif type(vehicle) is Truck and vehicle.getSize().value == 12:
                    truck2.add(vehicle)
                print('vehicle added')
                break
            except:
                print('invalid inputs')
                continue
    if vehicleType == 'Lorry':
        while True:
            vehicleNo = input('Vehicle No : ')
            vehicleDriver = input('Vehicle Driver : ')
            load = int(input('Load : '))
            try:
                vehicle = Truck(vehicleNo,vehicleDriver,load)
                vehicles.append(vehicle)
                if type(vehicle) is Lorry and vehicle.getLoad().value == 2500:
                    lorry1.add(vehicle)
                elif type(vehicle) is Lorry and vehicle.getLoad().value == 3500:
                    lorry2.add(vehicle)
                print('vehicle added')
                break
            except:
                print('invalid inputs')
                continue
        
def removeVehicle():
    vehicleNo = input('Vehicle Number : ')
    for vehicle in vehicles:
        if vehicle.getVehiclNo() == vehicleNo:
            vehicles.remove(vehicle)
            checkRemove(vehicle,vehicleNo)
            print('vehicle removed')
            break
        else:
            print('vehicle not found')

def main():
    login = input('Login as: (customer/admin/b) :')
    if login == 'b':
        return
    elif login == 'customer':
        z = setHire()
        if z == -1 or z == 0:
            return
        while True:
            x = input('wanna release job : (y/n) :')
            if x == 'y':
                releaseHire(z)
                print('Hire completed')
                break
            else:
                continue
    elif login == 'admin':
        while True:
            pw = input('Enter password : ')
            if pw == 'admin1':
                print('logged in as admin')
                print('To Add Vehicle : +')
                print('To Remove Vehicle : -')
                print('To Add Hire : A')
                print('To Release Hire : R')
                print('To Display Available Vehicles : D')
                print('return to main menu : b')
                choice = input('choose : (+/-/A/R/D/b) : ')
                if choice == 'b':
                    return
                elif choice == '+':
                    addVehicle()
                elif choice == '-':
                    removeVehicle()
                    
                elif choice == 'A':
                    v = input('Enter vehicle No : ')
                    for vehicle in vehicles:
                        if vehicle.getVehicleNo() == v:
                            vehicle.addJob()
                            print(vehicle.getStatus())
                            checkRemove(vehicle,v)
                            
                elif choice == 'R':
                    v = input('Enter vehicle No : ')
                    for vehicle in vehicles:
                        if vehicle.getVehicleNo() == v:
                            vehicle.releaseJob()
                            print(vehicle.getStatus())
                            checkAdd(vehicle)
                elif choice == 'D':
                    display()
                else:
                    print('invalid choice')
            else:
                print('invalid password')
                break
    else:
        print("invalid login")
        
while True:
    print('Welcome to Trash Cab ... u can go back using b ... ')
    terminate = input('press E to exit Enter to continue : ')
    if terminate == 'E':
        exit()
    else:
        main()



