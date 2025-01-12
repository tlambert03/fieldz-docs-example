from attrs import define, field


@define
class Thing:
    """Thing.

    Parameters
    ----------
    x : str
        some integer
    """

    x: int = 1
    y: int = field()

    @y.default
    def _y_default(self) -> int:
        """Twice the value of x."""
        return self.x * 2
