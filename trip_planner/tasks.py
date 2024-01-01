from crewai import Task
from textwrap import dedent

class TripPlannerAnalysisTasks():
  def research(self, agent):
    return Task(description=dedent(f"""
                                   Collect information on the best local and tourist activities to do in Honolulu, Hawaii for all of February 2024. Pay close attention to upcoming events and hidden gems.
                                   Utilize local news and sites relevant websites that have information of things to do in the area. Create a list of things to do, with dates associated and links to the information.

                                   
  
        Your final answer MUST be a list that includes recommendations
        on the best things to do or places to visit in Oahu Hawaii, with a particular focus on Honolulu.
        
        {self.__tip_section()}
  
        Make sure to use the most recent data as possible.
      """),
      agent=agent
    )
    
  
  def recommend(self, agent):
    return Task(description=dedent(f"""
        Review and synthesize the research provided by the
        Trip Planner Researcher. Use this information to create a focused list on activities to do, places to visit, and attactions for a family with four kids under the age of five staying in Honolulu for all of February 2024. 
        
        You MUST Consider all aspects of the activities because they must be kid friendly, do not require a flight away from the island, and are not expensive.

        Make sure to include a section that describes why each activity was selected.

        Your final answer MUST be a recommendation for your
        customer. It should be a full super detailed list, providing clear recommendations.
        Make it pretty and well formated for your customer.
        {self.__tip_section()}
      """),
      agent=agent
    )

  def __tip_section(self):
    return "If you do your BEST WORK, I'll give you a $10,000 commision!"
