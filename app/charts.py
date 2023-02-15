import matplotlib.pyplot as plt

def generate_bar_chat(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def generate_pie_chat(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b','c']
  values= [40,100,150]
  #generate_bar_chat(labels, values)
  generate_pie_chat(labels, values)