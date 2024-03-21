import random
import pygame
import time

time_per_movement = input("indicate time per movement or x for 60 seconds\n\t>>")
if time_per_movement == "x":
    time_per_movement = 60
elif time_per_movement == "":
    time_per_movement = 60
else:
    try:
        time_per_movement = int(time_per_movement)
    except:
        print(f"invalid integer [{time_per_movement}] put in, defaulting to 60s")
        time_per_movement = 60

class MartialArts:
    def __init__(self): 
        self.voice_43e_dictionary = {
            "backhand": "martial_audio/43e_backhand1.wav",
            "backstep": "martial_audio/43e_backstep_util.wav",
            "back sway": "martial_audio/43e_backSway.wav",
            "bell clap": "martial_audio/43e_bellClap.wav",
            "chain punch": "martial_audio/43e_chainPunch.wav",
            "choke slam": "martial_audio/43e_chokeSlam.wav",
            "cross-punch": "martial_audio/43e_crossPunch.wav",
            "cross-to-knee": "martial_audio/43e_crossToKnee.wav",
            "cross palm strike": "martial_audio/43e_crosstoPalmStrike.wav",
            "cross to shuffle punch": "martial_audio/43e_crossToShufflePunch.wav",
            "double-arm shove":"martial_audio/43e_doubleArmShove.wav",
            "ducking sway":"martial_audio/43e_duckingSway.wav",
            "downward elbow strike":"martial_audio/43e_downwardElbowStrike.wav",
            "elbow jab":"martial_audio/43e_elbowJab1.wav",
            "elbow smash":"martial_audio/43e_elbowSmash.wav",
            "falling double axe handle": "martial_audio/43e_fallingDoubleAxeHandle.wav",
            "feinting hook, true jab" :"martial_audio/43e_feintHookJab.wav",
            "feinting cross":"martial_audio/43e_feintingCross343.wav",
            "feinting cross, side chop":"martial_audio/43e_feintingCrossSideChop.wav",
            "feinting hook":"martial_audio/43e_feintingHook.wav",
            "feinting hook, shove":"martial_audio/43e_feintingHookShove.wav",
            "feinting jab":"martial_audio/43e_feintingJab.wav",
            "feinting jab, true cross":"martial_audio/43e_feintJabTrueCross.wav",
            "knee-feint":"martial_audio/43e_feintKnee_2.wav",
            "gut punch":"martial_audio/43e_gutPunch.wav",
            "heavy palm strike":"martial_audio/43e_heavyPalmStrike.wav",
            "high block":"martial_audio/43e_highBlock.wav",
            "hooking knee strike":"martial_audio/43e_hookingKneeStrike.wav",
            "hook, shove":"martial_audio/43e_hookShove.wav",
            "inner parry":"martial_audio/43e_innerParry.wav",
            "in-sway" :"martial_audio/43e_inwardSway.wav",
            "straight jab" :"martial_audio/43e_jab.wav",
            "jab, karate chop":"martial_audio/43e_jabKarateChop.wav",
            "jab to knee":"martial_audio/43e_jabToKnee.wav",
            "karate chop":"martial_audio/43e_entheusiasticKarateChop.wav",
            "low block":"martial_audio/43e_lowBlock_0.wav",
            "lunge for the legs":"martial_audio/43e_lungeForTheLegs.wav",
            "outward parry":"martial_audio/43e_outwardParry.wav",
            "outward parry palm strike":"martial_audio/43e_outwardParryPalmStrike.wav",
            "out-sway":"martial_audio/43e_outwardSway.wav",
            "quick palm strike":"martial_audio/43e_palmStrike2.wav",
            "quarter turn roll":"martial_audio/43e_quarterTurnRoll.wav",
            "quarter turn step":"martial_audio/43e_quarterTurnStep.wav",
            "roll and uppercut":"martial_audio/43e_rollingUppercut.wav",
            "roll and hook":"martial_audio/43e_rollinHook.wav",
            "shuffle back":"martial_audio/43e_shuffleBack.wav",
            "shuffle forward":"martial_audio/43e_shuffleForward.wav",
            "shuffle-forward jab":"martial_audio/43e_shuffleForwardJab.wav",
            "side chop":"martial_audio/43e_sideChop.wav",
           
            "sidestep roll":"martial_audio/43e_sidestepRoll.wav",
            "step forward":"martial_audio/43e_stepForward_utility.wav",
            "single-leg shove takedown":"martial_audio/43e_singleLegShoveTakedown.wav",
            "straight knee":"martial_audio/43e_straightKnee.wav",
            "outward parry, clothesline":"martial_audio/43e_outwardParryClothesline.wav",
            "throat punch":"martial_audio/43e_throatPunch.wav",
            "white crane, shove":"martial_audio/43e_whiteCraneShove.wav",
            "low shove":"martial_audio/43e_lowShove.wav",
            "feinting jab":"martial_audio/43e_FeintingJab_odd_pronounciation.wav",
            "rising double axe handle":"martial_audio/43e_RisingDoubleAxeHandle.wav",
            "superman punch":"martial_audio/43e_SupermanPunch.wav",
            "white crane, bell clap":"martial_audio/43e_WhiteCraneBellClap.wav",
            # :"martial_audio/.wav",
        }
        self.voice_43e_feint_auds = [
            "martial_audio/43e_feint2.wav",
            "martial_audio/43e_feint.wav"
        ]
        self.voice_43e_left_auds = [
            "martial_audio/43e_left.wav",
            "martial_audio/43e_leftFootForward.wav",
            "martial_audio/43e_leftFootForward2.wav",
            "martial_audio/43e_leftSide.wav"
        ]
        self.voice_43e_right_auds = [
            "martial_audio/43e_right.wav",
            "martial_audio/43e_rightfootforward.wav",
            "martial_audio/43e_rightFootForward2.wav",
            "martial_audio/43e_rightSide.wav"
        ]

        self.seen_once_arr = []

        self.directional_boxing_arr = [
            "step forward",
            "shuffle forward",
            "sidestep roll",
            "shuffle back",
            "quarter turn roll","quarter turn roll","quarter turn roll","quarter turn roll",
            "quarter turn step","quarter turn step",
            "backstep"
        ]

        self.temp_directional_boxing_arr = self.directional_boxing_arr

        self.boxing_defensive_maneuvers = [
            # "stepping inward parry",
            # "stepping outward parry","stepping outward parry","stepping outward parry",
            "high block",
            "low block",
            "outward parry",
            # "side-step roll","side-step roll",
            # "inward full-circle redirection parry",
            # "outward full redirection",
            # "low block full redirection",
            # "high full redirection",
            "out-sway",
            "in-sway", 
            "back-sway", 
            "ducking sway"
        ]
        self.temp_boxing_defensive_maneuvers = self.boxing_defensive_maneuvers

        self.small_area_single_only_moves = [
            "chain punch",
            "straight knee",
            "superman punch",
            "heavy palm strike",
            # "back leg flying knee", # jump up
            # "front leg flying knee",
            "low shove", # ghost butterfly
            "single-leg shove takedown",
            "lunge for the legs",
            "feinting hook, shove",
            "feinting hook, true jab",
            "feinting jab",
            "knee-feint",
            "feinting cross",
            "feinting hook",
            "feinting jab, true cross",
            # "feinting cross, palm strike",
            # "feinting jab, palm strike",
            "feinting cross, side chop",
            # "feinting jab, karate chop",
            "hook, shove", 
            "cross to shuffle punch",
            "cross-to-knee",
            "bell clap",
            "white crane, bell clap",
            "white crane, shove",
            # "clothesline strike",
            "outward parry, clothesline",
            "downward elbow strike",
            "choke slam",
            "double-arm shove",
            "jab to knee",
            "rising double axe handle",
            "outward parry palm strike"
            ]
        self.temp_small_area_single_only_moves = self.small_area_single_only_moves

        self.small_area_quick_moves = [
            "hooking knee strike",
            "falling double axe handle",
            "cross-punch",
            "cross palm strike",
            "gut punch",
            "quick palm strike",
            "elbow smash", 
            "elbow jab",
            "straight jab",
            "shuffle-forward jab",
            # "sway and jab", 
            "roll and hook",
            "roll and uppercut", 
            "karate chop",
            "side chop",
            "gut punch",
            "jab, karate chop",
            "backhand",
            "inner parry",
            "outward parry",
            "throat punch",
            "out-sway", 
            "in-sway", 
            "back sway", 
            "ducking sway"
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
        # IGNORE: 20% chance for 3 moves, 65% chance for 2 moves, 25% for 1 move
        # if d100_roll1 > 79:
        #     # print(f"roll for n-motions {d100_roll1}: [!] 90+ so n=3 !!!")
        #     num_of_items_in_chain = 3
        # 25% chance for only one move, otherwise, 2
        if d100_roll1 > 25:
            # print(f"roll for n-motions {d100_roll1}: above 35, so n=2")
            num_of_items_in_chain = 2
        else:
            num_of_items_in_chain = 1
            # print(f"roll for n-motions {d100_roll1}: less than 35, so n=1")
        return num_of_items_in_chain

    def get_step_array(self):
        d100_roll2 = random.randint(1, 100)
        # 40% chance to make a step from the directional boxing arr
        if d100_roll2 > 60:
            if len(self.temp_directional_boxing_arr) > 0:
                random.shuffle(self.temp_directional_boxing_arr)
                chosen_step = self.temp_directional_boxing_arr.pop()
            else:
                self.temp_directional_boxing_arr = self.directional_boxing_arr
                random.shuffle(self.temp_directional_boxing_arr)
                chosen_step = self.temp_directional_boxing_arr.pop()
        # 30% chance to get step from defensive arr
        elif d100_roll2 > 30:
            if len(self.temp_boxing_defensive_maneuvers) > 0:
                random.shuffle(self.temp_boxing_defensive_maneuvers)
                chosen_step = self.temp_boxing_defensive_maneuvers.pop()
            else:
                self.temp_boxing_defensive_maneuvers = self.boxing_defensive_maneuvers
                random.shuffle(self.temp_boxing_defensive_maneuvers)
                chosen_step = self.temp_boxing_defensive_maneuvers.pop()
        else:
            # print(f"roll for step {d100_roll2}: less than 30, no step added to move")
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
        movement_arr = self.get_step_array()
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
        
def get_string_list():
    obj1 = MartialArts()
    long_arr = []
    sound_bytes_guide_strings = []
    counter1 = 0
    pygame.mixer.init()
    total_strings_out_arr = []
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
        # print(combo_str)
        sound_bytes_guide_strings.append([arr1, arr2])
        
    # print(f"strings arr = {long_arr}\n --------- \n audio arr = {sound_bytes_guide_strings}")
    for x in range(len(sound_bytes_guide_strings)):
        # print(f"main arr {long_arr[x]} \n secondary: {sound_bytes_guide_strings[x]}")
        # only 2 length because left/right
        for y in range(2):
            temp_soundbyte_arr = []
            counter1 += 1
            soundbyte_arr = sound_bytes_guide_strings[x][y]
            for portion in soundbyte_arr:
                print(portion)
                temp_soundbyte_arr.append(portion)
            temp_soundbyte_arr.append("sound_end_flag")
            total_strings_out_arr.append(temp_soundbyte_arr)
            # print(f"Move #{counter1} : {long_arr[x][y]}")
            # print(f"NAME: {long_arr[x][y]} \n sound-file's key string = {sound_bytes_guide_strings[x][y]}")
            # for z in soundbyte_arr:
            #     if z == "Right":
            #         rand_right_bark = random.choice(obj1.voice_43e_right_auds)
            #         pygame.mixer.Sound(rand_right_bark).play()
            #         while pygame.mixer.get_busy():  # Wait for the sound to finish playing
            #             pygame.time.Clock().tick(30)
            #     elif z == "Left":
            #         rand_left_bark = random.choice(obj1.voice_43e_left_auds)
            #         pygame.mixer.Sound(rand_left_bark).play()
            #         while pygame.mixer.get_busy():  # Wait for the sound to finish playing
            #             pygame.time.Clock().tick(30)
            #     else:
            #         # input(f"target for dictionary is >> {obj1.voice_43e_dictionary[z]}")
            #         audio_bark = obj1.voice_43e_dictionary[z]
            #         pygame.mixer.Sound(audio_bark).play()
            #         while pygame.mixer.get_busy():  # Wait for the sound to finish playing
            #             pygame.time.Clock().tick(30)
            # time.sleep(1)
                    
            # starting_encouragement_sound = pygame.mixer.Sound(sound_bytes_guide_strings[x][y])
            # starting_encouragement_sound.play()
            # while pygame.mixer.get_busy():  # Wait for the sound to finish playing
            #     pygame.time.Clock().tick(30)
    print(total_strings_out_arr)
    for sound_trigger_arr in total_strings_out_arr:
        print(", ".join(sound_trigger_arr[:-1]))
        for sound_trigger_piece in sound_trigger_arr:
            if sound_trigger_piece == "Right":
                rand_right_bark = random.choice(obj1.voice_43e_right_auds)
                pygame.mixer.Sound(rand_right_bark).play()
                while pygame.mixer.get_busy():  # Wait for the sound to finish playing
                    pygame.time.Clock().tick(30)
            elif sound_trigger_piece == "Left":
                rand_left_bark = random.choice(obj1.voice_43e_left_auds)
                pygame.mixer.Sound(rand_left_bark).play()
                while pygame.mixer.get_busy():  # Wait for the sound to finish playing
                    pygame.time.Clock().tick(30)
            elif sound_trigger_piece == "sound_end_flag":
                print("end of audio sequence reached")
                time.sleep(time_per_movement)
            else:
                audio_bark = obj1.voice_43e_dictionary[sound_trigger_piece]
                pygame.mixer.Sound(audio_bark).play()
                while pygame.mixer.get_busy():  # Wait for the sound to finish playing
                    pygame.time.Clock().tick(30)
            
def main():
    get_string_list()

if __name__ == "__main__":
    main()       

#  NYI: side aimed chance exists, but not put into process execution area yet
    #  NYI get kick-included items for outside training
