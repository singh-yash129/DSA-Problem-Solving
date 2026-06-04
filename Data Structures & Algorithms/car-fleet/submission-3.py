class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair positions with speeds and sort by position in descending order
        # (Cars closest to the target come first)
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        current_max_time = 0.0
        
        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            
            # If this car takes STRICTLY MORE time than the fleet ahead,
            # it cannot catch up. It must form its own new fleet.
            if time_to_target > current_max_time:
                fleets += 1
                current_max_time = time_to_target # This car is now the leader of the new fleet
                
        return fleets