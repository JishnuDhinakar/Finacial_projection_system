def holdingformat(holding,projected_values):
    return(
        f"{holding['name']:<15}"
        f"{holding['platform']:<12}"
        f"{holding['asset_type']:<12}"
        f"Current:₹{holding['current_value']:>12,.2f}"
        f"Projected: ₹{projected_values:>12,.2f}"
    )   


def generate_report(portfolio,projections,years):
    print(f"\n{"="*70}")
    print(f"PORTFOLIO PROJECTION REPORT - {years} year(s) ahead")
    print(f"{"="*70}\n")

    total_current = 0
    total_projected =0
    by_current ={}
    by_projected = {}

    for holding in portfolio:
        name = holding["name"]
        if name not in projections:
            continue
        projected_value = projections[name]
        print(holdingformat(holding,projected_value))
        total_current += holding["current_value"]
        total_projected += projected_value

        asset_type = holding["asset_type"]
        by_current[asset_type] = by_current.get(asset_type ,0)+holding["current_value"]
        by_projected[asset_type] = by_projected.get(asset_type,0)+projected_value

    print(f"\n{'-'*70}")
    print(f"TOTAL CURRENT VALUE: ₹{total_current:,.2f}")
    print(f"TOTAL PROJECTED VALUE: ₹{total_projected:,.2f}")
    print(f"{"="*70}\n")