from dataclasses import dataclass
from typing import List, Union


@dataclass
class IPOps:
    file_name: str
    ip: List[Union[str, int]]

    def __init__(self, file_name: str):
        with open(f"{file_name}", 'r') as f:
            self.ip = [i.strip('\n') for i in f]
        
        if "test" in file_name and "," in self.ip[0] and not "[" in self.ip[0]:
            ip, exp_p1, exp_p2 = [], [], []
            for item in self.ip:
                ip_string, p1, p2 = item.split(",")
                ip.append(ip_string.strip())
                exp_p1.append(p1.strip())
                exp_p2.append(p2.strip())
            
            self.exp_p1 = exp_p1
            self.exp_p2 = exp_p2
            self.ip = ip