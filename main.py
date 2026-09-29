from storage import load_portfolio ,save_portfolio , edit_holding ,remove_holding ,view_portfolio
from growth import project_market , project_bonds , project_p2p
from report import generate_report

def build_portfolio():
    portfolio =[]
    i = int(input("Enter the number of asset_types:-  \n"
    "1.Stocks \n" 
    "2.MutualFunds\n" 
    "3.Bonds\n" 
    "4.P2P_Lending\n" 
    "5.etc\n"
    "\nWhat is your choice:- "))
    while i != 0:
        asset_no = int(input("\nwhat asset_type are you entering data regarding (Enter 1-5):- \n"
                            "1.Stocks\n"
                            "2.MutualFunds\n" 
                            "3.Bonds\n"
                            "4.P2P_lending\n" 
                            "5.etc (specify?)\n"
                            "\nWhat is your choice:- "))
        if asset_no == 1:
            asset_info = "Stocks"
        elif asset_no == 2:
            asset_info = "MutualFunds"
        elif asset_no == 3:
            asset_info = "Bonds"
        elif asset_no == 4:
            asset_info = "P2P_lending"
        elif asset_no == 5:
            asset_info = "etc"
        else:
            print("Invalid input")
        
        
        
        j = int(input("how many platforms:- "))
        while j != 0:
            portfolio.append(get_holding(asset_info))
            j-=1
        i -= 1
    return portfolio


def get_holding(asset_info):
    holding = {}
    holding["name"] = input("\nEnter the holding name:- ")
    holding["asset_type"] = asset_info
    if asset_info == "Stocks":
        asset_platform = int(input("Enter the your choice:- \n"
                            "1.Zerodha\n" 
                            "2.Groww\n"
                            "3.Angel One\n"
                            "4.specify\n"
                            "\n Enter your choice:- "))
        if asset_platform == 1:
            holding["platform"] = "Zerodha"
            Ror_asset = int(input("Enter the your choice:- \n"
                            "1.12%\n" 
                            "2.15%\n"
                            "3.18%\n"
                            "4.specify\n"))
            if Ror_asset == 1:
                holding["rate"] = 12.0/100
            elif Ror_asset == 2:
                holding["rate"] = 15.0/100
            elif Ror_asset == 3:
                holding["rate"] = 18.0/100
            else:
                holding["rate"] = (float(input("Enter the rate:- ")))/100
        elif asset_platform == 2:
            holding["platform"] = "Groww"
            Ror_asset = int(input("Enter the your choice:- \n"
                                        "1.12%\n" 
                                        "2.15%\n"
                                        "3.18%\n"
                                        "4.specify\n"))
            if Ror_asset == 1:
                holding["rate"] = 12.0/100
            elif Ror_asset == 2:
                holding["rate"] = 15.0/100
            elif Ror_asset == 3:
                holding["rate"] = 18.0/100
            else:
                holding["rate"] = (float(input("Enter the rate:- ")))/100
        elif asset_platform == 3:
            holding["platform"] = "Angel One"
            Ror_asset = int(input("Enter the your choice:- \n"
                                        "1.12%\n" 
                                        "2.15%\n"
                                        "3.18%\n"
                                        "4.specify\n"))
            if Ror_asset == 1:
                holding["rate"] = 12.0/100
            elif Ror_asset == 2:
                holding["rate"] = 15.0/100
            elif Ror_asset == 3:
                holding["rate"] = 18.0/100
            else:
                holding["rate"] = (float(input("Enter the rate:- ")))/100
        elif asset_platform == 4:
            holding["platform"] = input("Enter the your platform no:- ")
            Ror_asset = int(input("Enter the your choice:- \n"
                                        "1.12%\n" 
                                        "2.15%\n"
                                        "3.18%\n"
                                        "4.specify\n"))
            if Ror_asset == 1:
                holding["rate"] = 12.0/100
            elif Ror_asset == 2:
                holding["rate"] = 15.0/100
            elif Ror_asset == 3:
                holding["rate"] = 18.0/100
            else:
                holding["rate"] = (float(input("Enter the rate:- ")))/100
        else:
            print("Invalid input ")


    elif asset_info == "MutualFunds":
        asset_platform = int(input("\nEnter the your choice:- \n"
                            "1.Zerodha\n" 
                            "2.Groww\n"
                            "3.Angel One\n"
                            "4.specify\n"))
        if asset_platform == 1:
            holding["platform"] = "Zerodha"
            Ror_asset = int(input("Enter the your choice:- \n"
                            "1.12%\n" 
                            "2.15%\n"
                            "3.18%\n"
                            "4.specify\n"))
            if Ror_asset == 1:
                holding["rate"] = 12.0/100
            elif Ror_asset == 2:
                holding["rate"] = 15.0/100
            elif Ror_asset == 3:
                holding["rate"] = 18.0/100
            else:
                holding["rate"] = (float(input("Enter the rate:- ")))/100
        elif asset_platform == 2:
            holding["platform"] = "Groww"
            Ror_asset = int(input("Enter the your choice:- \n"
                                        "1.12%\n" 
                                        "2.15%\n"
                                        "3.18%\n"
                                        "4.specify\n"))
            if Ror_asset == 1:
                holding["rate"] = 12.0/100
            elif Ror_asset == 2:
                holding["rate"] = 15.0/100
            elif Ror_asset == 3:
                holding["rate"] = 18.0/100
            else:
                holding["rate"] = (float(input("Enter the rate:- ")))/100
        elif asset_platform == 3:
            holding["platform"] = "Angel One"
            Ror_asset = int(input("Enter the your choice:- \n"
                                        "1.12%\n" 
                                        "2.15%\n"
                                        "3.18%\n"
                                        "4.specify\n"))
            if Ror_asset == 1:
                holding["rate"] = 12.0/100
            elif Ror_asset == 2:
                holding["rate"] = 15.0/100
            elif Ror_asset == 3:
                holding["rate"] = 18.0/100
            else:
                holding["rate"] = (float(input("Enter the rate:- ")))/100
        elif asset_platform == 4:
            holding["platform"] = input("Enter the your platform no:- ")
            Ror_asset = int(input("Enter the your choice:- \n"
                                        "1.12%\n" 
                                        "2.15%\n"
                                        "3.18%\n"
                                        "4.specify\n"))
            if Ror_asset == 1:
                holding["rate"] = 12.0/100
            elif Ror_asset == 2:
                holding["rate"] = 15.0/100
            elif Ror_asset == 3:
                holding["rate"] = 18.0/100
            else:
                holding["rate"] = (float(input("Enter the rate:- ")))/100
        else:
            print("Invalid input ")
    elif asset_info == "Bonds":
        asset_platform = int(input("\nEnter the your choice:- \n"
                            "1.Wint wealth\n" 
                            "2.Grip Invest\n"
                            "3.India Bonds\n"
                            "4.specify\n"))
        if asset_platform == 1:
            holding["platform"] = "Wint Wealth"
            Ror_asset = int(input("Enter the your choice:- \n"
                            "1.10%\n" 
                            "2.11%\n"
                            "3.12%\n"
                            "4.specify\n"))
            if Ror_asset == 1:
                holding["rate"] = 10.0/100
            elif Ror_asset == 2:
                holding["rate"] = 11.0/100
            elif Ror_asset == 3:
                holding["rate"] = 12.0/100
            else:
                holding["rate"] = (float(input("Enter the rate:- ")))/100
        elif asset_platform == 2:
            holding["platform"] = "Grip Invest"
            Ror_asset = int(input("Enter the your choice:- \n"
                                        "1.10%\n" 
                                        "2.11%\n"
                                        "3.12%\n"
                                        "4.specify\n"))
            if Ror_asset == 1:
                holding["rate"] = 10.0/100
            elif Ror_asset == 2:
                holding["rate"] = 11.0/100
            elif Ror_asset == 3:
                holding["rate"] = 12.0/100
            else:
                holding["rate"] = (float(input("Enter the rate:- ")))/100
        elif asset_platform == 3:
            holding["platform"] = "India Bonds"
            Ror_asset = int(input("Enter the your choice:- \n"
                                        "1.10%\n" 
                                        "2.11%\n"
                                        "3.12%\n"
                                        "4.specify\n"))
            if Ror_asset == 1:
                holding["rate"] = 10.0/100
            elif Ror_asset == 2:
                holding["rate"] = 11.0/100
            elif Ror_asset == 3:
                holding["rate"] = 12.0/100
            else:
                holding["rate"] = (float(input("Enter the rate:- ")))/100
        elif asset_platform == 4:
            holding["platform"] = input("Enter the your platform no:- ")
            Ror_asset = int(input("Enter the your choice:- \n"
                                        "1.10%\n" 
                                        "2.11%\n"
                                        "3.12%\n"
                                        "4.specify\n"))
            if Ror_asset == 1:
                holding["rate"] = 10.0/100
            elif Ror_asset == 2:
                holding["rate"] = 11.0/100
            elif Ror_asset == 3:
                holding["rate"] = 12.0/100
            else:
                holding["rate"] = (float(input("Enter the rate:- ")))/100
        else:
            print("Invalid input ")
    elif asset_info == "P2P_Lending":
        asset_platform = int(input("Enter the your choice:- \n"
                            "1.Lenden\n" 
                            "2.Specify\n"))
        if asset_platform == 1:
            holding["platform"] = "lenden"
            Ror_asset = int(input("Enter the your choice:- \n"
                            "1.16%\n" 
                            "2.24%\n"
                            "3.30%\n"
                            "4.specify\n"))
            if Ror_asset == 1:
                holding["rate"] = 16.0/100
            elif Ror_asset == 2:
                holding["rate"] = 24.0/100
            elif Ror_asset == 3:
                holding["rate"] = 30.0/100
            else:
                holding["rate"] = (float(input("Enter the rate:- ")))/100
        elif asset_platform == 2:
            holding["platform"] = input("Enter the your platform no:- ")
            Ror_asset = int(input("Enter the your choice:- \n"
                                        "1.16%\n" 
                                        "2.24%\n"
                                        "3.30%\n"
                                        "4.specify\n"))
            if Ror_asset == 1:
                holding["rate"] = 16.0/100
            elif Ror_asset == 2:
                holding["rate"] = 24.0/100
            elif Ror_asset == 3:
                holding["rate"] = 30.0/100
            else:
                holding["rate"] = (float(input("Enter the rate:- ")))/100
        else:
            print("Invalid input ")
    elif asset_info == "etc":
            asset_info = input("enter the type of asset:-")
            holding["asset_type"] = asset_info
            holding["platform"] = input("Enter the your platform no:- ")
            Ror_asset = int(input("Enter the your choice:- \n"
                                        "1.12%\n" 
                                        "2.15%\n"
                                        "3.18%\n"
                                        "4.specify\n"))
            if Ror_asset == 1:
                holding["rate"] = 12.0/100
            elif Ror_asset == 2:
                holding["rate"] = 15.0/100
            elif Ror_asset == 3:
                holding["rate"] = 18.0/100
            else:
                holding["rate"] = (float(input("Enter the rate:- ")))/100


    else:
        print("Invalid choice")

    

    holding["principal"] = float(input("Enter the Principal:- "))
    holding["current_value"] = float(input("Enter the current value:- "))
    holding["sip_amount"] = float(input("Enter the SIP amount:- "))
    holding["start_date"] = input("Enter the start date (YYYY-MM-DD):- ")
    holding["last_updated"] = input("Enter the last updated date (YYYY-MM-DD):- ")
    rule_choice = input(
    "Enter the Reinvestment rule \n"
    "1.none \n"
    "2.full \n"
    "3.partial \n"
    "4.fixed_amount_withdraw:- \n1"
    )
    rule_map = {"1": "none", "2": "full", "3": "partial", "4": "fixed_amount_withdraw"}
    holding["reinvestment_rule"] = rule_map[rule_choice]

    if holding["reinvestment_rule"] == "partial":
        holding["reinvestment_split"] = float(input("Reinvestment split % :- "))
    else:
        holding["reinvestment_split"] = 0

    if holding["reinvestment_rule"] == "fixed_amount_withdraw":
        holding["withdraw_amount"] = float(input("Fixed monthly withdrawal amount:- "))
    else:
        holding["withdraw_amount"] = 0

    return holding


while True:
    portfolio = load_portfolio()
    master_rule = int(input("\ndo you want to add new holdings/projection:- \n"
                        "1.Enter the holdings\n" 
                        "2.view holdings \n"
                        "3.Edit holdings \n"
                        "4.Delete holdings \n"
                        "5.Projection of stocks \n"
                        "6.Projection of Mutual funds \n"
                        "7.Projection of Bonds\n"
                        "8.Projection of P2P lending\n"
                        "9.Projection of etc\n"
                        "10.Comprehensive report\n"
                        "11.Exit\n"
                        "\nWhat is your choice:- "))
    if master_rule == 1:
        new_holdings = build_portfolio()
        portfolio.extend(new_holdings)
        save_portfolio(portfolio)
    elif master_rule ==2:
        view_portfolio(portfolio)
        save_portfolio(portfolio)
    elif master_rule == 3:
        edit_holding(portfolio)
    elif master_rule == 4:
        remove_holding(portfolio)
    elif master_rule == 5:
        holding_name = input("Enter the desired holding:- ")
        years = int(input("Enter the number of years:- "))
        holdingif = None
        for h in portfolio:
            if h["name"]== holding_name:
                holdingif = h
                break
        if holdingif:
            result  = project_market(holdingif,years)
            print(f"Projected value in {years} years: {result}")
            save_portfolio(portfolio)
        else:
            print("Holding not found")
            save_portfolio(portfolio)
    elif master_rule == 6:
        holding_name = input("Enter the desired holding:- ")
        years = int(input("Enter the number of years:- "))
        holdingif = None
        for h in portfolio:
            if h["name"]== holding_name:
                holdingif = h
                break
        if holdingif:
            result  = project_market(holdingif,years)
            print(f"Projected value in {years} years: {result}")
            save_portfolio(portfolio)
        else:
            print("Holding not found")
            save_portfolio(portfolio)
    elif master_rule == 7:
        holding_name = input("Enter the desired holding:- ")
        years = int(input("Enter the number of years:- "))
        holdingif = None
        for h in portfolio:
            if h["name"]== holding_name:
                holdingif = h
                break
        if holdingif:
            result  = project_bonds(holdingif,years)
            print(f"Projected value in {years} years: {result}")
            save_portfolio(portfolio)
        else:
            print("Holding not found")
            save_portfolio(portfolio)
    elif master_rule == 8:
        holding_name = input("Enter the desired holding:- ")
        years = int(input("Enter the number of years:- "))
        holdingif = None
        for h in portfolio:
            if h["name"]== holding_name:
                holdingif = h
                break
        if holdingif:
            result  = project_p2p(holdingif,years)
            print(f"Projected value in {years} years: {result}")
            save_portfolio(portfolio)
        else:
            print("Holding not found")
            save_portfolio(portfolio)
    elif master_rule == 9:
        holding_name = input("Enter the desired holding:- ")
        years = int(input("Enter the number of years:- "))
        holdingif = None
        for h in portfolio:
            if h["name"]== holding_name:
                holdingif = h
                break
        if holdingif:
            result  = project_market(holdingif,years)
            print(f"Projected value in {years} years: {result}")
            save_portfolio(portfolio)
        else:
            print("Holding not found")  
            save_portfolio(portfolio)  
    elif master_rule == 10:
        years = int(input("Enter the number of years:- "))
        projections = {}
        for h in portfolio:
            if h["asset_type"] in ("Stocks", "MutualFunds", "etc"):
                projections[h["name"]] = project_market(h, years)
            elif h["asset_type"] == "Bonds":
                projections[h["name"]] = project_bonds(h, years)
            elif h["asset_type"] == "P2P_lending":
                projections[h["name"]] = project_p2p(h, years)
        generate_report(portfolio, projections, years)
        save_portfolio(portfolio)
    elif master_rule == 11:
        save_portfolio(portfolio)
        print("Goodbye!")  
        break  
    else:
        print("Invalid choice")
    
save_portfolio(portfolio)