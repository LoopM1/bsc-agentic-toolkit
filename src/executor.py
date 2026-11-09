import json
import urllib.request
import sys

RPC_URL = "https://bsc-dataseed.binance.org"

def simulate_call(ca: str, calldata: str, from_addr: str = "0x0000000000000000000000000000000000000001", value: int = 0):
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_call",
        "params": [{
            "from": from_addr,
            "to": ca,
            "data": calldata,
            "value": hex(value)
        }, "latest"]
    }).encode('utf-8')
    
    req = urllib.request.Request(RPC_URL, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            if "error" in data:
                return {"success": False, "error": data["error"]}
            return {"success": True, "result": data.get("result", "0x")}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    res = simulate_call("0xb2625d56a7fc855bf7432b5584b390a4b4d9c7fd", "0xa0712d680000000000000000000000000000000000000000000000000000000000000001")
    print(json.dumps(res, indent=2))
