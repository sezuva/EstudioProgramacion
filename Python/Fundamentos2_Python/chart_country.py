import read_csv
import charts
data = read_csv.read_csv('./world_population.csv')

def chart_country(data):

    country = input('Escriba el país para ver su población en el tiempo ')
    data_Argentina = list(filter(lambda variable: variable['Country/Territory'] == country, data))
    data_Argentina = data_Argentina[0]
    data_Population = dict(filter(lambda subcadena: ' Population' in subcadena[0] and "Percentage" not in subcadena[0], data_Argentina.items()))
    labels = list(map(lambda cadena: cadena.replace(' Population',''), data_Population.keys()))
    values = list(map(int,data_Population.values()))
    charts.generate_bar_chart(labels, values,'Población de '+country)

if __name__ == '__main__':
    chart_country(data)