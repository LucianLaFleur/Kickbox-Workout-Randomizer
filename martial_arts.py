import random
import pygame

class MartialArts:
    def __init__(self): 
        self.seen_once_arr = []
        self.fencing_steps = [
            "shuffle forward",
            "shuffle back",
            "lunge forward", 
            "backstep",
            # "deep left side lunge", 
            # "deep right side lunge",
            # "deep forward lunge",
            "cross-step forward",
            "cross-step back",
            "quarter turn right",
            "quarter turn left",
            "cross-back left",
            "cross-back right"
        ]

        self.directions = [
            "upward",
            "downward",
            "left",
            "right"
        ]

        self.fencing_moves =[
            "ronde-de-ferre", #1-2 motion, weak strong attacking the weapon
            "outward parry",
            "inward parry",
            "feint and switch",
            "slash",
            "stab",
            "grapple and stab",
            "grapple and slash",
            "bind and shove to disengage",
            "backstep disengage",
            "sidestep disengage"
        ]

        #expand on dagger reverse grip moves
        # dagger reverse grip
        self.reverse_grip_dagger = [
            "hook",
            "uppercut",
            "downward fang",
            "jab"
        ]

        self.other_motions = [
        "draw sword from hip",
        "throw dagger from cloak",
        "draw sword from back",
        ""
        ]
         
        self.wide_area_quick_moves = [
            "roundhouse",
            "low roundhouse",
            "side-kick",
            "axe kick",
            "front snap kick",
            "front push kick",
            "falling dragon axe", #spinning axe kick
            "outward wheel kick",
            "inward wheel kick",
            "hook kick",
            "stomp",
            "side-stomp",
            "instep stomp",
            "backwards chop",
            "spinning punch",
            "spinning elbow", 
            "spinning side kick",
            "spinning back kick",
            "backwards elbow"
        ]
        self.kick_single_only_moves = [
            "switch kick",
            "hopping front-kick",
            "hopping side kick",
            "double front kick",
            "back kick",
            "hopping stamp kick",
            "jumping side-kick",
            "jumping inward wheel kick",
            "tornado kick",
            "spinning outward wheel kick",
            "low dodge to flying knee",
            "straight flying knee",
            "crouching sweep kick",
            "feinting cross to front kick",
            "feinting cross to side kick",
            "feinting cross to roundhouse kick",
            "feinting cross to knee",
            "feinting cross to shuffle punch",
            "feinting jab to front kick",
            "feinting jab to side kick",
            "feinting jab to roundhouse kick",
            "feinting jab to knee",
            "feinting jab to superman punch"
        ]

        self.wrestling_move_absurd_list = [
            "overhead axe-handle",
            "rising axe handle",
            "choke slam"
        ]

        self.directional_boxing_arr = [
            "step forward",
            "shuffle forward",
            "shuffle back",
            "backstep"
        ]

        self.boxing_small_steps = [
            "quarter turn step",
            "stepping inward parry",
            "stepping outward parry",
            "high block",
            "low block",
            "outward parry",
            # "step forward", 
            # "backstep",
            "quarter turn roll", "quarter turn roll",
            "side-step roll","side-step roll",
            "inward full-circle redirection parry",
            "outward full redirection",
            "low block full redirection",
            "high full redirection",
            "out-sway",
            "in-sway", 
            "back-sway", 
            "ducking sway"
        ]
        self.temp_boxing_small_steps = self.boxing_small_steps

        self.small_area_single_only_moves = [
            "cross-punch",
            "chain punch",
            "straight knee",
            "hooking knee strike",
            "superman punch",
            "heavy palm-strike",
            "back leg flying knee", # jump up
            "front leg flying knee",
            "low shove", # ghost butterfly
            "single-leg shove takedown",
            "lunge for the legs",
            "feinting hook, true jab",
            "feinting jab",
            "feinting cross",
            "feinting hook",
            "feinting jab, true cross",
            "feinting cross, palm strike",
            "feinting jab, palm strike",
            "feinting cross, side chop",
            "feinting jab, karate chop",
            "bell clap",
            "white crane, bell clap",
            "white crane, shove",
            "clothesline strike",
            "outward parry, clothesline",
            "downward elbow strike",
            "choke slam",
            "rising double axe handle",
            "falling double axe handle",
            "outward parry palm strike"
            ]
        self.temp_small_area_single_only_moves = self.small_area_single_only_moves

        self.small_area_quick_moves = [
            "gut punch",
            "quick palm strike",
            "shove", 
            "elbow smash", 
            "elbow jab",
            "straight jab",
            "shuffle-forward jab",
            "sway and jab", 
            "roll and hook",
            "roll and uppercut", 
            "karate chop",
            "side chop",
            "jab",
            "gut punch",
            "backhand",
            "inner parry",
            "outward parry",
            "throat punch",
            "out-sway", "in-sway", "back-sway", "ducking sway"
        ]
        self.temp_small_area_quick_moves = self.small_area_quick_moves

        self.all_moves_arr = []
        for x in self.small_area_single_only_moves:
            self.all_moves_arr.append(x)
        for y in self.small_area_quick_moves:
            self.all_moves_arr.append(y)

    def get_random_item_from_target_arr(self, src_arr, temp_arr):
        # regen array if empty
        if len(temp_arr) == 0:
            temp_arr = src_arr
        random.shuffle(temp_arr)
        return temp_arr.pop()

    def get_move_number(self, ):
        d100_roll1 = random.randint(1, 100)
        # 20% chance for 3 moves, 65% chance for 2 moves, 25% for 1 move
        if d100_roll1 > 79:
            # print(f"roll for n-motions {d100_roll1}: [!] 90+ so n=3 !!!")
            num_of_items_in_chain = 3
        if d100_roll1 > 25:
            # print(f"roll for n-motions {d100_roll1}: above 35, so n=2")
            num_of_items_in_chain = 2
        else:
            num_of_items_in_chain = 1
            # print(f"roll for n-motions {d100_roll1}: less than 35, so n=1")
        return num_of_items_in_chain

    def get_step_array(self, lesser_percent_arr, destructable_bulky_percent_arr, original_bulky_arr):
        d100_roll2 = random.randint(1, 100)
        # 60% chance for step, 30% of which is directional 30% for other, # 40% chance for for no step
        if d100_roll2 > 69:
            # print(f"roll for step {d100_roll2}: over 70, primary directional added!")
            chosen_step = random.choice(lesser_percent_arr)
        elif d100_roll2 > 39:
            # print(f"roll for step {d100_roll2}: over 40, less than 70, random other step")
            if len(destructable_bulky_percent_arr) > 0:
                random.shuffle(destructable_bulky_percent_arr)
                chosen_step = destructable_bulky_percent_arr.pop()
            else:
                destructable_bulky_percent_arr = original_bulky_arr
                random.shuffle(destructable_bulky_percent_arr)
                chosen_step = destructable_bulky_percent_arr.pop()
        else:
            # print(f"roll for step {d100_roll2}: less than 40, no step added to move")
            # give an empty array if "no step" gets rolled
            return []
        return [chosen_step]
    
#  give True 30% chance of time, False 70%
    # def roll_for_side_aimed_or_not(self):
    #     d100_roll2 = random.randint(1, 100)
    #     if d100_roll2 > 69:
    #         return True 
    #     else:
    #         return False

    def get_boxing_items(self):
        single_exercise_combo_arr = []
        # get the number of moves in the chain
        n_for_exercise = self.get_move_number()
        movement_arr = self.get_step_array(self.directional_boxing_arr, self.temp_boxing_small_steps, self.boxing_small_steps)
    #  allow quick moves to be repeated, so you can have "karate chop, karate chop"
        destructable_moves_arr = self.all_moves_arr
        for y in range(n_for_exercise):
            if len(destructable_moves_arr) == 0:
                destructable_moves_arr = self.all_moves_arr
                # reset the seen once array since we're regenerating a new cycle
                self.seen_once_arr = []
        # make a copy of the all-moves-array so I can pop off unrepeatable moves
        # if it's the first pass, add the item straight (minor tech. save on processing the "any" comparison)
            random.shuffle(destructable_moves_arr)
            chosen_move = destructable_moves_arr[-1]
        # if chosen move is in the "single-only" array
            if n_for_exercise > 1:
                if chosen_move in self.small_area_single_only_moves:
                    verified_unrepeatable_move = destructable_moves_arr.pop()
                    # print(f"unrepeatable rolled: {verified_unrepeatable_move}")
                    single_exercise_combo_arr.append(verified_unrepeatable_move)
                else:
                    single_exercise_combo_arr.append(chosen_move)
            #  if the move's already been seen once, then delete after using a second time
                if chosen_move in self.seen_once_arr:
                    destructable_moves_arr.pop()
            else:
                single_exercise_combo_arr.append(chosen_move)
            #  after the move is used, add it to the seen-once array.
            self.seen_once_arr.append(chosen_move)
        if movement_arr:
            # print("[!] movement added! ")
            single_exercise_combo_arr.insert(1, movement_arr[0])
        combo_string = ", ".join(single_exercise_combo_arr)
        left_ver = "Left " + combo_string
        right_ver = "Right " + combo_string
        # print(f"output >>> {combo_string}")
        left_right_string_array = [left_ver, right_ver]
        random.shuffle(left_right_string_array)
#check if the shuffled order has Left first by looking at the first letter
        if left_right_string_array[0][0] == "L":
        # return the strings for left/right versions, as well as the components for keywords
                                                        # Is the right side first?
            return left_right_string_array, single_exercise_combo_arr, False
        else:
            return left_right_string_array, single_exercise_combo_arr, True
        
def main():
    obj1 = MartialArts()
    long_arr = []
    sound_bytes_guide_strings = []
    for x in range(3):
        info_arr = obj1.get_boxing_items()
        # combo_str is an array of 2 becasue of mirrored moves for left/right 3/4 stance
        combo_str = info_arr[0]
        long_arr.append(combo_str)
        data_pieces = info_arr[1]
        is_right_side_first = info_arr[2]
        if is_right_side_first:
            arr1 = ["Right"] + data_pieces
            arr2 = ["Left"] + data_pieces
        else:
            arr1 = ["Left"] + data_pieces
            arr2 = ["Right"] + data_pieces
        sound_bytes_guide_strings.append([arr1, arr2])
        
    print(f"strings arr = {long_arr}\n --------- \n audio arr = {sound_bytes_guide_strings}")
    for x in range(len(sound_bytes_guide_strings)):
        # print(f"main arr {long_arr[x]} \n secondary: {sound_bytes_guide_strings[x]}")
        # only 2 length because left/right
        for y in range(2):
            print(f"NAME: {long_arr[x][y]} \n sound-file's key string = {sound_bytes_guide_strings[x][y]}")
            # starting_encouragement_sound = pygame.mixer.Sound(sound_bytes_guide_strings[x][y])
            # starting_encouragement_sound.play()
            # while pygame.mixer.get_busy():  # Wait for the sound to finish playing
            #     pygame.time.Clock().tick(30)
    print("execution over! Congrats!")
if __name__ == "__main__":
    main()       
