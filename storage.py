import json
"""
{
    "platform": str,
    "asset_type": str,
    "principal": float,
    "current_value": float,
    "rate": float,
    "sip_amount": float,
    "start_date": str,
    "last_updated": str,
    "reinvestment_rule": str,
    "reinvestment_split": float,
    "withdraw_amount": float 
}
"""
def load_portfolio(filename="portfolio.json"):
    try:
        with open(filename,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]

def save_portfolio(portfolio,filename = "portfolio.json" ):
    with open(filename, "w") as f:
        json.dump(portfolio , f,indent=4)
def edit_holding(portfolio):
    name = input("Enter the name of the holding to edit:- ")
    target = None
    for h in portfolio:
        if h["name"] == name:
            target = h
            break

    if not target:
        print("Holding not found")
        return

    print(f"\nEditing '{name}'. Current values:")
    for key, value in target.items():
        print(f"  {key}: {value}")

    field = input("\nWhich field do you want to change?:- ")
    if field not in target:
        print("That field doesn't exist on this holding.")
        return

    new_value = input(f"Enter new value for {field}:- ")

    numeric_fields = ["principal", "current_value", "rate", "sip_amount",
                       "reinvestment_split", "withdraw_amount"]
    if field in numeric_fields:
        target[field] = float(new_value)
    else:
        target[field] = new_value

    print(f"Updated {field} to {target[field]}")


def remove_holding(portfolio):
    name = input("Enter the name of the holding to remove:- ")
    for h in portfolio:
        if h["name"] == name:
            portfolio.remove(h)
            print(f"Removed '{name}'")
            return
    print("Holding not found")

def view_portfolio(portfolio):
    if not portfolio:
        print("\nNo holdings yet.")
        return

    print(f"\n{'='*70}")
    print("CURRENT PORTFOLIO")
    print(f"{'='*70}")
    for h in portfolio:
        print(f"\nName:         {h['name']}")
        print(f"Platform:     {h['platform']}")
        print(f"Asset type:   {h['asset_type']}")
        print(f"Principal:    ₹{h['principal']:,.2f}")
        print(f"Current value:₹{h['current_value']:,.2f}")
        print(f"Rate:         {h['rate']*100:.1f}%")
        print(f"SIP:          ₹{h['sip_amount']:,.2f}/month")
        print(f"Reinvestment: {h['reinvestment_rule']}")
    print(f"\n{'='*70}\n")