class Player:

    def __init__(self, name: str, team: str, number: int):
        """
        Class to define a player
        :param name: Name of the player
        :param team: Name of team
        :param number: Number for player
        """
        self.name = name
        self.team = team
        self.number = number

    def announce_player(self) -> str:
        """
        Returns the player announcement
        :return: String of player announcement
        """
        return f"Player Name: {self.name}, Team name: {self.team}, Number: {str(self.number)}"
