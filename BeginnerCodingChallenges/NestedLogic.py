import re
class Novel():
    def __init__(self, a_return_date = None, e_return_date = None):
        self.expected_return_date = e_return_date
        self.expected_return_date_formatted = re.split(r'\d{2}:\d{2}:\d{4}',':'.join(self.expected_return_date))
        self.actual_return_date = a_return_date
        self.actual_return_date_formatted = re.split(r'\d{2}:\d{2}:\d{4}',':'.join(self.actual_return_date))
        self.total_fines = 0

    def calculateFines(self):
        # Verify time stamps are correctly entered
        if self.expected_return_date_formatted and self.actual_return_date_formatted:
            # Set variable to identify largest difference between days, months, or years
            largest_difference = 0
            #Calculate the difference between the two dates
            days_difference = int(self.expected_return_date[0]) - int(self.actual_return_date[0])
            months_difference = int(self.expected_return_date[1]) - int(self.actual_return_date[1])
            years_difference = int(int(self.expected_return_date[2]) - int(self.actual_return_date[2]))
            # If there is a difference in days found only, just calculate daily fines
            if days_difference > 0 and years_difference == 0:
                print("Largest difference found in days:", days_difference)
                largest_difference = days_difference
                fine_value = 15
            # If there is a difference in months found, only calculate monthly fines
            if months_difference > 0 and years_difference == 0:
                print("Largest difference found in months:", months_difference)
                largest_difference = months_difference
                fine_value = 500
            # If there is a difference in years found, simply send a single fine of 10,000.00 Hackos
            if years_difference >= 1:
                print("Largest difference found in years:", years_difference)
                self.total_fines += 10000
                return self.total_fines
            # Calculate fines based on largest difference found
            for time in range(largest_difference):
                self.total_fines += fine_value
            # Return total fines
            return self.total_fines
        else:
            print("Not a valid date format!")
            return False

def main():
    expected_timestamp = list( map(str, input().split()) )
    actual_timestamp = list( map(str, input().split()) )
    romancenovel = Novel(actual_timestamp, expected_timestamp)
    print(romancenovel.calculateFines())

if __name__ == "__main__":
    main()