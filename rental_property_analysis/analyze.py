from crewai import Crew
from textwrap import dedent

from rental_property_analysis.agents import RentalPropertyAnalysisAgents
from rental_property_analysis.tasks import RentalPropertyAnalysisTasks


class RealEstateCrew:
  def __init__(self, company):
    self.company = company

  def run(self):
    agents = RentalPropertyAnalysisAgents()
    tasks = RentalPropertyAnalysisTasks()

    research_analyst_agent = agents.research_analyst()
    financial_analyst_agent = agents.financial_analyst()
    investment_advisor_agent = agents.investment_advisor()

    research_task = tasks.research(research_analyst_agent, self.company)
    financial_task = tasks.financial_analysis(financial_analyst_agent)
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
        recommend_task
      ],
      verbose=True
    )

    result = crew.kickoff()
    return result


def create_rental_property_analysis_report(market):
   print("## Welcome to Real Estate Analysis Crew")
   print('-------------------------------')
   real_estate_crew = RealEstateCrew(market)
   result = real_estate_crew.run()
   print("\n\n########################")
   print("## Here is the Report")
   print("########################\n")
   print(result)
   return result
