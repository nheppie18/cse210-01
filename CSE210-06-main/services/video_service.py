class VideoService: 
    def clear_buffer(self):
        raise NotImplementedError("No clear buffer implemented in base class")
    
    def draw_image(self, image, position):
        raise NotImplementedError("No draw image method implemented in base class")
    
    # def draw_rectangle(self, size, position, color): 
        # raise NotImplementedError("No draw rectangle method implemented in base class")
    
    def draw_text(self, text, position):
        raise NotImplementedError("No draw text method implemented in base class")
    
    def flush_buffer(self):
        """Swaps the buffers, displaying everything that has been drawn on the screen."""
        raise NotImplementedError("not implemented in base class")

    def initialize(self):
        """Initializes underlying video device. This method should be called before the main game 
        loop begins."""
        raise NotImplementedError("not implemented in base class")

    def is_window_open(self):
        """Whether or not the window is open.
        
        Returns:
            True if the window is open; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")

    def load_fonts(self, directory):
        """Loads all the fonts in the given directory and sub-directories.
        
        Args:
            directory: A string containing the absolute folder path where font files are stored.
        """
        raise NotImplementedError("not implemented in base class")

    def load_images(self, directory):
        """Loads all the images in the given directory and sub-directories.
        
        Args:
            directory: A string containing the absolute folder path where image files are stored.
        """
        raise NotImplementedError("not implemented in base class")

    def release(self):
        """Releases the underlying video device. This method should be called after the game loop 
        has finished running."""
        raise NotImplementedError("not implemented in base class")

    def unload_fonts(self):
        """Unloads all fonts that were previously loaded."""
        raise NotImplementedError("not implemented in base class")

    def unload_images(self):
        """Unloads all images that were previously loaded."""
        raise NotImplementedError("not implemented in base class")