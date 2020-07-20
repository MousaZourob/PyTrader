# PyTrader
Predictious trading bot that streams market data of specific instruments to buy or sell them. Gets data using **TradingView webhook API** which sends a **JSON** message to an **AWS Lambda** function to execute a **Python** script by using the **AWS Chalice Serverless Framework**. The **Python** script then executes a bracket order using the **Alpaca API**.

### Resources Used: 
* **TradingView webhooks:** https://www.tradingview.com/support/solutions/43000529348-i-want-to-know-more-about-webhooks/
* **AWS Chalice Framework for Serverless Python:** https://github.com/aws/chalice
* **Alpaca API:** https://alpaca.markets/docs/trading-on-alpaca/paper-trading/
