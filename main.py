# Create a multi-agent system to predict stock price
# Input: Stock name + price
# Create three prices (by code)
# Let agents to guess which is the real price
# Three functions:
## Search function
## Firecrawl function
## Answer submission function

from camel.societies.workforce import Workforce
from camel.tasks import Task

stock_price = float(input("Input the stock price: "))
stock_name = input("Input the stock name: ")

options = [stock_price*0.9, stock_price, stock_price*1.1]

# Setting up workforce
stock_predictor = Workforce("A workforce for predicting the price of a stock")

stock_predictor.add_single_agent_worker()

guesser_task = Task(
    content = "To speculate which of the options is the right answer.",
    id = "0"
)

task = stock_predictor.process_task(guesser_task)
print(task.result)
