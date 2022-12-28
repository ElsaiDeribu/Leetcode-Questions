class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        dic = defaultdict(int)
        ans = []
        
        
        def countDomains(string):
            
            count, domain = string.split()
            domains = domain.split('.')
            
            
            for i in range(len(domains)):
                parentCpDomain = '.'.join(domains[i:])
                dic[parentCpDomain] += int(count)

        
        for i in cpdomains:
            countDomains(i)
            
        
        for d in dic:
            ans.append(str(dic[d]) + " " + d)
            
        return ans