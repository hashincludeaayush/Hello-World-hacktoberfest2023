import math

def reward_function(params):
    # Initialize the reward with a small value
    reward = 0.0001

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    progress = params['progress']
    abs_steering = abs(params['steering_angle'])
    steps = params['steps']

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

     # Calculate the direction in radians, arctan2(dy, dx), the result is (-pi, pi)
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
        # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 20.0
    
    # Max speed for the agent
    MAX_SPEED = 1.1
    speed_rate = speed / MAX_SPEED
    
    # Penalize if car steer too much to prevent zigzag
    ABS_STEERING_THRESHOLD = 30.0
    
    # Penalize for slow speed
    if all_wheels_on_track == True:
     reward += speed_rate * 2
    else:
     reward -= 2.0

    # Reward for going in right direction and doesn't steer too much
    if direction_diff < DIRECTION_THRESHOLD and abs_steering < ABS_STEERING_THRESHOLD:
        reward += speed_rate + 0.1  
    else: 
        reward -= 0.2 

    # Reward for making progress and completing the lap in less time
    reward += 4 * (progress / steps)
        

    return reward
