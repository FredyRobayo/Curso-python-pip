import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America', data))
  
  countrys = list(map(lambda x: x['Country/Territory'], data))
  porcenta = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chat(countrys, porcenta)
  country = input('Type Country = ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chat(country['Country/Territory'], labels, values)

if __name__ == '__main__':
  run()