import sys
sys.stdout.reconfigure(encoding='utf-8')

class CpsAffiliateCommissionYieldRouterClient:
    """
    K2 Lab creator monetization and commission yield optimization engine.
    Calculates expected net creator payout taking into account base commission %,
    progressive volume bonuses, platform processing cuts, and return/refund clawback provisions.
    Computes effective RPM (Revenue Per 1,000 Impressions).
    """
    def __init__(self, platform_fee_pct=0.035):
        self.platform_fee_pct = platform_fee_pct

    def evaluate_commission_yield(self, product_price_usd, base_commission_pct, conversion_rate_pct, expected_refund_rate_pct=0.08, volume_tier_bonus_pct=0.02):
        """
        product_price_usd: Retail selling price
        base_commission_pct: e.g. 0.15 for 15%
        conversion_rate_pct: e.g. 1.8 for 1.8%
        expected_refund_rate_pct: refund/cancellation deduction e.g. 0.08 for 8%
        volume_tier_bonus_pct: additional tier incentive e.g. 0.02 for 2%
        """
        gross_commission_rate = base_commission_pct + volume_tier_bonus_pct
        gross_commission_per_unit = product_price_usd * gross_commission_rate

        # Net effective commission after platform fee and refund clawbacks
        net_retained_ratio = (1.0 - expected_refund_rate_pct) * (1.0 - self.platform_fee_pct)
        net_commission_per_unit = gross_commission_per_unit * net_retained_ratio

        # Expected revenue per 1,000 video views (RPM)
        orders_per_1000_views = (conversion_rate_pct / 100.0) * 1000.0
        expected_gmv_per_1000_views = orders_per_1000_views * product_price_usd
        expected_creator_rpm = orders_per_1000_views * net_commission_per_unit

        payout_grade = "TIER_1_HIGH_YIELD" if expected_creator_rpm >= 15.0 else ("TIER_2_VIABLE_PROFIT" if expected_creator_rpm >= 6.0 else "TIER_3_LOW_EFFICIENCY")

        return {
            "status": "success",
            "product_price_usd": round(product_price_usd, 2),
            "gross_commission_rate_pct": round(gross_commission_rate * 100, 1),
            "net_commission_per_order": round(net_commission_per_unit, 2),
            "expected_orders_per_1k_views": round(orders_per_1000_views, 2),
            "expected_gmv_per_1k_views": round(expected_gmv_per_1000_views, 2),
            "expected_creator_rpm_usd": round(expected_creator_rpm, 2),
            "yield_efficiency_rating": payout_grade,
            "deductions_summary": {
                "platform_fee_pct": round(self.platform_fee_pct * 100, 1),
                "refund_clawback_pct": round(expected_refund_rate_pct * 100, 1)
            }
        }
