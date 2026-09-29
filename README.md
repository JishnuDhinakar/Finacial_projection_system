# Financial Projection System

A command-line Python tool for tracking a personal investment portfolio and estimating what it will be worth later. I built it for the Indian market, so the projection rules for stocks, mutual funds, bonds and P2P lending follow how those assets actually behave here. [one line on why you built it, e.g. what you were using before]

Holdings live in a local JSON file (`portfolio.json`). You can add, view, edit and delete them, run a projection for one asset type, or generate a single report showing current and projected value for everything.

**Check the numbers yourself before acting on them, and read the code before you run it.** This is a personal tool, not financial advice. [add anything you know is a weak spot, e.g. tax handling, inflation]

## What it tracks

Each holding stores its name, asset type (stock, mutual fund, bond, P2P lending, or custom), platform, principal, current value, annual return rate, SIP amount, dates, and its withdrawal and reinvestment rules.

## How projections work

- **Stocks and mutual funds:** annual growth plus monthly SIP contributions.
- **Bonds:** coupon treatment and reinvestment choices.
- **P2P lending:** reinvestment and withdrawal choices.

[Add the compounding method and any assumptions, e.g. how monthly SIPs compound against an annual rate. This is what a reader will want to know first.]

## Setup

You need Python 3.8 or later. The only library used is the standard `json` module, so there is nothing to install.

1. Clone or download the repository.
2. Open a terminal in the project folder.
3. Check that everything compiles: `[command, e.g. python -m compileall .]`
4. Run it: `[command, e.g. python main.py]`

## Testing

There are no automated tests yet. I check it by hand, comparing what the program shows against `portfolio.json` each time:

1. View the sample portfolio. [where does it come from?]
2. Add a holding.
3. Edit a field on an existing holding.
4. Delete a holding.
5. Run a projection for each asset type separately.
6. Generate the full report and check the current and projected figures against your own calculation.
7. Delete `portfolio.json` and start the program, and confirm it creates a fresh one.