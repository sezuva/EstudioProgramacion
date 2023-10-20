import read_csv
import charts
data = read_csv.read_csv('./world_population.csv')

def chart_percentage(data):
    data_countries = list(map(lambda variable: variable['Country/Territory'], data))
    data_percentage = list(map(lambda variable: float(variable['World Population Percentage']), data))
    charts.generate_pie_chat(data_countries, data_percentage)

if __name__ == '__main__':
    chart_percentage(data)