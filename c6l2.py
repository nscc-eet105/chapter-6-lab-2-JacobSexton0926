import matplotlib.pyplot as plt

def plot_linear_equation():
    m = float(input("Enter the slope: "))
    b = float(input("Enter the y-intercept: "))

    x_coords = [x for x in range (-20,21)]
    y_coords = [m * x + b for x in x_coords]

    plt.plot(x_coords,y_coords, label = f'y = {m}x +{b}')
    plt.grid(True)
    plt.axis('square')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()

if __name__ == "__main__":
    plot_linear_equation()
                    
