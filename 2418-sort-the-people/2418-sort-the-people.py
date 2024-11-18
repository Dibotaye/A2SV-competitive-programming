class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            index=i
            for j in range(i+1,len(heights)):
                if heights[j]>heights[index]:
                    index=j
            heights[i],heights[index]=heights[index],heights[i]
            names[i],names[index]= names[index],names[i]
        return names
        