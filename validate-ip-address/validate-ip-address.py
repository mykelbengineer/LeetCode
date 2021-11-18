class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        if queryIP.count(':') == 7:
            return self.validateIPSix(queryIP)
            
        elif queryIP.count('.') == 3:
            return self.validateIPFour(queryIP)
        
        else:
            return "Neither"
            
        
        
    def validateIPFour(self, ip):
        ips = ip.split('.')
        if len(ips) != 4 : return 'Neither'
        for i in ips:
            if len(i)== 0 or (len(i) > 1 and i[0] == '0'):
                return 'Neither'
            
            if not i.isdigit() or int(i) > 255:
                return 'Neither'
            
        return 'IPv4'
            
    
    def validateIPSix(self, ip):
        ips = ip.split(':')
        valid = '0123456789abcdefABCDEF'
        if len(ips) != 8 : return 'Neither'
        
        for i in ips:
            ip_len = len(i)
            if ip_len < 1 or ip_len > 4:
                return 'Neither'
            
            for char in i:
                if char not in valid:
                    return 'Neither'
                        
        return 'IPv6'
                            
            
        
        