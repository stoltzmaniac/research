from crewai import Task
from textwrap import dedent

class RentalPropertyAnalysisTasks():
  def research(self, agent, company):
    return Task(description=dedent(f"""
        Collect and summarize recent news articles, press
        releases, and market analyses related to the market.
        Pay special attention to any significant events, market
        sentiments, market trends, and analysts' opinions. Also pay special
        attention to demographic data.
  
        Your final answer MUST be a report that includes recommendations
        on the best places to invest in either new or existing
        multifamily real estate commercial properties.
        
        {self.__tip_section()}
  
        Make sure to use the most recent data as possible.
  
        Selected market by the customer: {company}
      """),
      agent=agent
    )
    
  def financial_analysis(self, agent): 
    return Task(description=dedent(f"""
        Conduct a thorough analysis of the real estate market's
        multifamily housing performance. This includes examining
        key metrics such as rent growth, concessions, rent to income ratio,
        affordable housing initiatives.
        
        Also, analyze potential performance in comparison 
        to comparable real estate markets.

        Your final report MUST expand on the summary provided
        but now including a clear assessment of the market's
        financial standing, its strengths and weaknesses, 
        and how it fares against its competitors in the current
        market scenario.{self.__tip_section()}

        Make sure to use the most recent data as possible.
      """),
      agent=agent
    )

  def recommend(self, agent):
    return Task(description=dedent(f"""
        Review and synthesize the analyses provided by the
        Financial Analyst and the Research Analyst.
        Combine these insights to form a comprehensive
        investment recommendation. 
        
        You MUST Consider all aspects, including financial
        health, market sentiment, and qualitative data.

        Make sure to include a section that describes the best
        properties to invest in.

        Your final answer MUST be a recommendation for your
        customer should be a full super detailed report, providing a 
        clear investment stance and strategy with supporting evidence.
        Make it pretty and well formated for your customer.
        {self.__tip_section()}
      """),
      agent=agent
    )

  def __tip_section(self):
    return "If you do your BEST WORK, I'll give you a $10,000 commision!"
