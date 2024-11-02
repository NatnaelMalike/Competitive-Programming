class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for domain in cpdomains:
            n, d_str = domain.split()
            n = int(n)
            d_str = d_str.split('.')
            for i in range(len(d_str)):
                d = '.'.join(d_str[i:])
                if d in dic:
                    dic[d] += n
                else:
                    dic[d] = n
        return [str(val) + " " + key for key, val in dic.items()]

        