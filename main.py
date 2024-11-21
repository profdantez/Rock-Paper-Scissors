import random

# Define possible moves and their counters
MOVES = ['R', 'P', 'S']
counter_move = {'R': 'P', 'P': 'S', 'S': 'R'}

def player(prev_play, opponent_history=[]):
    # Add the previous opponent move to the history
    if prev_play:
        opponent_history.append(prev_play)

    # If we have no history, return a random move
    if not opponent_history:
        return random.choice(MOVES)

    # Pattern Matching Strategy
    # Get the last 3 moves from the opponent to look for a pattern
    recent_moves = ''.join(opponent_history[-3:])
    pattern_counts = {'R': 0, 'P': 0, 'S': 0}

    # Populate pattern counts based on history
    for i in range(len(opponent_history) - 3):
        pattern = ''.join(opponent_history[i:i+3])
        if pattern == recent_moves:
            next_move = opponent_history[i+3]
            pattern_counts[next_move] += 1

    # Predict the opponent's next move based on the most frequent occurrence
    if max(pattern_counts.values()) > 0:
        predicted_move = max(pattern_counts, key=pattern_counts.get)
    else:
        # If no pattern is found, default to a random move
        predicted_move = random.choice(MOVES)

    # Return the counter move to the predicted move
    return counter_move[predicted_move]
