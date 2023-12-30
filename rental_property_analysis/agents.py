from crewai import Agent
from langchain.llms import Ollama

from rental_property_analysis.tools.browser_tools import BrowserTools
from rental_property_analysis.tools.calculator_tools import CalculatorTools
from rental_property_analysis.tools.search_tools import SearchTools
from rental_property_analysis.tools.sec_tools import SECTools

from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool


llm = Ollama(model="llama2:13b")

class RentalPropertyAnalysisAgents():
  def financial_analyst(self):
    return Agent(
      role='The Best Multifamily Apartment Financial Analyst',
      goal="""Impress all real estate investors with real estate property knowledge, data, 
      and market trends analysis""",
      backstory="""The most seasoned real estate financial analyst with 
      lots of expertise in multifamily housing and apartments analysis and investment
      strategies that is working for a important large commercial real estate investment firms.""",
      verbose=True,
      llm=llm,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        CalculatorTools.calculate
      ]
    )

  def research_analyst(self):
    return Agent(
      role='Staff Research Analyst',
      goal="""Being the best at gather, interpret data and amaze
      your customer with it""",
      backstory="""Known as the BEST research analyst, you're
      skilled in sifting through news, company announcements, 
      and market sentiments. Now you're working for super 
      important commercial real estate investment firm clients.""",
      verbose=True,
      llm=llm,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        SearchTools.search_news,
        YahooFinanceNewsTool()
      ]
  )

  def investment_advisor(self):
    return Agent(
      role='Private Investment Advisor',
      goal="""Impress your customers with full analyses over stocks
      and complete investment recommendations""",
      backstory="""You're the most experienced real estate investment advisor
      and you combine various analytical insights to formulate
      strategic investment advice. You are now working for important
      commercial real estate investment firm clients you need to impress.""",
      verbose=True,
      llm=llm,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        SearchTools.search_news,
        CalculatorTools.calculate,
        YahooFinanceNewsTool()
      ]
    )

