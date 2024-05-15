class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, start_day,days_in_month):
        day_index = {
            "Monday": 0,
            "Tuesday": 1,
            "Wednesday": 2,
            "Thursday": 3,
            "Friday": 4,
            "Saturday": 5,
            "Sunday": 6
        }
        
        start_day_index = day_index[start_day]
        days_until_sunday = (6 - start_day_index) % 7
        first_sunday = 1 + days_until_sunday
        
        if first_sunday > days_in_month:
            return 0
        sundays_count = 1 + (days_in_month - first_sunday) // 7
        
        return sundays_count
