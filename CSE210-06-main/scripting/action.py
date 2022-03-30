class Action:
    """
    Action has to execute something in the game, if it doesn't it'll raise a not implemented error. 
    """ 
    def execute(self, cast, script, callback) :
        """
        execute should be implemented in each child class, if it's not it'll raise a not implemented error
        ARGS: 
        cast (inst of class)
        script(inst of class)
        *callback(inst of class)
        * I don't thinke we need this one. 
        """
        raise NotImplementedError("execute not implemented in base class")