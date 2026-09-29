# Financial Projection System

A command-line Python tool for tracking a personal investment portfolio and estimating what it will be worth later. It is built for the Indian market, so the projection rules for stocks, mutual funds, bonds and P2P lending follow how those assets are usually treated here. It replaces scattered notes and platform screens with one file and one report.

Holdings live in a local JSON file (`portfolio.json`). You can add, view, edit and delete them, run a projection for one asset type, or generate a single report showing current and projected value for everything.

**Check the numbers yourself before acting on them, and read the code before you run it.** This is a personal tool, not financial advice. It uses a fixed annual rate, so it ignores inflation, tax and fees, and it does not model market swings.

## What it tracks

Each holding stores its name, asset type (stock, mutual fund, bond, P2P lending, or custom), platform, principal, current value, annual return rate, SIP amount, dates, and its withdrawal and reinvestment rules.

## How projections work

- **Stocks and mutual funds:** annual growth plus monthly SIP contributions.
- **Bonds:** coupon treatment and reinvestment choices.
- **P2P lending:** reinvestment and withdrawal choices.

For stocks and mutual funds, each year the current value grows by the annual rate, and then twelve months of SIP contributions are added. Because the SIP is added after the growth step, contributions earn no return in the year they are made, so projections run slightly conservative. Projections start from the current value, not the original principal.

For example, ₹100,000 at 10% a year with a ₹5,000 monthly SIP becomes ₹170,000 after year one (100,000 × 1.10 + 60,000) and ₹247,000 after year two.

## Setup

You need Python 3.8 or later. The only library used is the standard `json` module, so there is nothing to install.

1. Clone or download the repository.
2. Open a terminal in the project folder.
3. Check that everything compiles: `python -m py_compile main.py storage.py growth.py report.py`
4. Run it: `python main.py`

`portfolio.json` holds personal data, so it is not committed to the repository. The program creates it if it does not exist.

## Testing

There are no automated tests yet. I check it by hand, comparing what the program shows against `portfolio.json` each time:

1. View your holdings, adding one first if the file is empty.
2. Add a holding.
3. Edit a field on an existing holding.
4. Delete a holding.
5. Run a projection for each asset type separately.
6. Generate the full report and check the current and projected figures against your own calculation, such as the ₹100,000 example above.
7. Delete `portfolio.json` and start the program, and confirm it creates a fresh one.