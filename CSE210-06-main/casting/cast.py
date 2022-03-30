"""
Cast class

Holds a list of all the cast in the program.
performs various functions with each cast member 
or the cast as a whole.  
"""


class Cast: 
    def __init__(self) -> None:
        self._actors = {}
    
    def get_actors(self, group) -> list:
        """
        Returns a string of all actors in a given group
        ARGS: self (initializer)
        group(str)
        RTRN: results (list)
        """
        results = []
        if group in self._actors.keys() :
            results = self._actors[group].copy()
        return results
    
    def get_actor_by_index(self, group, index):
        results = []
        if group in self._actors.keys():
            return self._actors[group][index]

    def get_all_actors(self, group) -> list:
        """
        Returns a list of all actors in the cast
        ARGS: self (initializer)
        group(str)
        RTRN: results (list)
        """
        results = []
        for group in self._actors:
            results.extend(self._actors[group])  
        return results      
    
    def get_first_actor(self, group) -> dict:
        """
        Gets the first actor in any given group
        ARGS: self (initializer)
        group(str)
        RTRN: self._actors[group][0] (dict)
        """
        if group in self._actors.keys(): 
            return self._actors[group][0]

    def add_actor(self, group, actor):
        """
        Adds an actor to any group 
        ARGS: self(initializer)
        group(str)
        actor(str)
        """
        if group not in self._actors :
            self._actors[group] = []
        self._actors[group].append(actor)
    
    def clear_actors(self, group):
        """
        Clears all actors 
        ARGS: self (initializer)
        group(str)
        
        """
        if group in self._actors :
            self._actors[group] = []

    def remove_actor(self, group, actor): 
        """
        Removes any actor from a given group
        ARGS: self(initializer)
        group (str)
        actor (str)
        """
        if group in self._actors :
            self._actors[group].remove(actor)
