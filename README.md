# PyTrader
Predictious trading bot that streams market data of specific instruments to buy or sell them. Gets data using **TradingView webhook API** which sends a **JSON** message to an **AWS Lambda** function, this executes a **Python** script running through the **AWS Chalice Serverless Framework**. The **Python** script then executes a bracket order using the **Alpaca API Paper Trading API**. Tested requests using **Insomnia REST API Client**.

### Demo
![image](https://user-images.githubusercontent.com/66835262/89742871-bc13ee00-da6b-11ea-9d8c-ee2e4bcfa645.png)
![image](https://user-images.githubusercontent.com/66835262/89742880-d948bc80-da6b-11ea-90c3-58d0c3d9cfc7.png)

### Resources Used: 
* **TradingView webhooks:** https://www.tradingview.com/support/solutions/43000529348-i-want-to-know-more-about-webhooks/
* **AWS Chalice Framework for Serverless Python:** https://github.com/aws/chalice
* **Alpaca API:** https://alpaca.markets/docs/api-documentation/api-v2/
