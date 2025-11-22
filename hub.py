from transitions import Machine
from recon import ReconModule
from scan import ScanModule
from exploit import ExploitModule
from evasion import EvasionModule

class AIToolkit:
    states = ['idle', 'recon', 'scan', 'exploit', 'evade', 'done']
    
    def __init__(self, target_ip, nmap_output=None):
        self.target = target_ip
        self.nmap_output = nmap_output  # Pass your scan output here
        self.machine = Machine(model=self, states=AIToolkit.states, initial='idle')
        self.machine.add_transition('start_recon', 'idle', 'recon')
        self.machine.add_transition('start_scan', 'recon', 'scan')
        self.machine.add_transition('start_exploit', 'scan', 'exploit')
        self.machine.add_transition('apply_evasion', 'exploit', 'evade')
        self.machine.add_transition('finish', 'evade', 'done')
        
        self.recon = ReconModule()
        self.scan = ScanModule()
        self.exploit = ExploitModule()
        self.evasion = EvasionModule()
    
    def run_pipeline(self):
        print(f"[DEBUG] Starting AI toolkit pipeline on HTB target: {self.target}")
        self.start_recon()
        vuln_data = self.recon.run(self.target, self.nmap_output)
        print(f"[DEBUG] Recon complete: {vuln_data}")
        
        self.start_scan()
        scan_results = self.scan.run(self.target, vuln_data)  # Skip re-scan; use parsed data
        print(f"[DEBUG] Scan complete: {scan_results}")
        
        self.start_exploit()
        exploit_success = self.exploit.run(self.target, scan_results)
        print(f"[DEBUG] Exploit success: {exploit_success}")
        
        self.apply_evasion()
        evasion_result = self.evasion.run(exploit_success)
        print(f"[DEBUG] Evasion applied: {evasion_result}")
        
        self.finish()
        return f"Pipeline complete. Evasion accuracy: {evasion_result['accuracy']}%"

if __name__ == "__main__":
    # Paste your Nmap output here or load from file
    nmap_output = """
Starting Nmap 7.98SVN ( https://nmap.org ) at 2025-11-22 06:32 -0500
Nmap scan report for 10.129.208.46
Host is up (0.42s latency).
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
23/tcp open  telnet  Linux telnetd
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
"""
    toolkit = AIToolkit("10.129.208.46", nmap_output)
    print(toolkit.run_pipeline())
