from client import CpsAffiliateCommissionYieldRouterClient
import sys
sys.stdout.reconfigure(encoding='utf-8')

def main():
    router = CpsAffiliateCommissionYieldRouterClient()
    print("=== MORAS CPS AFFILIATE COMMISSION YIELD ROUTER ===")

    # Trending Home Appliance: $49.99 with 20% base commission
    res = router.evaluate_commission_yield(
        product_price_usd=49.99,
        base_commission_pct=0.20,
        conversion_rate_pct=1.45,
        expected_refund_rate_pct=0.07,
        volume_tier_bonus_pct=0.03
    )

    print()
    print(f"Product Price      : ${res['product_price_usd']}")
    print(f"Gross Commission   : {res['gross_commission_rate_pct']}%")
    print(f"Net Creator Payout : ${res['net_commission_per_order']}/order (After refund & platform fees)")
    print(f"Orders / 1K Views  : {res['expected_orders_per_1k_views']}")
    print(f"Expected GMV / 1K  : ${res['expected_gmv_per_1k_views']:,.2f}")
    print(f"Creator Yield (RPM): ${res['expected_creator_rpm_usd']} / 1,000 Views")
    print(f"Rating Category    : {res['yield_efficiency_rating']}")

if __name__ == "__main__":
    main()
