from crewai import Agent
from langchain.llms import Ollama

from trip_planner.tools.browser_tools import BrowserTools
from trip_planner.tools.calculator_tools import CalculatorTools
from trip_planner.tools.search_tools import SearchTools
from trip_planner.tools.sec_tools import SECTools

from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool


llm = Ollama(model="openhermes")

class TripPlannerAnalysisAgents():
  def trip_planner_researcher(self):
    return Agent(
      role='The best travel booking researcher in Hawaii.',
      goal="""Impress all clients with families with knowledge of the local area and activities in Honolulu, Hawaii in February 2024.""",
      backstory="""The most seasoned travel agent researcher that knows the best local attractions for both tourists and locals in Honolulu and Oahu. Known as the person who can find things to do that are great for families and are not extremely busy or crowded.""",
      verbose=True,
      llm=llm,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        CalculatorTools.calculate
      ]
    )

  def trip_planner_agent(self):
    return Agent(
      role='The best travel agent in Honolulu, Hawaii',
      goal="""Create itinerary for the entire month of February 2024 for a family with four children under the age of five renting a condo in Hawaii.""",
      backstory="""Known as the best travel agent, you are able to find identify the best places for families to enjoy time in Hawaii without spending a lot of money. You specialize in finding local activities that are fun and easy to do with young children.""",
      verbose=True,
      llm=llm,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        SearchTools.search_news
      ]
  )
