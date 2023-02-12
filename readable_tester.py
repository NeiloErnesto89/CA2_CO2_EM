"""
I took a chunk of Matty's code to try make it a bit more readable for the lads
who have less experience with Python. 
Have a look below and see if it makes more sense. 
The formula is very simply but the naming could improved for readablity 
as it's a group project with an external person grading it so it's good to be
really precise with comments (inline, etc.)

"""

# this is just a simple example of function annotation in Python, it's not needed as there is Duck typing
def calculate_co2_emissions(flight_distance: int) -> int:


   if flight_distance:
       s = 280.21
       plf = 0.82
       cf = 0.74
       a_func = 0.0001
       b_func = 7.104
       c_func = 5044.93
   else:
       s = 153.51
       plf = 0.82
       cf = 0.93
       a_func = 0
       b_func = 2.714
       c_func = 1166.52
    
   x = flight_distance
   cw = 2.40 
   ef = 3.15
   m = 2
   p = 0.54
   af = 0.00038
   afm = 11.68


   function_result = (a_func*x**2) + (b_func*x) + c_func # quadratic equations result
   return function_result / (s * plf)  * (1 - cf) * cw * (ef * m + p) + (af * x) + afm

   
print(calculate_co2_emissions(100)) # just prining the return obj so we can see it in console
print(calculate_co2_emissions(200))