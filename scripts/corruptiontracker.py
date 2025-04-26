from logging import getLogger


logger = getLogger(__name__)


class CorruptionTrackerType:
    def __init__(self):
        """
        Crée la classe CorruptionTracker
        """
        # Initialise le compteur de corruption
        self._counter = 0

    def __iadd__(self, count: int):
        """
        Incrémente le compteur de corruption
        """
        self._counter += count
        logger.warning(f"CorruptionTracker: {count} corruption(s) detected")
        return self
    
    @property
    def _(self):
        """
        Retourne le compteur de corruption
        """
        return self._counter

CorruptionTracker = CorruptionTrackerType()