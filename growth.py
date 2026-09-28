def project_bonds(holding_name, years):
    rate = holding_name["rate"]
    principal = holding_name["current_value"]
    rule = holding_name["reinvestment_rule"]
    value = principal
    payout_total = 0

    for y in range(years):
        coupon = value * rate
        if rule == "none":
            payout_total += coupon
        elif rule == "full":
            value += coupon  
        elif rule == "partial":
            reinvest_share = coupon * (holding_name["reinvestment_split"] / 100)
            payout_total += coupon - reinvest_share
            value += reinvest_share
        elif rule == "fixed_amount_withdraw":
            value += coupon
            value -= holding_name["withdraw_amount"] * 12
        if value < 0:
            value = 0
    return value  

def project_market(holding_name, years):
    rate = holding_name["rate"]
    value = holding_name["current_value"]
    sip = holding_name["sip_amount"]
    rule = holding_name["reinvestment_rule"]

    for y in range(years):
        gain = value * rate
        value += gain
        value += sip * 12
        if rule == "partial":
            withdrawal = gain * (holding_name["reinvestment_split"] / 100)
            value -= withdrawal
        elif rule == "fixed_amount_withdraw":
            value -= holding_name["withdraw_amount"] * 12
        if value < 0:
            value = 0
    return value


def project_p2p(holding_name, years):
    rate = holding_name["rate"]
    value = holding_name["current_value"]
    rule = holding_name["reinvestment_rule"]

    for y in range(years):
        value = value * (1 + rate)
        if rule == "fixed_amount_withdraw":
            value -= holding_name["withdraw_amount"] * 12
        elif rule == "partial":
            gain = value - value / (1 + rate)
            withdrawal = gain * (holding_name["reinvestment_split"] / 100)
            value -= withdrawal
        if value < 0:
            value = 0
    return value