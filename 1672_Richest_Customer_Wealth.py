# manual algorithm type
class Solution:
    def maximumWealth(self, accounts) -> int:
        dict_ = {}
        max_ = 0 

        # Loop in List in List
        for i in accounts:
            # if don't have sum result of each List add it to Dict
            if i[0] not in dict_:
                # sum each of List and added it into Dict
                dict_[sum(i)] = accounts.index(i)
        # Loop in Dict for searching max valuation of each of List 
        for i in dict_:
            if i > max_:
                max_ = i
                
        return max_

# function algorithm type
class Solution:
    def maximumWealth(self, accounts) -> int:
        return max(map(sum, accounts))   

print(Solution().maximumWealth([[95],[95],[64],[96]]))