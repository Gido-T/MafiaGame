import random
import json
import math

# Define roles
expedition_roles = ["Janitorial-Worker", "Night-Watch", "Personnel-Officer", "Detective", "Mortician",
"Bouncer", "Blood-Brother", "Insomniac", "Record-Keeper", "Martial-Judge",
"Reserve", "Captain", "Duelist", "Weapons-Master"]

ohne_knotchen_roles = ["Augenlos(Eyeless)", "Seelenlos(Soulless)", "Hirnlos(Brainless)", "Selbstlos(Selfless)",
                        "Stimmlos(Voiceless)", "Gesichtslos(Faceless)", "Lautlos(Soundless)", "Blutlos(Bloodless)"]

cryptid_roles = ["Skin-Walker", "Grim-Reaper", "Wendigo", "Moth-Man"]

solo_roles = ["Identity-Thief", "Spy", "Windergaste", "Serial-Killer", "Necromancer", "Lawyer", "Cult-Fanatic", "Adversaries"]

# Step 1: Get list of players from user
input_names = input("Enter the names of all players, separated by commas: ")
selected_names = [name.strip() for name in input_names.split(',') if name.strip()]

count = len(selected_names)

# Step 2: Choose number of evil and solo roles
max_roles = count - 1  # Leave room for at least 1 expedition role

evil_count = int(input("How many evil roles?:"))
solo_input = input("Enter possible solo role counts (e.g. 1,2,3): ")
try:
    solo_options = [int(val.strip()) for val in solo_input.split(',') if val.strip().isdigit()]
    if not solo_options:
        raise ValueError
    solo_count = random.choice(solo_options)
    print(f"Randomly selected solo count: {solo_count}")
except ValueError:
    print("Invalid input for solo role counts. Please enter numbers separated by commas.")
    exit()

# Step 2.5: Remove restricted roles for smaller groups
filtered_solo_roles = solo_roles.copy()
filtered_ohne_knotchen_roles = ohne_knotchen_roles.copy()
filtered_cryptid_roles = cryptid_roles.copy()
filtered_expedition_roles = expedition_roles.copy()

if count < 8:
    if 'Selbstlos(Selfless)' in filtered_ohne_knotchen_roles:
        filtered_ohne_knotchen_roles.remove('Selbstlos(Selfless)')
    if 'Wendigo' in filtered_cryptid_roles:
        filtered_cryptid_roles.remove('Wendigo')
    if 'Personnel-Officer' in filtered_expedition_roles:
        filtered_expedition_roles.remove('Personnel-Officer')

if count < 7:
    if 'Spy' in filtered_solo_roles:
        filtered_solo_roles.remove('Spy')
    if 'Adversaries' in filtered_solo_roles:
        filtered_solo_roles.remove('Adversaries')

# Step 3: Assign roles
expedition_count = count - evil_count - solo_count

if solo_count <= len(filtered_solo_roles):
    solos = random.sample(filtered_solo_roles, solo_count)
else:
    solos = filtered_solo_roles.copy()
    remaining_count = solo_count - len(solos)
    solos += random.choices(filtered_solo_roles, k=remaining_count)

# Ensure at least one of 'Serial-Killer' or 'Necromancer' if no evil roles
if evil_count == 0 and not any(role in solos for role in ['Serial-Killer', 'Necromancer']):
    forced_role = random.choice(['Serial-Killer', 'Necromancer'])
    # Replace a random solo with the forced one
    replace_index = random.randint(0, len(solos) - 1)
    solos[replace_index] = forced_role

evil_pool = random.choice([filtered_ohne_knotchen_roles, filtered_cryptid_roles])
evils = random.sample(evil_pool, evil_count)

# Handle double 'Selbstlos(Selfless)' case
if 'Selbstlos(Selfless)' in evils:
    evils = ['Selbstlos(Selfless)', 'Selbstlos(Selfless)'] + [role for role in evils if role != 'Selbstlos(Selfless)']
    evil_count = evil_count + 1
    expedition_count = expedition_count - 1

# Handle double 'Adversaries' case
if 'Adversaries' in solos:
    solos = ['Adversaries', 'Adversaries'] + [role for role in solos if role != 'Adversaries']
    solo_count = solo_count + 1
    expedition_count = expedition_count - 1

expeditions = random.sample(filtered_expedition_roles, expedition_count)
roles = solos + evils + expeditions
random.shuffle(roles)

# Assign numbers
role_numbers = list(range(1, math.ceil((count + 1) / 5) * 5 + 1))
role_numbers = random.sample(role_numbers, count)

assignments = sorted(zip(role_numbers, roles, selected_names))

# Output
print("\n--- Assigned Roles ---")
for num, role, name in assignments:
    print(f"{name} ({num}): {role}")

print(f"\nNumbers: {[num for num, _, _ in assignments]}")
