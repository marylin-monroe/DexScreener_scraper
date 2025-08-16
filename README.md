<div align="center">
  <img src="https://github.com/user-attachments/assets/5a92bb01-768f-4d48-8dc8-6306224f66f4" width="400" alt="DexScreener"/>
</div>

# DexScreener Scraper

Note, the dexscreener.com domain is cloudflare protected, meaning some requests will fail to get access to an unprotected endpoint, @benedixxion telegram if you need a help with endpoint.

## Why use this?
- **Fast & Lightweight**: 20KB script that doesn't overload your system
- **Cloudflare Bypass**: Custom logic to access protected DexScreener endpoints  
- **Smart Filtering**: Only saves tokens meeting strict growth criteria
- **Continuous Monitoring**: Runs 24/7 with automatic mode switching
- **Clean Output**: JSON format ready for integration with your tools

## What it does
All discovered tokens are filtered by strict criteria and saved to JSON for further processing.

## Filtering Criteria
Only tokens that pass ALL filters are saved (it is obvious that metrics can be changed): 
- **24H Growth**: >= 550%
- **Transactions**: >= 5,000 TXNS
- **Market Cap**: >= $500,000

## Deduplication
- **Contract Level**: Skips already processed token addresses and keep the first one.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Output
The scraper logs contract addresses of tokens that passed all filters:
```
CMx7yon2cLzHcXqgHsKJhuU3MmME6noWLQk2rAycBAGS
ESBCnCXtEZDmX8QnHU6qMZXd9mvjSAZVoYaLKKADBAGS
HtTYHz1Kf3rrQo6AqDLmss7gq5WrkWAaXn3tupUZbonk
🔄 Switched mode
9GtvcnDUvGsuibktxiMjLQ2yyBq5akUahuBs8yANbonk
🔄 Switched mode
```

## Data Structure
Results are saved to `trending_tokens.json`:
```json
{
  "tokens": [
    {
      "mintAddress": "...",
      "symbol": "...",
      "price": "$0.00269320",
      "volume": 6900000.0,
      "price_change_24h": "58,983%",
      "txns": 89966,
      "liquidity": 184000.0,
      "mcap": 2600000.0,
      "source_page": "trending",
      "scraped_at": "2025-07-28T17:53:59.710872"
    }
       ],
  "last_updated": "2025-07-28T17:54:01.807950",
  "total_tokens": 9
}
```

## Schedule
- Runs continuously
- Switches mode every 5 minutes
- Processes all available tokens (typically 100+)
- Maintains rolling history of last 100 tokens in JSON

## Performance
- Processes 100+ tokens per cycle
- Typical output: 5-15 tokens per run that pass filters
- Memory efficient with contract address deduplication

## Integration
The JSON output can be consumed by trading bots, analyzers, or other systems that need filtered Solana token data with high-growth potential.

## Contacts and price
If you are looking for a dex scraper right now, write to me on telegram @benedixxion. The scraper takes up a minimum of space, approximately 20 KB, does not overload your computer at all, and I guarantee that there is no malicious code in it.

Price for full access to the code $20.

## Donations
Donations are appreciated! (Solana)

BAs1wwmoNjxEwNAPCdyax5kzDVkEU53eUZWSeeVUKnYi

## Updates
11/08/2025
changed from pairAddress to token mint address, in the structure itself the name is pairAddress, but in fact inside there is a token mint address - it does not affect the work in any way, you will receive in the structure exactly the token address, but if you wish I can display both pairAddress and token address, as you prefer!
