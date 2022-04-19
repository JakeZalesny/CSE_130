

from calendar import month


class Date(): 

    def __init__(self, day, month, year) -> None:
        self._day = day
        self._month = month
        self._year = year
        self._year_value = 365
        
        self._month_to_number = {
            "January": 1,
            "February" : 2,
            "March" : 3,
            "April" : 4,
            "May" : 5,
            "June" : 6,
            "July" : 7,
            "August" : 8,
            "September" : 9,
            "October" : 10,
            "November" : 11,
            "December" : 12
        }
    
    def get_day(self):
        return self._day
    
    def get_month(self):
        return self._month
    
    def get_year(self):
        return self._month
    
    def is_30(self, month):
        if month.upper() == "NOVEMBER" or month.upper == "SEPTEMBER" or month.upper() == "APRIL" or month.upper() == "JUNE": 
            return True
        else: 
            return False
    def is_31(self, month):
        if month.upper() != "FEBRUARY" and self.is_30(month) != True :
            return True
        else:
            return False
    
    def is_leap_year(self) :
        if self._year % 4 == 0 or self._year % 400 == 0 : 
            return True
        
        elif self._year % 4 == 0 and self._year % 100 == 0 :
            return True
        
        else: 
            return False

    def calculate_day_total(self) -> int:
        
        month_number = self._month_to_number[self._month]
        month_list = self._month_to_number.keys()
        month_total = 0
        year_total = 0
        
        for i in range(0, self._year - 1) :
            year_total += 365

            if self.is_leap_year() == True :
                year_total += 366 
        
        
        for i in month_list:
            if self.is_30(i) == True :
                 month_total += 30
            
            elif self.is_31(i) :
                month_total += 31

            if i.upper() == "FEBRUARY" :
                if self.is_leap_year() == True :
                    month_total += 29
                
                else: 
                    month_total += 30
            if i == month_number :
                break
        
        return year_total + month_total + self._day
    


def do_calculation(): 
    day_1 = int(input("What is the day of the first date: "))
    month_1 = input("What is the month: ")
    year_1 = int(input("What is the year: "))
    
    date_1 = Date(day_1, month_1, year_1)
    first_total = date_1.calculate_day_total()

    day_2 = int(input("What is the day of the second date: "))
    month_2 = input("What is the month: ")
    year_2 = year_1 = int(input("What is the year: "))

    date_2 = Date(day_2, month_2, year_2)
    second_total = date_2.calculate_day_total()

    total = first_total - second_total

    return total
    
def main():
    total = do_calculation()
    print(total)

main()






    