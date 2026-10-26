import sys, json
from client import CpsAffiliateCommissionYieldRouterClient
sys.stdout.reconfigure(encoding='utf-8')

def handle_mcp():
    router = CpsAffiliateCommissionYieldRouterClient()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps({"status": "ready", "skill": "moras-cps-affiliate-commission-yield-router-skill"}))
        return
    req = json.loads(sys.stdin.read() or "{}")
    price = req.get("product_price_usd", 30.0)
    comm = req.get("base_commission_pct", 0.15)
    cvr = req.get("conversion_rate_pct", 1.5)
    res = router.evaluate_commission_yield(price, comm, cvr)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    handle_mcp()
