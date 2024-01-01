import typer
from stock_analysis.analyze import create_stock_analysis_report
from rental_property_analysis.analyze import create_rental_property_analysis_report
from trip_planner.analyze import create_trip_planner_report

from dotenv import load_dotenv
load_dotenv()


app = typer.Typer()


@app.command()
def rental_property_analysis_report(market_name: str):
    create_rental_property_analysis_report(market=market_name)


@app.command()
def stock_analyis_report(company_name: str):
    create_stock_analysis_report(company=company_name)

@app.command()
def trip_planner_report():
    create_trip_planner_report()


if __name__ == "__main__":
    app()
