    from queue import Queue
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result=[]
        if s==None:
            return result
        q=Queue()   
        set1=set()
        q.put(s)
        set1.add(s)
        print("hi")
            
        flag=False
        while not(q.empty()):
            curr=q.get()
            #agar valid hain string to result me add kardo
            if self.isValid(curr):
                flag=True
                result.append(curr)
            elif not(flag):
                for i in range(len(curr)):
                    if curr[i].isalpha():
                        continue
                    child=curr[0:i]+curr[i+1:]
                    if child not in set1:
                        q.put(child)
                        set1.add(child)
        return result
                        
    def isValid(self,string):
        count=0
        i=0
        while i<len(string):
            if string[i]=='(':
                count+=1
            elif string[i]==')':
                count-=1
                if count<0:
                    return False
        if count>0:
            return False
        else:
            return True
Time Complexity is O(n2 raise to power n)
Space is O(2 raise to power n)
