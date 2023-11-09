import streamlit as st

# Define a function to calculate the mod of base raised to exponent divided by divisor
def mod_pow(base, exponent, divisor):
  # Convert the exponent to binary
  binary = bin(exponent)[2:]
  print(exponent, " -> ", binary)
  # Initialize the result to 1
  result = 1
  # Loop through each bit of the binary from left to right
  for bit in binary:
    # Print the current bit
    print("Current bit:", bit)
    # Square the result and mod by the divisor
    result = (result * result) % divisor
    # Print the intermediate result
    print("Intermediate result:", result)
    # If the bit is 1, multiply the result by the base and mod by the divisor
    if bit == "1":
      print(result, '=' , '(', result, '*', base, ')' ,'%', divisor)
      result = (result * base) % divisor
      # Print the final result
      print("Final result:", result, '\n')
  # Return the result
  return result

# Create a title for the app
st.title("Modular Exponentiation Calculator")

# Write a brief introduction for the app
st.write("This app calculates the mod of base raised to exponent divided by divisor using a fast algorithm.")

# Create three number input widgets for the base, exponent, and divisor
base = st.number_input("Enter base:")
exponent = st.number_input("Enter exponent:")
divisor = st.number_input("Enter divisor:")

# Create a button that triggers the calculation when clicked
if st.button("Calculate"):
  # Display the code in a code block
  st.code(mod_pow(base, exponent, divisor), "python")
  # Write the result of the calculation
  st.write("The result is:", mod_pow(base, exponent, divisor))
