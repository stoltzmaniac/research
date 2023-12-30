import typer
from stock_analysis.analyze import create_report

from dotenv import load_dotenv
load_dotenv()


app = typer.Typer()

@app.command()
def create_stock_analyis_report(company_name: str):
    create_report(company=company_name)


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()
