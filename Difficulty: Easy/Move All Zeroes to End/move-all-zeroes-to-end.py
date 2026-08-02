class Solution:
	def pushZerosToEnd(self, arr):
    	i = 0
        while i < len(arr):
            if arr[i] == 0:
                break
            i += 1
        j = i+1
        while j < len(arr):
            if arr[j] != 0:
                arr[i],arr[j] = arr[j],arr[i]
                i += 1
            j += 1
    
        return arr
    	