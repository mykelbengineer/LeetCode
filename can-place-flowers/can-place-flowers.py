class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers_to_place = n
        bed = [0] + flowerbed + [0]
        size = len(bed)
        
        for i in range(1, size - 1):
            if bed[i-1] == 0 and bed[i] == 0 and bed[i+1] == 0:
                bed[i] = 1
                flowers_to_place -= 1
                
        
        return flowers_to_place <= 0
        