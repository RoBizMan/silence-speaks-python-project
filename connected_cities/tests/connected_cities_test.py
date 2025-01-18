import unittest
from collections import defaultdict
from connected_cities.connected_cities_checker import (
    load_city_node, check_connected_cities
)
from unittest.mock import patch, mock_open


class TestCityConnections(unittest.TestCase):
    
    def setUp(self):
        self.graph = defaultdict(list)
        self.graph['Bengaluru'] = ['Hyderabad', 'Chennai', 'Kochi']
        self.graph['Hyderabad'] = ['Bengaluru', 'Nagpur', 'Vijayawada']
        self.graph['Chennai'] = ['Bengaluru']
        self.graph['Nagpur'] = ['Hyderabad']
        self.graph['Vijayawada'] = ['Hyderabad']
        self.graph['Kochi'] = ['Bengaluru']
        self.graph['Mumbai'] = ['Delhi']
        self.graph['Delhi'] = ['Mumbai', 'Indore']
        self.graph['Kolkata'] = ['Mumbai']
        self.graph['Guwahati'] = ['Ahmedabad', 'Jaipur']
        self.graph['Ahmedabad'] = ['Guwahati']
        self.graph['Jaipur'] = ['Guwahati']
        self.graph['Indore'] = ['Delhi']
    
    def test_check_connected_cities_directly_connected(self):
        """Test direct connectivity between two cities."""
        self.assertTrue(
            check_connected_cities(self.graph, 'Bengaluru', 'Hyderabad')
        )
        self.assertFalse(
            check_connected_cities(self.graph, 'Guwahati', 'Delhi')
        )
    
    def test_check_connected_cities_indirectly_connected(self):
        """Test indirect connectivity between two cities."""
        self.assertTrue(
            check_connected_cities(self.graph, 'Bengaluru', 'Kochi')
        )
        self.assertTrue(
            check_connected_cities(self.graph, 'Kochi', 'Bengaluru')
        )
        self.assertFalse(
            check_connected_cities(self.graph, 'Mumbai', 'Guwahati')
        )
    
    def test_check_connected_cities_not_connected(self):
        """Test if cities are not connected."""
        self.assertTrue(
            check_connected_cities(self.graph, 'Chennai', 'Kochi')
        )
        self.assertFalse(
            check_connected_cities(self.graph, 'Jaipur', 'Kolkata')
        )
    
    def test_check_connected_cities_non_existent(self):
        """Test if one or both cities do not exist in the graph."""
        self.assertTrue(
            check_connected_cities(self.graph, 'Bengaluru', 'Hyderabad')
        )
        self.assertFalse(
            check_connected_cities(self.graph, 'Tokyo', 'Hyderabad')
        )

    def test_load_city_node_valid_file(self):
        """Test loading a valid file (mocked in this case)."""
        mock_graph = {
            'Bengaluru': ['Hyderabad', 'Chennai', 'Kochi'],
            'Hyderabad': ['Bengaluru', 'Nagpur', 'Vijayawada'],
            'Chennai': ['Bengaluru'],
            'Nagpur': ['Hyderabad'],
            'Vijayawada': ['Hyderabad'],
            'Kochi': ['Bengaluru'],
            'Mumbai': ['Delhi'],
            'Delhi': ['Mumbai', 'Indore'],
            'Kolkata': ['Mumbai'],
            'Guwahati': ['Ahmedabad', 'Jaipur'],
            'Ahmedabad': ['Guwahati'],
            'Jaipur': ['Guwahati'],
            'Indore': ['Delhi']
        }
        self.assertEqual(self.graph, mock_graph)
    
    @patch("builtins.open", mock_open(read_data="InvalidLineWithoutComma\n"))
    def test_load_city_node_invalid_format(self):
        """Test loading a file with invalid format."""
        with self.assertRaises(ValueError):
            load_city_node('invalid_file_path.txt')
    
    def test_load_city_node_missing_file(self):
        """Test loading a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            load_city_node('non_existent_file.txt')


if __name__ == "__main__":
    unittest.main()
