class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pasTri=[[1]]
        for i in range(numRows-1):
            prow=[0]+pasTri[-1]+[0]
            row=[]
            for j in range(len(pasTri[-1])+1):
                row.append(prow[j]+prow[j+1])
            pasTri.append(row)
        return pasTri


        


