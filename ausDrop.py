import random

golden_pan_probability = 0.0047
eyelander_probability = 0.015
australium_probability = 0.045

nothing_probability = 1 - (golden_pan_probability + eyelander_probability + australium_probability)

probabilities = [golden_pan_probability, eyelander_probability, australium_probability, nothing_probability]
outcomes = ['Golden Pan', 'Eyelander', 'Australium', 'Other']

results = {'Golden Pan': 0, 'Eyelander': 0, 'Australium': 0, 'Other': 0}

for _ in range(10): #change the range what is your goal tour of mvm, 10 is example.
    result = random.choices(outcomes, probabilities)[0]
    results[result] += 1

for item, count in results.items():
    print(f"{item}: {count} times")