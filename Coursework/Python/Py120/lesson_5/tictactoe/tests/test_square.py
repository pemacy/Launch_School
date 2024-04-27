import unittest
from src.square import Square
from src.player import Human

class TestSquare(unittest.TestCase):
    def test_class_initialization_with_int(self):
        s = Square(1)
        assert s.__class__ == Square

    def test_class_initialization_with_str(self):
        s = Square('1')
        assert s.__class__ == Square

    def test_type_error_if_not_initialized_with_str_or_int(self):
        with self.assertRaises(TypeError):
            Square([1])

    def test_position_attribute_initialization_with_str(self):
        s = Square('1')
        assert s.position == '1'

    def test_position_attribute_initialization_with_int(self):
        s = Square(1)
        assert s.position == '1'

    def test_initialized_square_is_empty(self):
        s = Square('1')
        assert s.is_empty() is True

    def test_add_owner(self):
        s = Square('1')
        h = Human()
        s.owner = h

    def test_empty_str_output_when_empty(self):
        s = Square('1')
        spaces = ' ' * 5
        assert str(s) == F"{spaces}|"

    def test_str_output_on_end_square(self):
        s = Square('3')
        spaces = ' ' * 5
        assert str(s) == F"{spaces}\n"

    def test_empty_marker_for_initialized_square(self):
        s = Square('3')
        assert s.marker == ' '

    def test_owner_marker_for_marked_square(self):
        s = Square('3')
        h = Human()
        s.owner = h
        assert s.marker == 'X'
