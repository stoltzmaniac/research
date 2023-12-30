from crewai import Crew
from textwrap import dedent

from stock_analysis.agents import StockAnalysisAgents
from stock_analysis.tasks import StockAnalysisTasks


class FinancialCrew:
  def __init__(self, company):
    self.company = company

  def run(self):
    agents = StockAnalysisAgents()
    tasks = StockAnalysisTasks()

    research_analyst_agent = agents.research_analyst()
    financial_analyst_agent = agents.financial_analyst()
    investment_advisor_agent = agents.investment_advisor()

    research_task = tasks.research(research_analyst_agent, self.company)
    financial_task = tasks.financial_analysis(financial_analyst_agent)
    filings_task = tasks.filings_analysis(financial_analyst_agent)
    recommend_task = tasks.recommend(investment_advisor_agent)

    crew = Crew(
      agents=[
        research_analyst_agent,
        financial_analyst_agent,
        investment_advisor_agent
      ],
      tasks=[
        research_task,
        financial_task,
        filings_task,
        recommend_task
      ],
      verbose=True
    )

    result = crew.kickoff()
    return result


def create_report(company):
   print("## Welcome to Financial Analysis Crew")
   print('-------------------------------')
   company = input(
     dedent("""
            What is the company you want to analyize?""")
            )
   financial_crew = FinancialCrew(company)
   result = financial_crew.run()
   print("\n\n########################")
   print("## Here is the Report")
   print("########################\n")
   print(result)
   return result
