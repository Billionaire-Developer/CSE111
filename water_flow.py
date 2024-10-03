def water_column_height(tower_height, tank_height):
    return tower_height + 3 * tank_height / 4

def pressure_gain_from_water_height(height):
    rho = 998.2 
    g = 9.80665
    return rho * g * height / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    rho = 998.2
    return -friction_factor * pipe_length * rho * fluid_velocity**2 / (2000 * pipe_diameter)
