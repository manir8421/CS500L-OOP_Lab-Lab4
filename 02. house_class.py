# define class >>>> Room
class Room:
    def __init__(self,type: str, size: int) -> None:
        self.__type = type
        self.__size = size

    # getter method (for acces):type
    @property
    def type(self) -> str:
        return self.__type
    
    # setter method (for set value): type
    @type.setter
    def type(self, new_type: str) -> None:
        self.__type = new_type

    # getter method (for acces):size
    @property
    def size(self) -> int:
        return self.__size
    
    # setter method (for set value): size
    @size.setter
    def size(self, new_size: int) -> None:
        self.__size = new_size
    
    def __str__(self) -> str:
        return f"\nRoom type={self.__type},\tRoom size={self.__size} sq-ft"

    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value,Room):
            return self.__type == __value.__type
        else:
            return False
    
    
# define class >>>> Garage
class Garage:
    def __init__(self, type: str, size: int, door_type: str) -> None:
        self.__type = type
        self.__size = size
        self.__door_type = door_type

    # getter method (for acces): type
    @property
    def type(self) -> str:
        return self.__type
    
    # setter method (for set value): type
    @type.setter
    def type(self, new_type: str) -> None:
        self.__type = new_type

    # getter method (for acces): size
    @property
    def size(self) -> int:
        return self.__size
    
    # setter method (for set value): size
    @size.setter
    def size(self, new_size: int) -> None:
        self.__size = new_size

    # getter method (for acces): door_type
    @property
    def door_type(self) -> str:
        return self.__door_type
    
    # setter method (for set value): door_type
    @door_type.setter
    def door_type(self, new_door_type: str) -> None:
        self.__door_type = new_door_type
    
    def __str__(self) -> str:
        return f"\nType= {self.__type}, Size= {self.__size} sq-ft, Door_Type: {self.__door_type}"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value,Garage):
            return self.__type == __value.__type
        else:
            return False

# definie class >>>> Television   
class Television:
    def __init__(self, screen_type: str, screen_size: int, resolution: str, price: float) -> None:
        self.__screen_type = screen_type
        self.__screen_size = screen_size
        self.__resolution = resolution
        self.__price = price

    # getter method (for acces): screen_type
    @property
    def screen_type(self) -> str:
        return self.__screen_type
    
    # setter method (for set value): screen_type
    @screen_type.setter
    def screen_type(self, new_screen_type: str) -> None:
        self.__screen_type = new_screen_type

    # getter method (for acces): screen_size
    @property
    def screen_size(self) -> int:
        return self.__screen_size
    
    # setter method (for set value): screen_size
    @screen_size.setter
    def screen_size(self, new_screen_size: int) -> None:
        self.__screen_size = new_screen_size

    # getter method (for acces): resolution
    @property
    def resolution(self) -> str:
        return self.__resolution
    
    # setter method (for set value): resolution
    @resolution.setter
    def type(self, new_resolution: str) -> None:
        self.__resolution = new_resolution

    # getter method (for acces): price
    @property
    def price(self) -> float:
        return self.__price
    
    # setter method (for set value): price
    @price.setter
    def price(self, new_price: float) -> None:
        self.__price = new_price


    def __str__(self) -> str:
        return f"\nScreen Type= {self.__screen_type},\tScreen Size= {self.__screen_size} inchs,\tResolution= {self.__resolution},\tPrice= {self.__price}"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value,Television):
            return self.__screen_type == __value.__screen_type
        else:
            return False

# define class >>>> House
class House:
    def __init__(self, address: str, square_feet: int, garage: Garage) -> None:
        self.__address = address
        self.__square_feet = square_feet
        self.__rooms: list[Room] = []
        self.__garages = garage
        self.__televisions: list[Television] = []

    # getter method (for acces): address
    @property
    def address(self) -> str:
        return self.__address
    
    # setter method (for set value): adress
    @address.setter
    def address(self, new_address: str) -> None:
        self.__address = new_address

    # getter method (for acces): square_feet
    @property
    def square_feet(self) -> int:
        return self.__square_feet
    
    # setter method (for set value): square_feet
    @square_feet.setter
    def square_feet(self, new_square_feet: int) -> None:
        self.__square_feet = new_square_feet


    # add room to list
    def add_room(self, room: Room) -> None:
        self.__rooms.append(room)

    # add television to list
    def add_television(self, television) -> None:
        self.__televisions.append(television)

    # remove telivision from list
    def remove_telivision(self, television) -> None:
        self.__televisions.remove(television)
    
    #list of OLED TV
    def get_oled_televisions(self) -> list[Television]:
        oled_tv:list[Television] = []
        for tv in self.__televisions:
            if tv.screen_type.lower() == "OLED".lower():
                oled_tv.append(tv)
        return oled_tv

    # to get biggest room of the house
    def get_biggest_room(self):
        biggest_room: Room = self.__rooms[0]
        for room in self.__rooms:
            if room.size > biggest_room.size:
                biggest_room = room
                break
        return biggest_room

    # similar house check
    def is_similar_house(self, other) -> bool:
            return self.__square_feet == other.__square_feet and len(self.__rooms) == len(other.__rooms)

    def __str__(self) -> str:
        return f"Address={self.__address}, Area={self.__square_feet} sq-ft,\nRoom= {self.__rooms},\nGarage= {self.__garages},\nTelevision= {self.__televisions}"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, House):
            return self.__square_feet == __value.__square_feet and len(self.__rooms) == len(__value.__rooms)
        else:
            return False


def main():
    ###################### House-01 #########################
    # call class 'Room' for input the room information (type:str, size:float)
    den_room = Room (" Den Room", 350)
    bedroom = Room (" Bedroom", 250)
    storeroom = Room (" Storeroom", 150)

    
    # call class 'Garage' for input the garage information (typ: str, size: float, door type: str)
    garage_01 = Garage ("Double", 550, "Roll-Up")

    # call class 'Television' for input the television information (scr type: str, scr siz: str, resol: str, price: float)
    tv_01 = Television ("LED", 60, "4K", 1000.00)
    tv_02 = Television ("LCD", 32, "HD", 500.00)
    tv_03 = Television ("OLED", 56, "8K", 2500.00)
    tv_04 = Television ("CRT", 21, "1080p", 320.00)

    # call class 'House' for input the house information (add: str, sq-ft: float, room: int, grage: str, tv: int)
    house_01 = House("161 Mission falls ln", 4500, garage_01)

    # ====== create my house_01 ======

    # add room to house
    house_01.add_room(den_room)
    house_01.add_room(bedroom)
    house_01.add_room(storeroom)

    # add television to house
    house_01.add_television(tv_01)
    house_01.add_television(tv_02)
    house_01.add_television(tv_03)
    house_01.add_television(tv_04)


    # print my house_01 details
    print ("===== House-01 Information =====")
    print (house_01)
    house_01.remove_telivision(tv_01)                                   # remove telivision
    garage_01.size = 400                                                # change garage size
    print ("\n==== House-01 after remove items and change value ====")
    print (house_01)

    # OLED TV list for house_01
    print ("\n====== House-01: OLED Television List ======")
    oled_tv = house_01.get_oled_televisions()
    print (f"OLED TV in house-01: {oled_tv}")
    
    # biggest room for house_01
    print ("\n====== House-01: biggest room ======")
    biggest_room = house_01.get_biggest_room()
    print(f"Biggest room in house-01: {biggest_room}")


###################### House-02 #########################
# call class 'Room' for input the room information (type:str, size:float)
    den_room_2 = Room (" Den Room", 320)
    bedroom_2 = Room (" Bedroom", 400)
    storeroom_2 = Room (" Storeroom", 250)

    # call class 'Garage' for input the garage information (typ: str, size: float, door type: str)
    garage_02 = Garage ("Double", 600, "Automatic")

    # call class 'Television' for input the television information (scr type: str, scr siz: str, resol: str, price: float)
    tv_01_2 = Television ("LED", 65, "4K", 2050.00)
    tv_02_2 = Television ("LCD", 44, "HD", 950.00)
    tv_03_2 = Television ("OLED", 52, "8K", 5000.00)

    # call class 'House' for input the house information (add: str, sq-ft: float, room: int, grage: str, tv: int)
    house_02 = House ("79 Wenatchee ln", 6200, garage_02)

    # ====== create my house_02 ======

    # add room to house
    house_02.add_room(den_room_2)
    house_02.add_room(bedroom_2)
    house_02.add_room(storeroom_2)

    # add television to house
    house_02.add_television(tv_01_2)
    house_02.add_television(tv_02_2)
    house_02.add_television(tv_03_2)


    # print my house_02 details
    print ("\n===== House-02 Information =====")
    print (house_02)
    house_02.remove_telivision(tv_03_2)                                   # remove telivision
    garage_02.size = 950                                                  # change garage size
    print ("\n==== House-02 after remove items and change value ====")
    print (house_02)
    
    # OLED TV list for house_02
    print ("\n====== House-02: OLED Television List ======")
    oled_tv = house_02.get_oled_televisions()
    if oled_tv:
        for tv in oled_tv:
            print(tv)
    else:
        print("No OLED television found")
    
    # biggest room for house_02
    print ("\n====== House-02: biggest room ======")
    biggest_room = house_02.get_biggest_room()
    print(f"Biggest room in house-02: {biggest_room}")

    # Check similarity hot both house (house-01 and house-02)
    print ("\n====== House Similarity Check ======")
    if house_01.is_similar_house(house_02):
        print ("Both houses are similar")
    else:
        print ("Sorry! Both houses are not similar.")


if __name__ == "__main__":
    main()

      