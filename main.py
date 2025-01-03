import django
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("WARNING! 90% Of sentiment ")
    data = {'Positive_statements': .23, 'Negative_statements': .31, 'Unclassified_statements': .46 }
    types = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(types, values, color='#7379d6', width=0.4, align='center')
    plt.ylim([0, 1])
    plt.grid(axis='y')
    plt.xlabel("Categorization for .90% accuracy interval")
    plt.ylabel("% of statments in each class")
    plt.title("Sample of 800 posts about Manufacturing stocks in the USA.")
    plt.show()
    plt.savefig('new.png')


if __name__ == "__main__":
    main()
