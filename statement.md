# Project Statement

## Project Title

**Portfolio Projection and Management System** [match the README name]

## Problem Statement

An individual investor's money usually sits in several places at once: stocks on one platform, mutual fund SIPs on another, bonds and P2P loans somewhere else. No single screen shows the whole picture, and nothing tells them what it might be worth in ten years. [add a real example from your own portfolio if you're comfortable, e.g. how many platforms you had to check]

This project is a command-line portfolio manager that fixes that. Holdings are stored in a local JSON file. Each one is projected forward using rules that suit its asset type, and everything comes together in one report showing current and estimated future value.

## Scope

**In scope**

- Tracking and projecting a personal portfolio locally, on one machine.
- Stocks, mutual funds, bonds, P2P lending, and custom asset types.
- Creating, viewing, updating and deleting holdings.
- Projecting future value over a number of years the user chooses.
- A consolidated report of current and projected values, per holding and for the whole portfolio.
- Saving everything to `portfolio.json` so data survives between runs.

**Out of scope** [confirm each of these is true for your project]

- Live market prices or any online data.
- Tax calculation.
- Multiple users, logins, or cloud sync.
- A graphical or web interface.

## Target Users

- Individual investors who want a simple, local tracker that handles more than one asset class.
- People who want a rough estimate of long-term growth, not a precise forecast.
- Anyone who wants to see their portfolio projected over a time span they choose.

## Key Features

1. **Data entry:** add a holding and record its details in one pass. [state how many prompts or steps it takes, if you want to keep a claim about speed]
2. **Portfolio management:** view, edit and delete saved holdings.
3. **Projection engine:** estimates future value using rules specific to each asset type, plus user-defined rules for custom assets.
4. **Reporting:** compares current and projected totals for each holding and for the portfolio overall.
5. **Local storage:** saves and reloads data from `portfolio.json`.