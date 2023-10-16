import matplotlib.pyplot as plt

def generate_bar_chart(labels,values,title):
    """Bar chart function \n 
    Arguments:
    labels: Receives a list of label titles on the x-axis
    values: Receives a list of values on the y-axis
    title: Receives the chart name"""
    
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    ax.set_title(title)
    plt.show()

def generate_pie_chat(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.show()

