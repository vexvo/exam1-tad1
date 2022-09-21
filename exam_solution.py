class Solution:
    def __init__(self):
        self.series = []
        
    def add_series(self):
        serie = {
                        "serie": "",
                        "number_seasons": 0,
                        "original_language": "",
                        "features_seasons": [{
                            "season_number": 0,
                            "season_name": "",
                            "premiere_date": "",
                            "cast": [
                                "",
                                ""
                            ],
                            "episodes": [{
                                "episode_name": "",
                                "time_duration": 0
                            }]
                        }]
                    }
        serie["serie"] = input("What's the name of the series?\n")
        serie["original_language"] = input("What's the series' original language?\n")
        while True:
            try: 
                serie["number_seasons"] = int(input("How many seasons does it have?\n"))
                break
            except:
                print("Expected a numerical value")

        for i in range(serie["number_seasons"]):
            while True:
                try:
                    serie["features_seasons"][0]["season_number"] = int(input("--- Season number: "))
                    break
                except:
                    print("Expected a numerical value")
            serie["features_seasons"][0]["season_name"] = input("--- Season name: ")
            serie["features_seasons"][0]["premiere_date"] = input("--- Premiere date: ")
            
            while True:
                try:
                    cast_size = int(input("Amount of people in the cast: "))
                    break
                except:
                    print("Expected a numerical value")
            for i in range(cast_size):
                serie["features_seasons"][0]["cast"][i] = input(f'--- Actor {i+1}: ')
            serie["features_seasons"][0]["episodes"][0]["episode_name"] = input("--- Episode name: ")
            serie["features_seasons"][0]["episodes"][0]["time_duration"] = input("--- Time durantion: ")

        self.series.append(serie)

    # feature 1
    def featured_actor(self):

        actor_name = input("Name of actor you're searching for: ")

        for i in range(len(self.series)):
            for j in range(len(self.series[i]["features_seasons"][0]["cast"])):
                if actor_name == self.series[i]["features_seasons"][0]["cast"][j]:
                    print(self.series[i]["serie"])

    # feature 2
    def series_same_language(self):
        searched_language = input("Language you wish to look for series in: ")

        for i in range(len(self.series)):
            if searched_language == self.series[i]["original_language"]:
                print(self.series[i]["serie"])

    # feature 3
    def delete_series_by_date(self):
        date_premiered = input("What date did the series premiere: ")
        found = False
        for i in range(len(self.series)):
            for j in range(len(self.series[i]["features_seasons"])):
                if date_premiered == self.series[i]["features_seasons"][j]["premiere_date"]:
                    print(f'Sucessfully removed {self.series[i]["serie"]}')
                    self.series.remove(self.series[i])
                    i += 1
                    j = 0
                    found = True
            
        if found == False:
            print("Was not found")