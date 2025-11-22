class ScanModule:
    def __init__(self):
        from evasion import EvasionModule
        self.evasion = EvasionModule()
    
    def run(self, target, vuln_data):
        # Skip re-scan; use recon data
        results = []
        for port in vuln_data['ports']:
            delay = self.evasion.predict_delay(port)
            print(f"[DEBUG] Simulating scan on port {port} with evasion delay {delay}s")
            import time
            time.sleep(delay * 0.1)  # Shorter for sim
            results.append(f"Port {port} open (telnet)")
        return results
