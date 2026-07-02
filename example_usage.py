"""
example_usage.py -- Demonstrates the InfluencerMatchClient SDK.
"""
from client import InfluencerMatchClient

def main():
    client = InfluencerMatchClient(seed=42)

    # 1. Beauty product, conversion-focused
    print("[1] Beauty Product -- Conversion Campaign ($5,000 budget)")
    result = client.match(
        product_category="beauty",
        budget_usd=5000,
        campaign_goal="conversions",
        platform="all",
        top_n=3,
    )
    print("Top Influencer Matches:")
    for m in result["matches"]:
        print(f"  {m['handle']} ({m['platform']}) | {m['tier']} | {m['followers']:,} followers | {m['engagement_rate']}% eng | Fit: {m['fit_score']} | Cost: ${m['estimated_cost_usd']:,}")
        roi = m["estimated_roi"]
        print(f"    -> Est. Conversions: {roi['estimated_conversions']}, CPC: ${roi['cost_per_conversion_usd']}")
    print(f"\nBudget Allocation:")
    for tier, amt in result["budget_allocation"].items():
        print(f"  {tier}: ${amt:,.2f}")
    print(f"\n{result['campaign_brief']}")

    # 2. Tech product, awareness campaign
    print("\n[2] Tech Product -- Awareness Campaign ($15,000 budget)")
    result = client.match(
        product_category="tech",
        budget_usd=15000,
        campaign_goal="awareness",
        platform="youtube",
        top_n=3,
    )
    for m in result["matches"]:
        print(f"  {m['handle']} | {m['followers']:,} subs | Fit Score: {m['fit_score']}")

if __name__ == "__main__":
    main()
