import json
import re
import urllib.request
import sys

RPC_URL = "https://bsc-dataseed.binance.org"

def extract_selectors_from_bytecode(code_hex: str):
    """Parses EVM dispatcher push4 patterns (PUSH4 0xXXXXXXXX EQ)."""
    return sorted(list(set(re.findall(r"63([0-9a-fA-F]{8})14", code_hex))))

def scan_contract(ca: str):
    payload = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "eth_getCode", "params": [ca, "latest"]}).encode('utf-8')
    req = urllib.request.Request(RPC_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())
        code = data.get("result", "")
        selectors = extract_selectors_from_bytecode(code)
        return {"contract": ca, "bytecode_length": len(code), "selectors_count": len(selectors), "selectors": ["0x" + s for s in selectors]}

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "0xb2625d56a7fc855bf7432b5584b390a4b4d9c7fd"
    print(json.dumps(scan_contract(target), indent=2))
