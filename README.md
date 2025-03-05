
# Activation Functions Project

This project contains a set of common activation functions used in neural networks, along with a script that generates plots of these functions and their derivatives. The functions include Sigmoid, Step, Gaussian, Identity, Piecewise Linear, ReLU, Sinusoidal, and Hyperbolic Tangent.

## Functions Included

The following activation functions are implemented in this project:

1. **Sigmoid**: A function that maps real values to the range (0, 1).
2. **Step**: A function that returns 1 if the input is greater than or equal to 0, otherwise returns 0.
3. **Gaussian**: A function shaped like a bell curve, controlled by an amplitude parameter `A`.
4. **Identity**: Returns the same value as the input.
5. **Piecewise Linear**: A piecewise linear function where the output is -1 for `x < -1`, `x` for `-1 <= x <= 1`, and 1 for `x > 1`.
6. **ReLU**: The Rectified Linear Unit (ReLU) activation function, returning 0 for negative values and the value itself for positive inputs.
7. **Sinusoidal**: A sinusoidal function modeled by amplitude, frequency, and phase shift.
8. **Hyperbolic Tangent**: A function that maps any real value to the range (-1, 1).

## Requirements

- Python 3.x
- Required Libraries:
  - `numpy`
  - `matplotlib`

You can install the necessary dependencies by running:

```bash
pip install numpy matplotlib
```

## Project Structure

The project contains the following functions imported from the `src` directory:

- `Sigmoid` (`sigmoid`)
- `Step` (`step`)
- `Gaussian` (`gaussian`)
- `Identity` (`identity`)
- `Piecewise Linear` (`piecewise`)
- `ReLU` (`relu`)
- `Sinusoidal` (`sinusoidal`)
- `Hyperbolic Tangent` (`tanh`)

## Code Description

The main script contains a function `plot_functions()` that:

1. **Generates values** for the `x` axis in the range `-10` to `10` with 400 points of resolution.
2. **Evaluates** the activation functions for these `x` values.
3. **Creates a figure with subplots** to visualize each function in a 4x2 grid layout.
4. **Customizes the plots**: Each function has a unique color and line style, with shading beneath the curves for better visualization.

### Script Details

- **Data Generation**: For each function, the values are evaluated in the interval `-10 <= x <= 10`.
- **Plotting**: `matplotlib` is used to create plots for each function with a 4x2 subplot layout.
- **Styling**: Each plot has a different color and shading under the curve. Additionally, the titles are styled, and the grid is visible to enhance readability.

## Running the Script

To run the script and generate the plots, simply execute the following command in your terminal:

```bash
python script_name.py
```

This will open a window displaying the plots of the activation functions and their derivatives.
