from crewai import Crew
from textwrap import dedent

from trip_planner.agents import TripPlannerAnalysisAgents
from trip_planner.tasks import TripPlannerAnalysisTasks


class TripPlannerCrew:
  def __init__(self):
    pass

  def run(self):
    agents = TripPlannerAnalysisAgents()
    tasks = TripPlannerAnalysisTasks()

    trip_planner_researcher = agents.trip_planner_researcher()
    trip_planner_agent = agents.trip_planner_agent()

    research_task = tasks.research(trip_planner_researcher)
    recommend_task = tasks.recommend(trip_planner_agent)

    crew = Crew(
      agents=[
        trip_planner_researcher,
        trip_planner_agent
      ],
      tasks=[
        research_task,
        recommend_task
      ],
      verbose=True
    )

    result = crew.kickoff()
    return result


def create_trip_planner_report(market):
   print("## Welcome to Trip Planner Crew")
   print('-------------------------------')
   trip_planner_crew = TripPlannerCrew(market)
   result = trip_planner_crew.run()
   print("\n\n########################")
   print("## Here are the recommendations.")
   print("########################\n")
   print(result)
   return result
